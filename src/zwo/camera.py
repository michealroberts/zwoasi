# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from array import array
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from ctypes import (
    CDLL,
    byref,
    c_char,
    c_char_p,
    c_int,
    c_long,
    cast,
    create_string_buffer,
)
from enum import Enum
from pathlib import Path
from sys import byteorder
from time import sleep
from typing import List, Optional, Tuple, TypedDict

from .capabilities import ZWOASI_CAMERA_CAPABILITIES_CTYPE, ZWOASICameraCapabilities
from .enums import (
    ZWOASIBool,
    ZWOASIControlType,
    ZWOASIErrorCode,
    ZWOASIExposureStatus,
    ZWOASIGuideDirection,
    ZWOASIImageType,
    ZWOASITriggerOutput,
)
from .errors import ZWOASIExposureError, errors
from .gps import ZWOASI_GPS_DATA_CTYPE, ZWOASIGPSData
from .info import ZWOASI_CAMERA_INFORMATION_CTYPE, ZWOASICameraInformation
from .lib import ZWOASICameraLib
from .mode import ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE, ZWOASICameraSupportedMode
from .utils import is_hexadecimal
from .version import ZWOASI_SDK_VERSION

# **************************************************************************************


class BaseDeviceState(Enum):
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    DISCONNECTING = "disconnecting"
    ERROR = "error"


# **************************************************************************************


class ZWOASICameraParams(TypedDict):
    pid: Optional[str]


# **************************************************************************************


class ZWOASIGPSExposureData(TypedDict):
    start: ZWOASIGPSData
    end: ZWOASIGPSData


# **************************************************************************************


def get_all_connected_camera_ids() -> List[int]:
    # Instantiate the ZWO library wrapper for the ASICamera SDK:
    sdk = ZWOASICameraLib(version=ZWOASI_SDK_VERSION)

    # If the SDK library failed to load, raise an error:
    if sdk.lib is None:
        raise RuntimeError("Failed to load the ZWO ASICamera SDK library.")

    # Attempt to get the number of connected cameras:
    number_of_cameras: int = sdk.lib.ASIGetNumOfConnectedCameras()

    # Return a list of camera indices from 0 to the number of connected cameras:
    return list(range(number_of_cameras))


# **************************************************************************************


def is_connected(vid: str, pid: str) -> bool:
    # Instantiate the ZWO library wrapper for the ASICamera SDK:
    sdk = ZWOASICameraLib(version=ZWOASI_SDK_VERSION)

    # If the SDK library failed to load, raise an error:
    if sdk.lib is None:
        raise RuntimeError("Failed to load the ZWO ASICamera SDK library.")

    # Convert the vendor and product IDs to integers from hexadecimal strings and
    # check the camera for the given vendor and product IDs:
    is_connected: int = sdk.lib.ASICameraCheck(int(vid, 16), int(pid, 16))

    # Return True if the camera is connected, otherwise False:
    return is_connected == ZWOASIBool.TRUE


# **************************************************************************************

ZWOASI_VENDOR_ID: str = "03c3"

# **************************************************************************************


