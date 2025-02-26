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
from .errors import ZWOASIError, ZWOASIExposureError, ZWOASIIOError
from .gps import ZWOASI_GPS_DATA_CTYPE, ZWOASIGPSData
from .info import ZWOASI_CAMERA_INFORMATION_CTYPE, ZWOASICameraInformation
from .mode import ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE, ZWOASICameraSupportedMode
from .time import ZWOASI_CAMERA_DATE_TIME_CTYPE, ZWOASIDateTime
from .utils import get_asi_libary_path

# **************************************************************************************

__version__ = "0.0.0"

# **************************************************************************************

__license__ = "MIT"

# **************************************************************************************

ZWOASI_SDK_VERSION: str = "1.37"

# **************************************************************************************

__all__: list[str] = [
    "__version__",
    "__license__",
    "get_asi_libary_path",
    "ZWOASI_SDK_VERSION",
    "ZWOASI_CAMERA_CAPABILITIES_CTYPE",
    "ZWOASI_CAMERA_DATE_TIME_CTYPE",
    "ZWOASI_CAMERA_INFORMATION_CTYPE",
    "ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE",
    "ZWOASI_GPS_DATA_CTYPE",
    "ZWOASIBayerPattern",
    "ZWOASIBool",
    "ZWOASICameraCapabilities",
    "ZWOASICameraMode",
    "ZWOASICameraInformation",
    "ZWOASICameraSupportedMode",
    "ZWOASIControlType",
    "ZWOASIDateTime",
    "ZWOASIError",
    "ZWOASIErrorCode",
    "ZWOASIExposureError",
    "ZWOASIExposureStatus",
    "ZWOASIFlipStatus",
    "ZWOASIGPSData",
    "ZWOASIGuideDirection",
    "ZWOASIIOError",
    "ZWOASIImageType",
]

# **************************************************************************************
