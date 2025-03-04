# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from ctypes import CDLL, POINTER, c_char, c_int, c_long, cdll
from ctypes.util import find_library
from pathlib import Path
from typing import Optional, Tuple

from .capabilities import ZWOASI_CAMERA_CAPABILITIES_CTYPE
from .gps import ZWOASI_GPS_DATA_CTYPE
from .info import ZWOASI_CAMERA_INFORMATION_CTYPE
from .mode import ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE
from .utils import get_asi_libary_path

# **************************************************************************************


class ZWOASICameraLib:
    lib: Optional[CDLL] = None

    def __init__(self, version: Tuple[int, int, int]) -> None:
        # Extract the semantic version provided, whereby we ignore patch versions:
        # Internally, we maintain the {major}.{minor} version to be the latest patch.
        major, minor, _ = version

        # where is the asi library path?
        where: Optional[Path] = None

        # We may need to search for the library path using ctypes.util.find_library:
        library_file: Optional[str] = None

        try:
            where = get_asi_libary_path(f"{major}{minor}")
        except FileNotFoundError:
            pass

        # If the SDK path lookup failed, fall back to using ctypes.util.find_library:
        if not where:
            library_file = find_library("ASICamera2")

        if library_file:
            where = Path(library_file)

        # If neither method found the library, raise an error:
        if not where:
            raise FileNotFoundError(
                "ASICamera2 library not found via SDK path or system lookup."
            )

        self.lib = cdll.LoadLibrary(name=where.as_posix())

        # We now have loaded the SDK, so we can begin to configure the C types
        # needed to interop with the C SDK:
        self._configure()

    def _configure(self) -> None:
        if not self.lib:
            raise RuntimeError("Library not loaded.")

        # ASIGetNumOfConnectedCameras:
        self.lib.ASIGetNumOfConnectedCameras.argtypes = []
        self.lib.ASIGetNumOfConnectedCameras.restype = c_int

        # ASICheckCamera:
        self.lib.ASICameraCheck.argtypes = [c_int, c_int]
        self.lib.ASICameraCheck.restype = c_int

        # ASIGetCameraProperty:
        self.lib.ASIGetCameraProperty.argtypes = [
            POINTER(ZWOASI_CAMERA_INFORMATION_CTYPE),
            c_int,
        ]
        self.lib.ASIGetCameraProperty.restype = c_int

        # ASIOpenCamera:
        self.lib.ASIOpenCamera.argtypes = [c_int]
        self.lib.ASIOpenCamera.restype = c_int

        # ASIInitCamera:
        self.lib.ASIInitCamera.argtypes = [c_int]
        self.lib.ASIInitCamera.restype = c_int

        # ASICloseCamera:
        self.lib.ASICloseCamera.argtypes = [c_int]
        self.lib.ASICloseCamera.restype = c_int

        # ASIGetID:
        self.lib.ASIGetID.argtypes = [c_int, POINTER(c_char)]
        self.lib.ASIGetID.restype = c_int

        # ASIGetNumOfControls:
        self.lib.ASIGetNumOfControls.argtypes = [
            c_int,
            POINTER(c_int),
        ]
        self.lib.ASIGetNumOfControls.restype = c_int

        # ASIGetControlCaps:
        self.lib.ASIGetControlCaps.argtypes = [
            c_int,
            c_int,
            POINTER(ZWOASI_CAMERA_CAPABILITIES_CTYPE),
        ]
        self.lib.ASIGetControlCaps.restype = c_int

        # ASIGetControlValue & ASISetControlValue:
        self.lib.ASIGetControlValue.argtypes = [
            c_int,
            c_int,
            POINTER(c_long),
            POINTER(c_int),
        ]
        self.lib.ASIGetControlValue.restype = c_int
        self.lib.ASISetControlValue.argtypes = [
            c_int,
            c_int,
            c_long,
            c_int,
        ]
        self.lib.ASISetControlValue.restype = c_int

        # ASIGetROIFormat & ASISetROIFormat:
        self.lib.ASIGetROIFormat.argtypes = [
            c_int,
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
        ]
        self.lib.ASIGetROIFormat.restype = c_int
        self.lib.ASISetROIFormat.argtypes = [
            c_int,
            c_int,
            c_int,
            c_int,
            c_int,
        ]
        self.lib.ASISetROIFormat.restype = c_int

        # ASIGetStartPos & ASISetStartPos:
        self.lib.ASIGetStartPos.argtypes = [
            c_int,
            POINTER(c_int),
            POINTER(c_int),
        ]
        self.lib.ASIGetStartPos.restype = c_int
        self.lib.ASISetStartPos.argtypes = [
            c_int,
            c_int,
            c_int,
        ]
        self.lib.ASISetStartPos.restype = c_int

        # ASIGetDroppedFrames:
        self.lib.ASIGetDroppedFrames.argtypes = [
            c_int,
            POINTER(c_int),
        ]
        self.lib.ASIGetDroppedFrames.restype = c_int

        # ASIEnableDarkSubtract:
        self.lib.ASIEnableDarkSubtract.argtypes = [
            c_int,
            POINTER(c_char),
        ]
        self.lib.ASIEnableDarkSubtract.restype = c_int

        # ASIDisableDarkSubtract:
        self.lib.ASIDisableDarkSubtract.argtypes = [
            c_int,
        ]
        self.lib.ASIDisableDarkSubtract.restype = c_int

        # ASIStartVideoCapture:
        self.lib.ASIStartVideoCapture.argtypes = [
            c_int,
        ]
        self.lib.ASIStartVideoCapture.restype = c_int

        # ASIStopVideoCapture:
        self.lib.ASIStopVideoCapture.argtypes = [
            c_int,
        ]
        self.lib.ASIStopVideoCapture.restype = c_int

        # ASIGetVideoData:
        self.lib.ASIGetVideoData.argtypes = [
            c_int,
            POINTER(c_char),
            c_long,
            c_int,
        ]
        self.lib.ASIGetVideoData.restype = c_int

        # ASIPulseGuideOn:
        self.lib.ASIPulseGuideOn.argtypes = [
            c_int,
            c_int,
        ]
        self.lib.ASIPulseGuideOn.restype = c_int

        # ASIPulseGuideOff:
        self.lib.ASIPulseGuideOff.argtypes = [
            c_int,
            c_int,
        ]
        self.lib.ASIPulseGuideOff.restype = c_int

        # ASIStartExposure:
        self.lib.ASIStartExposure.argtypes = [
            c_int,
            c_int,
        ]
        self.lib.ASIStartExposure.restype = c_int

        # ASI Stop Exposure:
        self.lib.ASIStopExposure.argtypes = [
            c_int,
        ]
        self.lib.ASIStopExposure.restype = c_int

        # ASIGetExpStatus:
        self.lib.ASIGetExpStatus.argtypes = [
            c_int,
            POINTER(c_int),
        ]
        self.lib.ASIGetExpStatus.restype = c_int

        # ASIGetDataAfterExp:
        self.lib.ASIGetDataAfterExp.argtypes = [
            c_int,
            POINTER(c_char),
            c_long,
        ]
        self.lib.ASIGetDataAfterExp.restype = c_int

        # ASIGetGainOffset:
        self.lib.ASIGetGainOffset.argtypes = [
            c_int,
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
        ]
        self.lib.ASIGetGainOffset.restype = c_int

        # ASIGetCameraMode & ASISetCameraMode:
        self.lib.ASIGetCameraMode.argtypes = [
            c_int,
            POINTER(c_int),
        ]
        self.lib.ASIGetCameraMode.restype = c_int
        self.lib.ASISetCameraMode.argtypes = [
            c_int,
            c_int,
        ]
        self.lib.ASISetCameraMode.restype = c_int

        # ASIGetCameraSupportMode:
        self.lib.ASIGetCameraSupportMode.argtypes = [
            c_int,
            POINTER(ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE),
        ]
        self.lib.ASIGetCameraSupportMode.restype = c_int

        # ASISendSoftTrigger:
        self.lib.ASISendSoftTrigger.argtypes = [
            c_int,
            c_int,
        ]
        self.lib.ASISendSoftTrigger.restype = c_int

        # ASIGetTriggerOutputIOConf & ASISetTriggerOutputIOConf:
        self.lib.ASIGetTriggerOutputIOConf.argtypes = [
            c_int,
            c_int,
            POINTER(c_int),
            POINTER(c_long),
            POINTER(c_long),
        ]
        self.lib.ASIGetTriggerOutputIOConf.restype = c_int
        self.lib.ASISetTriggerOutputIOConf.argtypes = [
            c_int,
            c_int,
            c_int,
            c_long,
            c_long,
        ]
        self.lib.ASISetTriggerOutputIOConf.restype = c_int

        # ASIGetID:
        self.lib.ASIGetID.argtypes = [
            c_int,
            POINTER(c_char * 16),
        ]
        self.lib.ASIGetID.restype = c_int

        # ASIGetSDKVersion:
        self.lib.ASIGetSDKVersion.argtypes = []
        self.lib.ASIGetSDKVersion.restype = POINTER(c_char)

        # ASIGetSerialNumber:
        self.lib.ASIGetSerialNumber.argtypes = [
            c_int,
            POINTER(c_char * 8),
        ]
        self.lib.ASIGetSerialNumber.restype = c_int

        # ASIGPSGetData:
        self.lib.ASIGPSGetData.argtypes = [
            c_int,
            POINTER(ZWOASI_GPS_DATA_CTYPE),
            POINTER(ZWOASI_GPS_DATA_CTYPE),
        ]
        self.lib.ASIGPSGetData.restype = c_int

        # ASIGetDataAfterExpGPS:
        self.lib.ASIGetDataAfterExpGPS.argtypes = [
            c_int,
            POINTER(c_char),
            c_long,
            POINTER(ZWOASI_GPS_DATA_CTYPE),
        ]
        self.lib.ASIGetDataAfterExpGPS.restype = c_int

        # ASIGetVideoDataGPS:
        self.lib.ASIGetVideoDataGPS.argtypes = [
            c_int,
            POINTER(c_char),
            c_long,
            c_int,
            POINTER(ZWOASI_GPS_DATA_CTYPE),
        ]
        self.lib.ASIGetVideoDataGPS.restype = c_int


# **************************************************************************************
