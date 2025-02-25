# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from .capabilities import ZWOASI_CAMERA_CAPABILITIES_CTYPE, ZWOASICameraCapabilities
from .enums import (
    ZWOASIBayerPattern,
    ZWOASIBool,
    ZWOASICameraMode,
    ZWOASIControlType,
    ZWOASIErrorCode,
    ZWOASIExposureStatus,
    ZWOASIFlipStatus,
    ZWOASIGuideDirection,
    ZWOASIImageType,
)
from .errors import ZWOASIError, ZWOASIIOError
from .info import ZWOASI_CAMERA_INFORMATION_CTYPE, ZWOASICameraInformation
from .time import ZWOASI_CAMERA_DATE_TIME_CTYPE, ZWOASIDateTime

# **************************************************************************************

__version__ = "0.0.0"

# **************************************************************************************

__license__ = "MIT"


# **************************************************************************************

__all__: list[str] = [
    "ZWOASI_CAMERA_CAPABILITIES_CTYPE",
    "ZWOASI_CAMERA_DATE_TIME_CTYPE",
    "ZWOASI_CAMERA_INFORMATION_CTYPE",
    "ZWOASIBayerPattern",
    "ZWOASIBool",
    "ZWOASICameraCapabilities",
    "ZWOASICameraMode",
    "ZWOASICameraInformation",
    "ZWOASIControlType",
    "ZWOASIDateTime",
    "ZWOASIError",
    "ZWOASIErrorCode",
    "ZWOASIExposureStatus",
    "ZWOASIFlipStatus",
    "ZWOASIGuideDirection",
    "ZWOASIIOError",
    "ZWOASIImageType",
]

# **************************************************************************************
