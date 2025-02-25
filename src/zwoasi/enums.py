# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from enum import IntEnum

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


class ZWOASIFlipStatus(IntEnum):
    """
    Enumeration corresponding to the C enumeration ASI_FLIP_STATUS:

    ASI_FLIP_NONE   = 0  (original)
    ASI_FLIP_HORIZ  = 1  (horizontal flip)
    ASI_FLIP_VERT   = 2  (vertical flip)
    ASI_FLIP_BOTH   = 3  (both horizontal and vertical flip)
    """

    NONE = 0
    HORIZ = 1
    VERT = 2
    BOTH = 3


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
