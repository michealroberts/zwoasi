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
