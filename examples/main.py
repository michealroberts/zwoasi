# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from time import sleep

from zwoasi import ZWOASICamera, ZWOASICameraParams, ZWOASIImageType

# **************************************************************************************


def main() -> None:
    # Let's assume the camera ID is 0 (e.g., only 1 camera is connected):
    id = 0

    # Create a new camera parameters instance (for demonstration purposes we are
    # connecting to a ASI62000M Pro model) which has a pid of "" (empty string):
    params: ZWOASICameraParams = ZWOASICameraParams(pid="620b")

    # Create a new camera instance:
    zwo = ZWOASICamera(id, params)

    # Get the camera id (should be 0):
    cid = zwo.get_id()

    # Get the camera name:
    name = zwo.get_name()

    print(f"Camera ID: {cid}, Name: {name}")

    # Check if the camera is ready, if not return:
    if not zwo.is_ready():
        return

    # Get the camera serial number:
    serial_number = zwo.get_serial_number()

    print(f"Camera serial number: {serial_number}")

    # Get the camera firmware version:
    sdk_version = zwo.get_sdk_version()

    print(f"Camera SDK version: {sdk_version}")

    # Check if your camera is a GPS supported model:
    is_gps_supported = zwo.is_gps_supported()

    print(f"Camera GPS is supported: {is_gps_supported}")

    # Get the camera's capabilities:
    capabilities = zwo.get_capabilities()

    print(f"Camera Capabilities: {capabilities}")

    # Get the camera's region of interest:
    width, height, binning, image_type = zwo.get_region_of_interest()

    print(f"Camera ROI: {width}x{height}, Binning: {binning}, Image Type: {image_type}")

    # Get the camera's width and start x position:
    width = zwo.get_x_size()

    start_x = zwo.get_start_x_position()

    print(f"Camera Width: {width}, Start X: {start_x}")

    # Get the camera's height and start y position:
    height = zwo.get_y_size()

    start_y = zwo.get_start_y_position()

    print(f"Camera Height: {height}, Start Y: {start_y}")

    # Get the camera's pixel size in x:
    pixel_sixe_x = zwo.get_pixel_size_x()

    print(f"Camera Pixel Size X: {pixel_sixe_x}")

    # Get the camera's pixel size in y:
    pixel_sixe_y = zwo.get_pixel_size_y()

    print(f"Camera Pixel Size Y: {pixel_sixe_y}")

    # Get the camera's full well capacity:
    full_well_capacity = zwo.get_full_well_capacity()

    print(f"Camera Full Well Capacity: {full_well_capacity}")

    # Get the camera's supported gain values:
    gains = zwo.get_supported_gains()

    print(f"Camera Supported Gains: {gains[0]} - {gains[-1]}")

    # Set the camera's gain to the last supported value:
    zwo.set_gain(gains[-1])

    # Get the camera's current gain value:
    gain = zwo.get_gain()

    print(f"Camera Gain: {gain}")

    # Get the camera's supported offsets:
    offsets = zwo.get_supported_offsets()

    print(f"Camera Supported Offsets: {offsets[0]} - {offsets[-1]}")

    # Set the camera's offset to the last supported value:
    zwo.set_offset(offsets[-1])

    # Get the camera's current offset value:
    offset = zwo.get_offset()

    print(f"Camera Offset: {offset}")

    binnings = zwo.get_supported_binnings()

    print(f"Camera Supported Binnings: {binnings}")

    # Set the camera's image type to RAW16 (16-bit) enum 2:
    zwo.set_image_type(ZWOASIImageType.RAW16)

    # Get the camera's image type:
    image_type = zwo.get_image_type()

    print(f"Camera Image Type: {image_type}")

    #  Set the x binning to 1x1:
    zwo.set_binning_x(1)

    # Get the x binning:
    binning_x = zwo.get_binning_x()

    print(f"Camera Binning X: {binning_x}")

    # Set the y binning to 1x1:
    zwo.set_binning_y(1)

    # Get the y binning:
    binning_y = zwo.get_binning_y()

    print(f"Camera Binning Y: {binning_y}")

    # Get the minimum exposure time supported:
    min_exposure_time = zwo.get_exposure_time_minimum()

    print(f"Camera Min Exposure Time: {min_exposure_time}")

    # Get the maximum exposure time supported:
    max_exposure_time = zwo.get_exposure_time_maximum()

    print(f"Camera Max Exposure Time: {max_exposure_time}")

    # Set the exposure time to the minimum supported value:
    zwo.set_exposure_time(min_exposure_time)

    # Get the current exposure time:
    exposure_time = zwo.get_exposure_time()

    print(f"Camera Exposure Time: {exposure_time}s")

    # Can the camera do pulse guiding?
    can_pulse_guide = zwo.can_pulse_guide()

    print(f"Camera Can Pulse Guide: {can_pulse_guide}")

    # Turn on the camera's cooler:
    zwo.turn_on_cooler()

    # Set the cooler's target temperature to -10°C:
    zwo.set_temperature(-10)

    # Wait for 5 seconds:
    sleep(10)

    # Get the current temperature of the CCD of the camera:
    temperature = zwo.get_temperature()

    print(f"Camera Temperature: {temperature}°C")

    # Get the frame from the camera:
    frame = zwo.get_frame()

    print(f"Camera Frame Size: {len(frame)}")

    # Turn off the camera's cooler:
    zwo.turn_off_cooler()


# **************************************************************************************

if __name__ == "__main__":
    main()

# **************************************************************************************
