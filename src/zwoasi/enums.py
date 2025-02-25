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
