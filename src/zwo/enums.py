# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from enum import IntEnum

# **************************************************************************************


class ZWOASIBool(IntEnum):
    """
    Enumeration corresponding to the C enumeration ASI_BOOL:

    ASI_FALSE = 0
    ASI_TRUE  = 1
    """

    FALSE = 0
    TRUE = 1


# **************************************************************************************


class ZWOASIBayerPattern(IntEnum):
    """
    Enumeration corresponding to the C enumeration ASI_BAYER_PATTERN:

    ASI_BAYER_RG = 0
    ASI_BAYER_BG = 1
    ASI_BAYER_GR = 2
    ASI_BAYER_GB = 3
    """

    RG = 0
    BG = 1
    GR = 2
    GB = 3


# **************************************************************************************


class ZWOASICameraMode(IntEnum):
    """
    Enumeration corresponding to the C enumeration ASI_CAMERA_MODE:

    ASI_MODE_NORMAL       =  0
    ASI_MODE_TRIG_SOFT_EDGE  =  1
    ASI_MODE_TRIG_RISE_EDGE  =  2
    ASI_MODE_TRIG_FALL_EDGE  =  3
    ASI_MODE_TRIG_SOFT_LEVEL =  4
    ASI_MODE_TRIG_HIGH_LEVEL =  5
    ASI_MODE_TRIG_LOW_LEVEL  =  6
    ASI_MODE_END         = -1
    """

    NORMAL = 0
    TRIGGER_SOFT_EDGE = 1
    TRIGGER_RISE_EDGE = 2
    TRIGGER_FALL_EDGE = 3
    TRIGGER_SOFT_LEVEL = 4
    TRIGGER_HIGH_LEVEL = 5
    TRIGGER_LOW_LEVEL = 6
    END = -1


# **************************************************************************************


class ZWOASIControlType(IntEnum):
    """
    Enumeration corresponding to the C enumeration ASI_CONTROL_TYPE.

    ASI_GAIN                    = 0   // Gain control
    ASI_EXPOSURE                = 1   // Exposure control
    ASI_GAMMA                   = 2   // Gamma control
    ASI_WB_R                    = 3   // White balance (red channel)
    ASI_WB_B                    = 4   // White balance (blue channel)
    ASI_OFFSET                  = 5   // Offset control
    ASI_BANDWIDTHOVERLOAD       = 6   // Bandwidth overload control
    ASI_OVERCLOCK               = 7   // Overclock setting
    ASI_TEMPERATURE             = 8   // return 10*temperature
    ASI_FLIP                    = 9   // Flip control
    ASI_AUTO_MAX_GAIN           = 10  // Automatic maximum gain
    ASI_AUTO_MAX_EXP            = 11  // Automatic maximum exposure (microsecond)
    ASI_AUTO_TARGET_BRIGHTNESS  = 12  // Automatic target brightness
    ASI_HARDWARE_BIN            = 13  // Hardware binning control
    ASI_HIGH_SPEED_MODE         = 14  // High speed mode control
    ASI_COOLER_POWER_PERC       = 15  // Cooler power percentage control
    ASI_TARGET_TEMP             = 16  // Target temperature (not multiplied by 10)
    ASI_COOLER_ON               = 17  // Cooler on/off control
    ASI_MONO_BIN                = 18  // Monochrome binning (reduces grid artifacts in color cameras)
    ASI_FAN_ON                  = 19  // Fan on/off control
    ASI_PATTERN_ADJUST          = 20  // Pattern adjustment control
    ASI_ANTI_DEW_HEATER         = 21  // Anti-dew heater control
    ASI_FAN_ADJUST              = 22  // Fan speed adjustment control
    ASI_PWRLED_BRIGNT           = 23  // Power LED brightness control
    ASI_USBHUB_RESET            = 24  // USB hub reset control
    ASI_GPS_SUPPORT             = 25  // GPS support indicator
    ASI_GPS_START_LINE          = 26  // GPS start line position
    ASI_GPS_END_LINE            = 27  // GPS end line position
    ASI_ROLLING_INTERVAL        = 28  // Rolling shutter interval (microsecond)
    """

    GAIN = 0
    EXPOSURE = 1
    GAMMA = 2
    WHITE_BALANCE_RED_CHANNEL = 3
    WHITE_BALANCE_BLUE_CHANNEL = 4
    OFFSET = 5
    BANDWIDTH_OVERLOAD = 6
    OVERCLOCK = 7
    TEMPERATURE_READING = 8
    IMAGE_FLIP = 9
    AUTO_MAXIMUM_GAIN = 10
    AUTO_MAXIMUM_EXPOSURE = 11
    AUTO_TARGET_BRIGHTNESS = 12
    HARDWARE_BINNING = 13
    HIGH_SPEED_MODE = 14
    COOLER_POWER_PERCENTAGE = 15
    TARGET_TEMPERATURE = 16
    COOLER_ON_OFF = 17
    MONOCHROME_BINNING = 18
    FAN_ON_OFF = 19
    PATTERN_ADJUSTMENT = 20
    ANTI_DEW_HEATER = 21
    FAN_SPEED_ADJUSTMENT = 22
    POWER_LED_BRIGHTNESS = 23
    USB_HUB_RESET = 24
    GPS_SUPPORT_INDICATOR = 25
    GPS_START_LINE_POSITION = 26
    GPS_END_LINE_POSITION = 27
    ROLLING_SHUTTER_INTERVAL = 28
    BRIGHTNESS = OFFSET
    AUTO_MAX_BRIGHTNESS = AUTO_TARGET_BRIGHTNESS


