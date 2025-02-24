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
