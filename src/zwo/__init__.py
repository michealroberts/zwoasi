# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from .camera import (
    ZWOASI_VENDOR_ID,
    BaseDeviceState,
    ZWOASICamera,
    ZWOASICameraParams,
    ZWOASIGPSExposureData,
    get_all_connected_camera_ids,
    is_connected,
)
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
    ZWOASITriggerOutput,
)
from .errors import ZWOASIError, ZWOASIExposureError, ZWOASIIOError
from .gps import ZWOASI_GPS_DATA_CTYPE, ZWOASIGPSData
from .info import ZWOASI_CAMERA_INFORMATION_CTYPE, ZWOASICameraInformation
from .mode import ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE, ZWOASICameraSupportedMode
from .time import ZWOASI_CAMERA_DATE_TIME_CTYPE, ZWOASIDateTime
from .utils import get_asi_libary_path
from .version import ZWOASI_SDK_VERSION

# **************************************************************************************

__version__ = "0.5.0"

# **************************************************************************************

__license__ = "MIT"

# **************************************************************************************

__all__: list[str] = [
    "__version__",
    "__license__",
    "get_all_connected_camera_ids",
    "get_asi_libary_path",
    "is_connected",
    "BaseDeviceState",
    "ZWOASI_SDK_VERSION",
    "ZWOASI_CAMERA_CAPABILITIES_CTYPE",
    "ZWOASI_CAMERA_DATE_TIME_CTYPE",
    "ZWOASI_CAMERA_INFORMATION_CTYPE",
    "ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE",
    "ZWOASI_GPS_DATA_CTYPE",
    "ZWOASI_VENDOR_ID",
    "ZWOASIBayerPattern",
    "ZWOASIBool",
    "ZWOASICamera",
    "ZWOASICameraParams",
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
    "ZWOASIGPSExposureData",
    "ZWOASIGuideDirection",
    "ZWOASIIOError",
    "ZWOASIImageType",
    "ZWOASITriggerOutput",
]

# **************************************************************************************