# **************************************************************************************


class ZWOASIErrorCode(IntEnum):
    """
    Enumeration corresponding to the C enumeration ASI_ERROR_CODE.

    ASI_SUCCESS = 0
    ASI_ERROR_INVALID_INDEX       = 1   // no camera connected or index value out of boundary
    ASI_ERROR_INVALID_ID          = 2   // invalid ID
    ASI_ERROR_INVALID_CONTROL_TYPE= 3   // invalid control type
    ASI_ERROR_CAMERA_CLOSED       = 4   // camera didn't open
    ASI_ERROR_CAMERA_REMOVED      = 5   // failed to find the camera (maybe removed)
    ASI_ERROR_INVALID_PATH        = 6   // cannot find the file path
    ASI_ERROR_INVALID_FILEFORMAT  = 7
    ASI_ERROR_INVALID_SIZE        = 8   // wrong video format size
    ASI_ERROR_INVALID_IMGTYPE     = 9   // unsupported image format
    ASI_ERROR_OUTOF_BOUNDARY      = 10  // start position is out of boundary
    ASI_ERROR_TIMEOUT             = 11  // timeout
    ASI_ERROR_INVALID_SEQUENCE    = 12  // need to stop capture first
    ASI_ERROR_BUFFER_TOO_SMALL    = 13  // buffer is not big enough
    ASI_ERROR_VIDEO_MODE_ACTIVE   = 14
    ASI_ERROR_EXPOSURE_IN_PROGRESS= 15
    ASI_ERROR_GENERAL_ERROR       = 16  // general error, e.g., value out of valid range
    ASI_ERROR_INVALID_MODE        = 17
    ASI_ERROR_GPS_NOT_SUPPORTED   = 18
    ASI_ERROR_GPS_VER_ERR         = 19
    ASI_ERROR_GPS_FPGA_ERR        = 20
    ASI_ERROR_GPS_PARAM_OUT_OF_RANGE = 21
    ASI_ERROR_GPS_DATA_INVALID    = 22
    ASI_ERROR_END                 = 23
    """

    SUCCESS = 0
    INVALID_INDEX = 1
    INVALID_ID = 2
    INVALID_CONTROL_TYPE = 3
    CAMERA_CLOSED = 4
    CAMERA_REMOVED = 5
    INVALID_PATH = 6
    INVALID_FILEFORMAT = 7
    INVALID_VIDEO_SIZE = 8
    INVALID_IMAGE_TYPE = 9
    START_POSITION_OUT_OF_BOUNDARY = 10
    TIMEOUT = 11
    INVALID_SEQUENCE = 12
    BUFFER_TOO_SMALL = 13
    VIDEO_MODE_ACTIVE = 14
    EXPOSURE_IN_PROGRESS = 15
    GENERAL_ERROR = 16
    INVALID_MODE = 17
    GPS_NOT_SUPPORTED = 18
    INVALID_GPS_VERSION = 19
    INVALID_GPS_FPGA = 20
    INVALID_GPS_PARAM_OUT_OF_RANGE = 21
    INVALID_GPS_DATA = 22
    END = 23


# **************************************************************************************


class ZWOASIExposureStatus(IntEnum):
    """
    Enumeration corresponding to the C enumeration ASI_EXPOSURE_STATUS.

    ASI_EXP_IDLE      = 0   // idle state, you can start exposure now
    ASI_EXP_WORKING   = 1   // exposing
    ASI_EXP_SUCCESS   = 2   // exposure finished and waiting for download
    ASI_EXP_FAILED    = 3   // exposure failed, you need to start exposure again
    """

    IDLE = 0
    WORKING = 1
    SUCCESS = 2
    FAILED = 3


# **************************************************************************************


class ZWOASIFlipStatus(IntEnum):
    """
    Enumeration corresponding to the C enumeration ASI_FLIP_STATUS:

    ASI_FLIP_NONE   = 0  (original)
    ASI_FLIP_HORIZ  = 1  (horizontal flip)
    ASI_FLIP_VERT   = 2  (vertical flip)
    ASI_FLIP_BOTH   = 3  (both horizontal and vertical flip)
    """

    NONE = 0
    HORIZONTAL = 1
    VERTICAL = 2
    BOTH = 3


# **************************************************************************************


class ZWOASIGuideDirection(IntEnum):
    """
    Enumeration corresponding to the C enumeration ASI_GUIDE_DIRECTION:

    ASI_GUIDE_NORTH = 0
    ASI_GUIDE_SOUTH = 1
    ASI_GUIDE_EAST  = 2
    ASI_GUIDE_WEST  = 3
    """

    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3


# **************************************************************************************


class ZWOASIImageType(IntEnum):
    """
    Enumeration corresponding to the C enumeration ASI_IMG_TYPE:

    ASI_IMG_RAW8 = 0
    ASI_IMG_RGB24 = 1
    ASI_IMG_RAW16 = 2
    ASI_IMG_Y8 = 3
    ASI_IMG_END = -1
    """

    RAW8 = 0
    RGB24 = 1
    RAW16 = 2
    Y8 = 3
    END = -1


# **************************************************************************************


class ZWOASITriggerOutput(IntEnum):
    """
    Enumeration corresponding to the C enumeration ASI_TRIGGER_OUTPUT:

    ASI_TRIG_OUTPUT_PINA = 0 Only Pin A output
    ASI_TRIG_OUTPUT_PINB = 1 Only Pin B output
    ASI_TRIG_OUTPUT_NONE = -1
    """

    PINA = 0
    PINB = 1
    NONE = -1


# **************************************************************************************