class ZWOASICamera(object):
    # The camera's unique identifier:
    id: int

    # The ZWO ASICamera SDK library instance:
    lib: CDLL

    # The version of the device driver:
    sdk_version: Tuple[int, int, int] = ZWOASI_SDK_VERSION

    # Vendor ID for ZWO ASI organisation:
    vid: str = ZWOASI_VENDOR_ID
    # Product ID for the Camera:
    pid: Optional[str] = None
    # Device ID (e.g., to differentiate devices with the same vid and pid):
    did: Optional[str] = None

    # The current state of the device:
    state: BaseDeviceState = BaseDeviceState.DISCONNECTED

    # The camera's information model:
    info: ZWOASICameraInformation

    # The camera's supported mode:
    mode: ZWOASICameraSupportedMode

    # Whether the camera is streaming video:
    is_video_streaming: bool = False

    # Whether the camera is cabable of returning GPS data:
    has_gps_support: bool = False

    def __init__(self, id: int, params: Optional[ZWOASICameraParams] = None) -> None:
        """
        Initialise the base camera interface.

        Args:
            params (Optional[BaseDeviceParameters]): An optional dictionary-like object
                containing device parameters such as vendor ID (vid), product ID (pid),
                or device ID (did).
        """
        self.id = id
        self.pid = params.get("pid", None) if params else None
        self.did = f"{id}"

        # Instantiate the ZWO library wrapper for the ASICamera SDK:
        sdk = ZWOASICameraLib(version=ZWOASI_SDK_VERSION)

        # If the SDK library failed to load, raise an error:
        if sdk.lib is None:
            raise RuntimeError("Failed to load the ZWO ASICamera SDK library.")

        # Set the library instance for this camera:
        self.lib = sdk.lib

        number_of_cameras = self.lib.ASIGetNumOfConnectedCameras()

        if number_of_cameras < 1:
            raise RuntimeError("No ZWO ASI cameras found.")

        if id >= number_of_cameras:
            raise RuntimeError(f"Camera index {id} is out of range.")

        # Attempt to get the camera information model for this device:
        self.info = self.get_configuration()

        # Connect to the camera (which in turn initialises the device):
        self.connect()

    def __del__(self) -> None:
        """
        Clean up the camera instance.

        This method is called when the camera instance is deleted.
        """
        try:
            self.disconnect()
        except Exception:
            pass

    @property
    def device_id(self) -> str:
        """
        Unique identifier for the device.

        Returns:
            str: The unique device identifier.
        """
        return self.did or "ZWO ASI Camera"

    @property
    def vendor_id(self) -> str:
        """
        Optional vendor identifier.

        Returns:
            str: The vendor identifier. Defaults to an empty string.
        """
        return f"0x{self.vid:04x}" if is_hexadecimal(self.vid) else f"{self.vid}"

    @property
    def product_id(self) -> str:
        """
        Optional product identifier.

        Returns:
            str: The product identifier. Defaults to an empty string.
        """
        return f"0x{self.pid:04x}" if is_hexadecimal(self.pid) else f"{self.pid}"

    def get_serial_number(self) -> str:
        # Allocate an 8-character buffer for the serial number:
        serial_number = create_string_buffer(8)

        error: int = self.lib.ASIGetSerialNumber(self.id, byref(serial_number))

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting serial number for index {self.id}. Error: {errors[error]}"
            )

        return serial_number.value.hex()

    def initialise(self, timeout: float = 5.0, retries: int = 3) -> None:
        """
        Initialise the device.

        This method should handle any necessary setup required before the device can be used.
        """

        # Define the initialisation function to be run in a separate thread:
        def do_initialise() -> None:
            # Attempt to open the camera device:
            error: int = self.lib.ASIOpenCamera(self.id)

            if error != ZWOASIErrorCode.SUCCESS:
                raise RuntimeError(
                    f"Failed to open camera {self.id}. Error: {errors[error]}"
                )

            # Attempt to initialise the camera:
            error = self.lib.ASIInitCamera(self.id)

            if error != ZWOASIErrorCode.SUCCESS:
                raise RuntimeError(
                    f"Failed to initialise camera {self.id}. Error: {errors[error]}"
                )

            # Attempt to get the camer mode model for this device:
            self.mode = self.get_mode()

            # Check if the camera is capable of returning GPS data:
            self.has_gps_support = (
                self._get_control_capability(ZWOASIControlType.GPS_SUPPORT_INDICATOR)
                is not None
            )

        # Keep a track of the number of attempts:
        i = 0

        # Try to initialise the camera up to `retries` times, with the given timeout:
        while i < retries:
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(do_initialise)
                try:
                    # Block for up to `timeout` seconds to see if init completes
                    future.result(timeout=timeout)
                    return
                except TimeoutError:
                    # If we have a timeout after the retries are exhausted, raise an exception:
                    if i == retries - 1:
                        raise TimeoutError(
                            f"Camera {self.id} did not initialize within {timeout} seconds "
                            f"after {retries} attempts."
                        )
                except RuntimeError as error:
                    # If we have a runtime error after the retries are exhausted, raise it:
                    if i == retries - 1:
                        raise error

            # Increment the retry counter:
            i += 1

    def reset(self) -> None:
        """
        Reset the device.

        This method should restore the device to its default or initial state.
        """
        # Attempt to reset the camera:
        self.disconnect()

        # Attempt to re-initialise the camera:
        self.connect()

    def connect(self, timeout: float = 5.0, retries: int = 3) -> None:
        """
        Establish a connection to the device.

        This method should implement the operations required to connect to the device.
        """
        # Check that the device is not already connected:
        if self.state not in [BaseDeviceState.DISCONNECTED, BaseDeviceState.ERROR]:
            return

        # Update the device state to connecting:
        self.state = BaseDeviceState.CONNECTING

        try:
            # Attempt to initialise the device:
            self.initialise(timeout=timeout, retries=retries)
        except Exception as e:
            self.state = BaseDeviceState.ERROR
            raise e

        # Update the device state to connected:
        self.state = BaseDeviceState.CONNECTED

    def disconnect(self) -> None:
        """
        Disconnect from the device.

        This method should handle any cleanup or shutdown procedures necessary to safely
        disconnect from the device.
        """
        if self.state == BaseDeviceState.DISCONNECTED:
            return

        # Update state to disconnecting to prevent reconnection:
        self.state = BaseDeviceState.DISCONNECTING

        # If video streaming / capture is active, stop it before closing the camera:
        if self.is_video_streaming:
            self.stop_acquisition()

        # Close the camera to free resources and disconnect:
        error: int = self.lib.ASICloseCamera(self.id)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            self.state = BaseDeviceState.ERROR
            raise RuntimeError(
                f"Error closing camera {self.id}. Error: {errors[error]}"
            )

        # Update state to disconnected after successful disconnection:
        self.state = BaseDeviceState.DISCONNECTED

    def is_connected(self) -> bool:
        """
        Check if the device is connected.

        Returns:
            bool: True if the device is connected; otherwise, False.
        """
        return self.state == BaseDeviceState.CONNECTED

    def is_ready(self) -> bool:
        """
        Check if the device is ready for operation.

        Returns:
            bool: True if the device is ready; otherwise, False.
        """
        # Get the current acquisition status:
        status = self.get_acquisition_status()

        # We are ready if the device is connected and is not currently exposing:
        return (
            self.state == BaseDeviceState.CONNECTED
            and self.info is not None
            and self.mode is not None
            and self.lib is not None
            and status == ZWOASIExposureStatus.IDLE
        )

    def get_id(self) -> int:
        """
        Get the device ID.

        Returns:
            int: The device ID.
        """
        id = create_string_buffer(16)

        # Call the ASIGetID function to get the ID for the camera:
        error: int = self.lib.ASIGetID(c_int(self.id), id)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting ID for index {self.id}. Error: {errors[error]}"
            )

        # Return the value of the id_struct as an integer:
        return int.from_bytes(id.raw[:8], byteorder=byteorder)

    def get_name(self) -> str:
        """
        Get the name of the device.

        Returns:
            str: The device name. The default is "BaseDevice".
        """
        return self.info.name

    def get_description(self) -> str:
        """
        Get a description of the device.

        Returns:
            str: A brief description of the device. Defaults to an empty string.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        return (
            f"{self.info.name} [ID: {self.info.id}] "
            f"- Max Resolution: {self.info.maximum_width} x {self.info.maximum_height}"
        )

    def get_driver_version(self) -> Tuple[int, int, int]:
        """
        Get the version of the device driver as a tuple (major, minor, patch).

        Returns:
            Tuple[int, int, int]: The driver version. Defaults to (0, 0, 0).
        """
        return ZWOASI_SDK_VERSION

    def get_sdk_version(self) -> Tuple[int, int, int]:
        """
        Get the version of the device SDK as a tuple (major, minor, patch).

        Returns:
            Tuple[int, int, int]: The SDK version. Defaults to (0, 0, 0).
        """
        c_version = self.lib.ASIGetSDKVersion()

        # If the version pointer is null, return (0, 0, 0):
        if not c_version:
            return (0, 0, 0)

        version = cast(c_version, c_char_p).value

        if not version:
            return (0, 0, 0)

        # Decode the version string. For example, the string might be "1, 13, 0503"
        try:
            # Split the version string by comma, strip each part, and convert to int.
            parts = [
                int(part.strip()) for part in version.decode("utf-8").strip().split(",")
            ]
            if len(parts) >= 3:
                return (
                    parts[0],  # Major
                    parts[1],  # Minor
                    parts[2],  # Patch
                )
        except Exception:
            pass

        return (0, 0, 0)

    def get_firmware_version(self) -> Tuple[int, int, int]:
        """
        Get the version of the device firmware as a tuple (major, minor, patch).

        Returns:
            Tuple[int, int, int]: The firmware version. Defaults to (0, 0, 0).
        """
        return 0, 0, 0

    def get_capabilities(self) -> List[str]:
        """
        Retrieve a list of capabilities supported by the device.

        Returns:
            List[str]: A list of capability names. Defaults to an empty list.
        """
        capabilities: List[str] = []

        # If the camera is not connected or we haven't initialised:
        if not self.is_connected() or self.info is None:
            return []

        if self.info.is_color:
            capabilities.append("is_color")

        if self.info.is_monochrome:
            capabilities.append("is_monochrome")

        if self.info.is_usb3:
            capabilities.append("is_usb3")

        if self.info.is_usb3_host:
            capabilities.append("is_usb3_host")

        if self.info.has_st4_port:
            capabilities.append("has_st4_port")

        if self.info.has_cooler:
            capabilities.append("has_cooler")

        if self.info.has_external_trigger:
            capabilities.append("has_external_trigger")

        if self.info.has_mechanical_shutter:
            capabilities.append("has_mechanical_shutter")

        return capabilities

    def get_configuration(self) -> "ZWOASICameraInformation":
        """
        Retrieve the current configuration of the camera.

        Returns:
            ZWOASICameraInformation: The current camera configuration.
        """
        c_info = ZWOASI_CAMERA_INFORMATION_CTYPE()

        # Attempt to get the camera property information:
        error: int = self.lib.ASIGetCameraProperty(byref(c_info), self.id)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            self.state = BaseDeviceState.ERROR
            raise RuntimeError(
                f"Error getting camera property for index {self.id}. Error: {errors[error]}"
            )

        # Create a new camera information model from the C struct:
        return ZWOASICameraInformation.from_c_types(c_info)

    def get_mode(self) -> "ZWOASICameraSupportedMode":
        """
        Retrieve the current mode of the camera.

        Returns:
            ZWOASICameraSupportedMode: The current camera mode.
        """
        c_mode = ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE()

        # Create a new camera mode model from the C struct:
        return ZWOASICameraSupportedMode.from_c_types(c_mode)

    def _get_number_of_controls(self) -> int:
        """
        Retrieve the number of controls available for the camera.

        Returns:
            int: The number of control entries.

        Raises:
            RuntimeError: If the number of controls cannot be retrieved.
        """
        if not self.is_connected():
            return 0

        number_of_controls = c_int()

        error: int = self.lib.ASIGetNumOfControls(self.id, number_of_controls)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error retrieving number of controls for camera {self.id}. Error: {errors[error]}"
            )

        return number_of_controls.value

    def _get_control_capability_by_index(
        self, index: int
    ) -> "ZWOASICameraCapabilities":
        """
        Retrieve the capabilities for a specific control index.

        Args:
            index (int): The index of the control.

        Returns:
            ZWOASICameraCapabilities: The control capabilities

        Raises:
            RuntimeError if the SDK call fails.
        """
        if not self.is_connected():
            return ZWOASICameraCapabilities()

        c_capability = ZWOASI_CAMERA_CAPABILITIES_CTYPE()

        error: int = self.lib.ASIGetControlCaps(self.id, index, c_capability)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error retrieving control caps (camera={self.id}, index={index}). Error: {errors[error]}"
            )

        return ZWOASICameraCapabilities.from_c_types(c_capability)

    def _get_control_capability(
        self, control_type: int
    ) -> Optional["ZWOASICameraCapabilities"]:
        """
        Retrieve the capabilities for a specific control type.

        Args:
            control_type (int): The control type.

        Returns:
            ZWOASICameraCapabilities: The control capabilities
        """
        if not self.is_connected():
            return None

        number_of_controls = self._get_number_of_controls()

        for i in range(number_of_controls):
            capability = self._get_control_capability_by_index(i)

            if capability.control_type == control_type:
                return capability

        return None

    def get_region_of_interest(self) -> Tuple[int, int, int, int]:
        if not self.is_connected():
            return 0, 0, 0, 0

        # The width of the ROI:
        w = c_int()
        # The height of the ROI:
        h = c_int()
        # The binning factor (e.g., 1 = 1x1, 2 = 2x2, etc.):
        b = c_int()
        # The type of the image (e.g., 8-bit, 16-bit, etc.):
        t = c_int()

        error: int = self.lib.ASIGetROIFormat(
            self.id, byref(w), byref(h), byref(b), byref(t)
        )

        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting ROI format for index {self.id}. Error: {errors[error]}"
            )

        return w.value, h.value, b.value, ZWOASIImageType(t.value)

    def set_region_of_interest(
        self,
        width: int,
        height: int,
        binning: int,
        image_type: int,
        start_x: Optional[int] = None,
        start_y: Optional[int] = None,
    ) -> None:
        """
        Set the camera's region of interest (ROI) and image format.

        Args:
            width (int): The desired width of the ROI.
            height (int): The desired height of the ROI.
            binning (int): The desired binning factor.
            image_type (int): The desired image type.
        """
        if not self.is_connected():
            return

        if width < 8:
            raise ValueError("Width must be at least 8 pixels.")

        if width > int(self.info.maximum_width / binning):
            raise ValueError(
                "Width exceeds maximum supported value for the binned sensor width"
            )

        if width % 8 != 0:
            raise ValueError("Width must be a multiple of 8 pixels.")

        if height < 2:
            raise ValueError("Height must be at least 2 pixels.")

        if height > int(self.info.maximum_height / binning):
            raise ValueError(
                "Height exceeds maximum supported value for the binned sensor height"
            )

        if height % 2 != 0:
            raise ValueError("Height must be a multiple of 2 pixels.")

        # If the start X position is not provided, center the ROI:
        if start_x is None:
            start_x = int((int(self.info.maximum_width / binning) - width) / 2)

        # If start X is out of bounds, raise an exception:
        if start_x < 0 or start_x + width > int(self.info.maximum_width / binning):
            raise ValueError("Start X is out of bounds.")

        # If the start Y position is not provided, center the ROI:
        if start_y is None:
            start_y = int((int(self.info.maximum_height / binning) - height) / 2)

        # If start Y is out of bounds, raise an exception:
        if start_y < 0 or start_y + height > int(self.info.maximum_height / binning):
            raise ValueError("Start Y is out of bounds.")

        # The width of the ROI:
        w = c_int(width)
        # The height of the ROI:
        h = c_int(height)
        # The binning factor (e.g., 1 = 1x1, 2 = 2x2, etc.):
        b = c_int(binning)
        # The type of the image (e.g., 8-bit, 16-bit, etc.):
        t = c_int(image_type)

        # Set the ROI format:
        error: int = self.lib.ASISetROIFormat(
            self.id, w.value, h.value, b.value, t.value
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error setting ROI format for index {self.id}. Error: {errors[error]}"
            )

        # The start X position of the ROI:
        sx = c_int(start_x)

        # The start Y position of the ROI:
        sy = c_int(start_y)

        # Set the start position of the ROI:
        error = self.lib.ASISetStartPos(self.id, sx, sy)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error setting start position for index {self.id}. Error: {errors[error]}"
            )

    def get_x_size(self) -> int:
        """
        Retrieve the current width of the camera's image frame.

        Returns:
            int: The current width (in pixels) of the camera frame.
        """
        if not self.is_connected():
            return 0

        width, _, _, _ = self.get_region_of_interest()

        return width

    def get_start_x_position(self) -> int:
        """
        Retrieve the current X position of the camera's image frame.

        Returns:
            int: The current X position of the camera frame.
        """
        if not self.is_connected():
            return 0

        start_x = c_int()

        start_y = c_int()

        error: int = self.lib.ASIGetStartPos(self.id, start_x, start_y)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting start position for index {self.id}. Error: {errors[error]}"
            )

        return start_x.value

    def get_y_size(self) -> int:
        """
        Retrieve the current height of the camera's image frame.

        Returns:
            int: The current height (in pixels) of the camera frame.
        """
        if not self.is_connected():
            return 0

        _, height, _, _ = self.get_region_of_interest()

        return height

    def get_start_y_position(self) -> int:
        """
        Retrieve the current Y position of the camera's image frame.

        Returns:
            int: The current Y position of the camera frame.
        """
        if not self.is_connected():
            return 0

        start_x = c_int()

        start_y = c_int()

        error: int = self.lib.ASIGetStartPos(self.id, start_x, start_y)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting start position for index {self.id}. Error: {errors[error]}"
            )

        return start_y.value

    def get_pixel_size_x(self) -> float:
        """
        Retrieve the camera's pixel size in the X dimension.

        Returns:
            float: The size of each pixel (in microns) along the X axis.
        """
        # ZWO ASI cameras have square pixels, so return the same value:
        return self.info.pixel_size

    def get_pixel_size_y(self) -> float:
        """
        Retrieve the camera's pixel size in the Y dimension.

        Returns:
            float: The size of each pixel (in microns) along the Y axis.
        """
        # ZWO ASI cameras have square pixels, so return the same value:
        return self.info.pixel_size

    def get_full_well_capacity(self) -> float:
        """
        Retrieve the sensor's approximate full-well capacity.

        Returns:
            float: The full-well capacity in electrons (e-),
                   or 0.0 if not supported or unknown.
        """
        return self.info.electrons_per_adu * (2**self.info.bit_depth - 1)

    def get_supported_gains(self) -> List[int]:
        """
        Retrieve a list of all supported gain values for the camera, if applicable.

        Returns:
            List[float]: A list of valid gain values in device-specific units.
        """
        if not self.is_connected():
            return []

        minimum = self.get_gain_minimum()
        maximum = self.get_gain_maximum()

        # If minimum > maximum, something is off so return an empty list:
        if minimum > maximum:
            return []

        # Otherwise, return a range from minimum to maximum, with a step of 1:
        return list(range(minimum, maximum + 1, 1))

    def get_gain(self) -> int:
        """
        Retrieve the camera's current gain setting.

        Returns:
            float: The current gain value in device-specific units.
        """
        if not self.is_connected():
            return 0

        gain = c_long()

        # Whether the gain is controlled automatically:
        is_auto = c_int()

        error: int = self.lib.ASIGetControlValue(
            self.id, ZWOASIControlType.GAIN, byref(gain), byref(is_auto)
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting gain for index {self.id}. Error: {errors[error]}"
            )

        return gain.value

    def set_gain(self, gain: int) -> None:
        """
        Set the camera's gain value.

        Args:
            gain (float): The desired gain, in device-specific units.
        """
        """Set gain; disable auto by passing auto=0 to the SDK."""
        if not self.is_connected():
            return

        error: int = self.lib.ASISetControlValue(
            self.id, ZWOASIControlType.GAIN, gain, 0
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error setting gain for index {self.id}. Error: {errors[error]}"
            )

    def get_gain_minimum(self) -> int:
        """
        Retrieve the camera's minimum supported gain value.

        Returns:
            int: The minimum allowed gain setting.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        # Use our helper to find the 'Gain' control:
        capability = self._get_control_capability(ZWOASIControlType.GAIN)

        # If we didn't find the gain control at all, fall back to 0:
        if not capability:
            return 0

        return capability.minimum_value

    def get_gain_maximum(self) -> int:
        """
        Retrieve the camera's maximum supported gain value.

        Returns:
            int: The maximum allowed gain setting.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        # Use our helper to find the 'Gain' control:
        capability = self._get_control_capability(ZWOASIControlType.GAIN)

        # If we didn't find the gain control at all, fall back to 0:
        if not capability:
            return 0

        return capability.maximum_value

    def get_supported_offsets(self) -> List[int]:
        """
        Retrieve a list of all supported offset (or brightness) values for the camera.

        Returns:
            List[float]: A list of valid offset values in device-specific units.
        """
        if not self.is_connected():
            return []

        minimum = self.get_offset_minimum()
        maximum = self.get_offset_maximum()

        # If minimum > maximum, something is off so return an empty list:
        if minimum > maximum:
            return []

        # Otherwise, return a range from minimum to maximum, with a step of 1:
        return list(range(minimum, maximum + 1, 1))

    def get_offset(self) -> int:
        """
        Retrieve the camera's current offset (or brightness) value.

        Returns:
            int: The offset value in device-specific units.
        """
        if not self.is_connected():
            return 0

        offset = c_long()

        # Whether the offset is controlled automatically:
        is_auto = c_int()

        error: int = self.lib.ASIGetControlValue(
            self.id, ZWOASIControlType.OFFSET, byref(offset), byref(is_auto)
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting offset for index {self.id}. Error: {errors[error]}"
            )

        return offset.value

    def set_offset(self, offset: int) -> None:
        """
        Set the camera's offset (brightness) value.

        Args:
            offset (int): The desired offset, in device-specific units.
        """
        if not self.is_connected():
            return

        error: int = self.lib.ASISetControlValue(
            self.id, ZWOASIControlType.OFFSET, offset, 0
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error setting offset for index {self.id}. Error: {errors[error]}"
            )

    def get_offset_minimum(self) -> int:
        """
        Retrieve the camera's minimum supported offset value.

        Returns:
            int: The minimum allowed offset setting.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        # Use our helper to find the 'Offset' control:
        capability = self._get_control_capability(ZWOASIControlType.OFFSET)

        # If we didn't find the gain control at all, fall back to 0:
        if not capability:
            return 0

        return capability.minimum_value

    def get_offset_maximum(self) -> int:
        """
        Retrieve the camera's maximum supported offset value.

        Returns:
            int: The maximum allowed offset setting.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        # Use our helper to find the 'Offset' control:
        capability = self._get_control_capability(ZWOASIControlType.OFFSET)

        # If we didn't find the gain control at all, fall back to 0:
        if not capability:
            return 0

        return capability.maximum_value

    def get_supported_binnings(self) -> List[int]:
        """
        Retrieve a list of all supported binning values for the camera.

        Returns:
            List[int]: A list of valid binning factors.
        """
        if not self.is_connected():
            return []

        # Assume self.info has an attribute 'supported_binnings' which is a list or tuple
        # of integers terminated by 0 (0 indicates end-of-list):
        if not hasattr(self.info, "supported_binnings"):
            return []

        # Return all binning values until a zero is encountered:
        return [
            binning_factor
            for binning_factor in self.info.supported_binnings
            if binning_factor != 0
        ]

    def get_binning_x(self) -> int:
        """
        Retrieve the camera's horizontal binning value.

        Returns:
            int: The binning factor in the X dimension. Defaults to 1 if no binning.
        """
        if not self.is_connected():
            return 1

        _, _, binning_x, _ = self.get_region_of_interest()

        return binning_x

    def set_binning_x(self, binning_x: int) -> None:
        """
        Set the camera's horizontal binning factor.

        Args:
            binning_x (int): The desired binning factor along the X dimension.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        # Retrieve the current region of interest:
        width, height, _, t = self.get_region_of_interest()

        # Update the region of interest with the new binning factor:
        self.set_region_of_interest(width, height, binning_x, t)

    def get_binning_y(self) -> int:
        """
        Retrieve the camera's vertical binning value.

        Returns:
            int: The binning factor in the Y dimension. Defaults to 1 if no binning.
        """
        if not self.is_connected():
            return 1

        _, _, binning_y, _ = self.get_region_of_interest()

        return binning_y

    def set_binning_y(self, binning_y: int) -> None:
        """
        Set the camera's vertical binning factor.

        Args:
            binning_y (int): The desired binning factor along the Y dimension.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        # Retrieve the current region of interest:
        width, height, _, t = self.get_region_of_interest()

        # Update the region of interest with the new binning factor:
        self.set_region_of_interest(width, height, binning_y, t)

    def get_exposure_time_minimum(self) -> float:
        """
        Retrieve the camera's minimum supported exposure time (in seconds).

        Returns:
            float: The smallest valid exposure time, in seconds.
        """
        capability = self._get_control_capability(ZWOASIControlType.EXPOSURE)

        # If we didn't find the exposure control at all, fall back to 0:
        if not capability:
            return 0.0

        # Convert the minimum value from microseconds to seconds:
        return capability.minimum_value / 1_000_000.0

    def get_exposure_time_maximum(self) -> float:
        """
        Retrieve the camera's maximum supported exposure time (in seconds).

        Returns:
            float: The largest valid exposure time, in seconds.
        """
        capability = self._get_control_capability(ZWOASIControlType.EXPOSURE)

        # If we didn't find the exposure control at all, fall back to 0:
        if not capability:
            return 0.0

        # Convert the maximum value from microseconds to seconds:
        return capability.maximum_value / 1_000_000.0

    def get_exposure_time(self) -> float:
        """
        Retrieve the camera's current exposure time (in seconds).

        Returns:
            float: The current exposure duration, in seconds.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        exposure_time = c_long()

        # Whether the exposure is controlled automatically:
        is_auto = c_int()

        error: int = self.lib.ASIGetControlValue(
            self.id, ZWOASIControlType.EXPOSURE, byref(exposure_time), byref(is_auto)
        )

        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting exposure for index {self.id}. Error: {errors[error]}"
            )

        # Convert exposure time from microseconds to seconds:
        return exposure_time.value / 1_000_000.0

    def set_exposure_time(self, exposure_time: float) -> None:
        """
        Set the camera's exposure time (in seconds).

        Args:
            exposure_time (float): The desired exposure duration, in seconds.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        error: int = self.lib.ASISetControlValue(
            self.id,
            ZWOASIControlType.EXPOSURE,
            int(round(exposure_time * 1_000_000)),
            0,
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error setting exposure for index {self.id}. Error: {errors[error]}"
            )

    def get_image_type(self) -> ZWOASIImageType:
        """
        Retrieve the current image type for the camera.

        Returns:
            ZWOASIImageType: The current image type.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        # Retrieve the image type from the region of interest:
        _, _, _, image_type = self.get_region_of_interest()

        return ZWOASIImageType(image_type)

    def set_image_type(self, image_type: ZWOASIImageType) -> None:
        """
        Set the camera's image type.

        Args:
            image_type (ZWOASIImageType): The desired image type.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        # Retrieve the current region of interest:
        width, height, binning, _ = self.get_region_of_interest()

        # Update the region of interest with the new image type:
        self.set_region_of_interest(width, height, binning, image_type)

    def _get_frame_buffer(self) -> Tuple[bytearray, int]:
        """
        Retrieve the frame buffer and size for the camera.

        This default implementation calculates the buffer size based on the current
        ROI and image type (8-bit, 16-bit, or RGB). Subclasses may override this
        method if they need a custom buffer allocation approach.

        Returns:
            Tuple[bytearray, int]: A tuple of (raw byte buffer, buffer size in bytes).
        """
        width, height, _, image_type = self.get_region_of_interest()

        # Calculate the size of the frame buffer:
        buffer_size = width * height

        # Adjust for 16-bit images:
        if image_type == ZWOASIImageType.RAW16:
            buffer_size *= 2

        if image_type == ZWOASIImageType.RGB24:
            buffer_size *= 3

        return bytearray(buffer_size), buffer_size

    def _convert_buffer_to_int_list(self, buffer: bytearray) -> List[int]:
        """
        Convert a bytearray buffer to a list of integers.

        Args:
            buffer (bytearray): The buffer to convert.

        Returns:
            List[int]: The list of integers.
        """
        _, _, _, image_type = self.get_region_of_interest()

        typecode = "H"

        # If the image type is 8-bit, convert the buffer to a list of uint8 integers:
        if image_type == ZWOASIImageType.RAW8 or image_type == ZWOASIImageType.Y8:
            typecode = "B"

        # If the image type is 16-bit, convert the buffer to a list of uint16 integers:
        if image_type == ZWOASIImageType.RAW16:
            typecode = "H"

        # If the image type is 24-bit RGB, convert the buffer to a list of uint8 intergers:
        # Essentially, this is a list of 3-tuples of RGB values, each represented by a uint8:
        if image_type == ZWOASIImageType.RGB24:
            typecode = "B"

        # Convert the bytearray to a list of uint16 integers:
        data = array(typecode, buffer)

        # Return the pixel data as a list of integers:
        return data.tolist()

    def _get_frame(self, is_dark: bool = False) -> List[int]:
        """
        Capture a single full-frame exposure using the current ROI and exposure settings.

        This default implementation:
          1) Starts an exposure via the SDK,
          2) Waits until the camera signals the exposure is complete,
          3) Retrieves the raw image bytes, and
          4) Converts them into a list of pixel values.

        Subclasses may override if they need custom exposure logic.

        Args:
            is_dark (bool): Whether to start a 'dark' exposure (e.g. shutter closed).
                            For certain camera models, this may be handled internally.

        Returns:
            List[int]: A list of pixel values representing the captured frame.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        exposure_time = self.get_exposure_time()

        # Start the exposure and wait for it to complete:
        error: int = self.lib.ASIStartExposure(self.id, is_dark)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error starting exposure for index {self.id}. Error: {errors[error]}"
            )

        # Get the frame buffer and size:
        buffer, size = self._get_frame_buffer()

        c_buffer_reference = c_char * size

        c_buffer = c_buffer_reference.from_buffer(buffer)

        # Wait for the exposure to complete:
        while True:
            # Get the exposure status from the camera:
            status = self.get_acquisition_status()

            # If the exposure is complete, break out of the loop:
            if status == ZWOASIExposureStatus.SUCCESS:
                break

            # If the exposure failed, raise an exception:
            if status == ZWOASIExposureStatus.FAILED:
                raise ZWOASIExposureError(
                    f"Error acquiring frame for index {self.id}. Error: Exposure failed.",
                    status_code=ZWOASIExposureStatus.FAILED,
                )

            # Sleep for 1/10th of the exposure time (which is in seconds):
            # [TBC]: Is this the right way to wait for the exposure to complete?
            sleep(exposure_time / 10)

        # [TBC]: Do we need to explicitly stop the exposure here?
        # error = self.lib.ASIStopExposure(self.id)

        # # If an error occurred, raise an exception:
        # if error != ZWOASIErrorCode.SUCCESS:
        #     raise RuntimeError(
        #         f"Error stopping exposure for index {self.id}. Error: {errors[error]}"
        #     )

        # Get the bytes data from the camera one we have a successful exposure:
        error = self.lib.ASIGetDataAfterExp(self.id, c_buffer, size)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting data after exposure for index {self.id}. Error: {errors[error]}"
            )

        # Convert exposure to immutable bytes to avoid any exported buffer issues:
        return self._convert_buffer_to_int_list(bytearray(c_buffer))

    def _get_video_frame(self, timeout: int = -1) -> List[int]:
        """
        Retrieve a single video frame in live-stream mode.

        This default implementation calls the SDK's ASIGetVideoData function to
        fetch the latest frame. It then converts the retrieved buffer into a list
        of pixel values.

        Subclasses may override if they need special handling of video streaming or
        different buffer post-processing.

        Args:
            timeout (int): Maximum time in milliseconds to wait for a new frame.
                           A value of -1 indicates an infinite wait.

        Returns:
            List[int]: A list of pixel values representing the most recent video frame.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        if not self.is_video_streaming:
            raise RuntimeError(
                "Device is not streaming video. You need to call start_acquisition() first."
            )

        buffer, size = self._get_frame_buffer()

        c_buffer_reference = c_char * size

        c_buffer = c_buffer_reference.from_buffer(buffer)

        # Get the bytes data from the camera one we have a successful exposure:
        error: int = self.lib.ASIGetVideoData(self.id, c_buffer, size, timeout)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting data after exposure for index {self.id}. Error: {errors[error]}"
            )

        # Convert exposure to immutable bytes to avoid any exported buffer issues:
        return self._convert_buffer_to_int_list(bytearray(c_buffer))

    def get_frame(self, is_dark: bool = False) -> List[int]:
        """
        Retrieve a single frame of image data from the camera.

        This method may return pixel data as a list of integers, or an empty list
        if no frame is available.

        Args:
            is_dark (bool): If True, return a dark frame (e.g., with the shutter closed). N.B. Not used when streaming video.

        Returns:
            List[int]: A list of pixel values representing the current frame.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        if not self.is_ready():
            raise RuntimeError("Device is not ready to capture frames.")

        # If we are streaming video, get a video frame, if not, get a single frame:
        return (
            self._get_video_frame()
            if self.is_video_streaming
            else self._get_frame(is_dark=is_dark)
        )

    def get_dropped_frames(self) -> int:
        """
        Retrieve the number of dropped frames since the last call to this method.

        Returns:
            int: The number of dropped frames since acquiring the last frame.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        dropped_frames = c_int()

        error: int = self.lib.ASIGetDroppedFrames(self.id, dropped_frames)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting dropped frames for index {self.id}. Error: {errors[error]}"
            )

        return dropped_frames.value

    def start_acquisition(self) -> None:
        """
        Start continuous data acquisition from the camera.

        This method should handle any hardware or software steps needed to begin
        capturing frames in a streaming or live view mode.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        # If we are already streaming, return early:
        if self.is_video_streaming:
            return

        # Update is_video_streaming after successful acquisition start:
        self.is_video_streaming = True

    def stop_acquisition(self) -> None:
        """
        Stop continuous data acquisition from the camera.

        This method should handle the necessary steps to stop capturing frames,
        release buffers, or do any cleanup required when leaving streaming mode.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        # If we are not streaming, return early:
        if not self.is_video_streaming:
            return

        error: int = self.lib.ASIStopVideoCapture(self.id)

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error starting video capture for index {self.id}. Error: {errors[error]}"
            )

        # Update is_video_streaming after successful acquisition stop:
        self.is_video_streaming = False

    def get_acquisition_status(self) -> ZWOASIExposureStatus:
        """
        Retrieve the current exposure status of the camera.

        Returns:
            ZWOASIExposureStatus: The current exposure status.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        status = c_int()

        error: int = self.lib.ASIGetExpStatus(self.id, byref(status))

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting exposure status for index {self.id}. Error: {errors[error]}"
            )

        return ZWOASIExposureStatus(status.value)

    def has_cooler(self) -> bool:
        """
        Check if this camera supports active cooling.

        Returns:
            bool: True if a cooler is supported; otherwise, False.
        """
        return self.info.has_cooler

    def turn_on_cooler(self) -> None:
        """
        Turn on the camera's cooling system, if available.
        """
        if not self.has_cooler():
            return

        # Turn on the cooler:
        on = 1

        error: int = self.lib.ASISetControlValue(
            self.id, ZWOASIControlType.COOLER_ON_OFF, on, 0
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(f"Error turning off cooler. Error: {errors[error]}")

    def turn_off_cooler(self) -> None:
        """
        Turn off the camera's cooling system, if available.
        """
        if not self.has_cooler():
            return

        # Turn off the cooler:
        off = 0

        error: int = self.lib.ASISetControlValue(
            self.id, ZWOASIControlType.COOLER_ON_OFF, off, 0
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(f"Error turning off cooler. Error: {errors[error]}")

    def turn_on_anti_dew_heater(self) -> None:
        """
        Turn on the camera's anti-dew heater, if available.
        """
        if not self.is_connected():
            return

        # Turn on the anti-dew heater:
        on = 1

        # Turn on the anti-dew heater:
        error: int = self.lib.ASISetControlValue(
            self.id, ZWOASIControlType.ANTI_DEW_HEATER, on, 0
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error turning on anti-dew heater for index {self.id}. Error: {errors[error]}"
            )

    def turn_off_anti_dew_heater(self) -> None:
        """
        Turn off the camera's anti-dew heater, if available.
        """
        if not self.is_connected():
            return

        # Turn off the anti-dew heater:
        off = 0

        # Turn off the anti-dew heater:
        error: int = self.lib.ASISetControlValue(
            self.id, ZWOASIControlType.ANTI_DEW_HEATER, off, 0
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error turning off anti-dew heater for index {self.id}. Error: {errors[error]}"
            )

    def get_temperature(self) -> float:
        """
        Retrieve the current sensor temperature (in °C), if cooling is supported.

        Returns:
            float: The sensor temperature in Celsius, or 0.0 if not applicable.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        temperature = c_long()

        # Whether the temperature is controlled automatically:
        is_auto = c_int()

        error: int = self.lib.ASIGetControlValue(
            self.id,
            ZWOASIControlType.TEMPERATURE_READING,
            byref(temperature),
            byref(is_auto),
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting temperature for index {self.id}. Error: {errors[error]}"
            )

        # N.B. the value of the temperature is the float value * 10, so we divide by 10:
        return temperature.value / 10.0

    def set_temperature(self, temperature: float) -> float:
        """
        Set the camera's target temperature (in °C), if cooling is supported.

        Args:
            temperature (float): The desired sensor temperature in Celsius.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        # If the camera does not support cooling, return the current temperature:
        if not self.has_cooler():
            return self.get_temperature()

        value = int(round(temperature * 10))

        error: int = self.lib.ASISetControlValue(
            self.id, ZWOASIControlType.TARGET_TEMPERATURE, value, 0
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                "Error setting target temperature. Error: {errors[error]}"
            )

        # Return the new target temperature:
        return self.get_temperature()

    def can_pulse_guide(self) -> bool:
        """
        Check if the camera supports pulse guiding.

        Returns:
            bool: True if pulse guiding is supported; otherwise, False.
        """
        # Pulse guiding is only supported if the camera has an ST4 port:
        return self.info.has_st4_port

    def turn_on_pulse_guiding(
        self, direction: ZWOASIGuideDirection = ZWOASIGuideDirection.NORTH
    ) -> None:
        """
        Turn on the camera's pulse guiding feature, if available.

        Args:
            direction (ZWOASIGuideDirection): The direction to guide the mount.
        """
        if not self.is_connected():
            return

        if not self.can_pulse_guide():
            return

        # Turn on pulse guiding in the specified direction:
        error: int = self.lib.ASIPulseGuideOn(self.id, direction)

        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error turning on pulse guiding for index {self.id}. Error: {errors[error]}"
            )

    def turn_off_pulse_guiding(
        self, direction: ZWOASIGuideDirection = ZWOASIGuideDirection.NORTH
    ) -> None:
        """
        Turn off the camera's pulse guiding feature, if available.

        Args:
            direction (ZWOASIGuideDirection): The direction to turn off pulse guiding.
        """
        if not self.is_connected():
            return

        if not self.can_pulse_guide():
            return

        # Turn off pulse guiding in the specified direction:
        error: int = self.lib.ASIPulseGuideOff(self.id, direction)

        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error turning off pulse guiding for index {self.id}. Error: {errors[error]}"
            )

    def turn_on_dark_subtraction(self, filename: Path) -> None:
        """
        Turn on the camera's dark subtraction feature, if available.
        """
        raise NotImplementedError("Dark subtraction is not supported by this library.")

    def turn_off_dark_subtraction(self) -> None:
        """
        Turn off the camera's dark subtraction feature, if available.
        """
        raise NotImplementedError("Dark subtraction is not supported by this library.")

    def is_gps_supported(self) -> bool:
        """
        Check if the camera supports GPS data.

        Returns:
            bool: True if GPS data is supported; otherwise, False.
        """
        try:
            # Use the helper to retrieve the capability for GPS support indicator:
            capability = self._get_control_capability(
                ZWOASIControlType.GPS_SUPPORT_INDICATOR
            )
            return capability is not None
        except Exception:
            return False

    def get_gps_data(self) -> "ZWOASIGPSExposureData":
        """
        Retrieve the current GPS coordinates of the camera.

        Returns:
            ZWOASIGPSExposureData: The GPS data for the exposure start and end times.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        if not self.has_gps_support:
            raise RuntimeError("GPS data is not supported by this camera.")

        # The start time GPS data:
        c_start_gps = ZWOASI_GPS_DATA_CTYPE()

        # The end time GPS data:
        c_end_gps = ZWOASI_GPS_DATA_CTYPE()

        # Call the SDK function to retrieve the GPS data.
        error: int = self.lib.ASIGPSGetData(
            self.id, byref(c_start_gps), byref(c_end_gps)
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting GPS data for index {self.id}. Error: {errors[error]}"
            )

        return ZWOASIGPSExposureData(
            start=ZWOASIGPSData.from_c_types(c_start_gps),
            end=ZWOASIGPSData.from_c_types(c_end_gps),
        )

    def get_frame_and_gps_data(self) -> Tuple[List[int], "ZWOASIGPSData"]:
        """
        Retrieve the GPS data associated with the current frame from the camera.

        Returns:
            Tuple[List[int], ZWOASIGPSData]: A tuple containing the pixel data and GPS
            data for the current frame.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        if not self.has_gps_support:
            raise RuntimeError("GPS data is not supported by this camera.")

        buffer, size = self._get_frame_buffer()

        c_buffer_reference = c_char * size

        c_buffer = c_buffer_reference.from_buffer(buffer)

        # Allocate a C structure for GPS data:
        gps_c_data = ZWOASI_GPS_DATA_CTYPE()

        error: int = self.lib.ASIGetDataAfterExpGPS(
            self.id, byref(c_buffer), size, byref(gps_c_data)
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error retrieving GPS data for camera {self.id}: {errors[error]}"
            )

        # Convert the returned C GPS data into your Python model:
        gps_data = ZWOASIGPSData.from_c_types(gps_c_data)

        # Convert the buffer to a list of integers:
        frame = self._convert_buffer_to_int_list(bytearray(c_buffer))

        return frame, gps_data

    def get_video_frame_and_gps_data(
        self, timeout: int = -1
    ) -> Tuple[List[int], "ZWOASIGPSData"]:
        """
        Retrieve the GPS data associated with the current video frame from the camera.

        Returns:
            Tuple[List[int], ZWOASIGPSData]: A tuple containing the pixel data and GPS
            data for the current video frame.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        if not self.has_gps_support:
            raise RuntimeError("GPS data is not supported by this camera.")

        buffer, size = self._get_frame_buffer()

        c_buffer_reference = c_char * size

        c_buffer = c_buffer_reference.from_buffer(buffer)

        # Allocate a C structure for GPS data:
        gps_c_data = ZWOASI_GPS_DATA_CTYPE()

        error: int = self.lib.ASIGetVideoDataGPS(
            self.id, byref(c_buffer), size, timeout, byref(gps_c_data)
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"Error getting video GPS data for camera {self.id}: {errors[error]}"
            )

        # Convert the returned C GPS data into a Python model:
        gps_data = ZWOASIGPSData.from_c_types(gps_c_data)

        # Convert the buffer to a list of integers:
        frame = self._convert_buffer_to_int_list(bytearray(c_buffer))

        return frame, gps_data

    def has_external_trigger(self) -> bool:
        """
        Check if the camera supports software-triggered exposures.

        Returns:
            bool: True if software-triggered exposures are supported; otherwise, False.
        """
        return self.info.has_external_trigger

    def get_soft_trigger_io_configuration(
        self, pin: ZWOASITriggerOutput
    ) -> Tuple[bool, int, int]:
        """
        Retrieve the configuration for a software trigger output I/O port.

        Args:
            pin (ZWOASITriggerOutput): The trigger output pin to configure.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        if not self.has_external_trigger():
            raise RuntimeError("External trigger is not supported by this camera.")

        # If true, the selected pin will output a high level as a signal when it is
        # effective. Or it will output a low level as a signal.
        # N.B. ASI_BOOL (nonzero means high)
        high = c_int()

        # The delay time of the trigger signal, in microseconds.
        delay = c_long()

        # The duration of the trigger signal, in microseconds.
        duration = c_long()

        error: int = self.lib.ASIGetTriggerOutputIOConf(
            self.id,
            c_int(pin),
            byref(high),
            byref(delay),
            byref(duration),
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"ASIGetTriggerOutputIOConf failed for I/O pin {pin}. Error: {errors[error]}"
            )

        return bool(high.value), delay.value, duration.value

    def set_soft_trigger_io_configuration(
        self,
        pin: ZWOASITriggerOutput,
        high: bool,
        delay: int,
        duration: int,
    ) -> None:
        """
        Set the configuration for a software trigger output I/O port.

        Args:
            pin (ZWOASITriggerOutput): The trigger output pin to configure.
            high (bool): True to output a high signal, False to output a low signal.
            delay (int): The delay time of the trigger signal, in microseconds.
            duration (int): The duration of the trigger signal, in microseconds.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        if not self.has_external_trigger():
            raise RuntimeError("External trigger is not supported by this camera.")

        # Convert pin output to either high (1) or low (0) based on the boolean value:
        output = 1 if high else 0

        error: int = self.lib.ASISetTriggerOutputIOConf(
            self.id,
            c_int(pin),
            c_int(output),
            c_long(delay),
            c_long(duration),
        )

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"ASISetTriggerOutputIOConf failed for I/O pin {pin}. Error: {errors[error]}"
            )

    def send_soft_trigger(self, start: bool) -> None:
        """
        Send a software trigger to the camera

        Args:
            start (bool): True to start the trigger, False to stop it.
        """
        if not self.is_connected():
            raise RuntimeError("Device is not connected.")

        if not self.has_external_trigger():
            raise RuntimeError("External trigger is not supported by this camera.")

        # Either send a soft trigger start (1) or stop (0) signal:
        starts: int = 1 if start else 0

        error: int = self.lib.ASISendSoftTrigger(self.id, c_int(starts))

        # If an error occurred, raise an exception:
        if error != ZWOASIErrorCode.SUCCESS:
            raise RuntimeError(
                f"ASISendSoftTrigger failed for camera {self.id}. Error: {errors[error]}"
            )


# **************************************************************************************
