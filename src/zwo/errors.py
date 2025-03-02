# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from typing import Optional

from .enums import ZWOASIErrorCode, ZWOASIExposureStatus

# **************************************************************************************


class ZWOASIError(Exception):
    """
    Exception class for errors returned from the :mod:`zwoasi` module.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


# **************************************************************************************


class ZWOASIIOError(ZWOASIError):
    """
    Exception class for all errors returned from the ASI SDK library.

    :param message: A descriptive error message.
    :param error_code: An optional integer error code returned by the SDK.
    """

    def __init__(
        self, message: str, error_code: Optional[ZWOASIErrorCode] = None
    ) -> None:
        super().__init__(message)
        self.error_code = int(error_code) if error_code is not None else None


# **************************************************************************************


class ZWOASIExposureError(ZWOASIError):
    """
    Exception class for errors returned when attempting to get the exposure frame
    from the :mod:`zwoasi` module.
    """

    def __init__(
        self, message: str, status_code: Optional[ZWOASIExposureStatus] = None
    ) -> None:
        super().__init__(message)
        self.status_code = int(status_code) if status_code is not None else None


# **************************************************************************************

errors = [
    None,
    ZWOASIIOError("Invalid index", ZWOASIErrorCode.INVALID_INDEX),
    ZWOASIIOError("Invalid ID", ZWOASIErrorCode.INVALID_ID),
    ZWOASIIOError("Invalid control type", ZWOASIErrorCode.INVALID_CONTROL_TYPE),
    ZWOASIIOError("Camera closed", ZWOASIErrorCode.CAMERA_CLOSED),
    ZWOASIIOError("Camera removed", ZWOASIErrorCode.CAMERA_REMOVED),
    ZWOASIIOError("Invalid path", ZWOASIErrorCode.INVALID_PATH),
    ZWOASIIOError("Invalid file format", ZWOASIErrorCode.INVALID_FILEFORMAT),
    ZWOASIIOError("Invalid size", ZWOASIErrorCode.INVALID_VIDEO_SIZE),
    ZWOASIIOError("Invalid image type", ZWOASIErrorCode.INVALID_IMAGE_TYPE),
    ZWOASIIOError(
        "Outside of boundary", ZWOASIErrorCode.START_POSITION_OUT_OF_BOUNDARY
    ),
    ZWOASIIOError("Timeout", ZWOASIErrorCode.TIMEOUT),
    ZWOASIIOError("Invalid sequence", ZWOASIErrorCode.INVALID_SEQUENCE),
    ZWOASIIOError("Buffer too small", ZWOASIErrorCode.BUFFER_TOO_SMALL),
    ZWOASIIOError("Video mode active", ZWOASIErrorCode.VIDEO_MODE_ACTIVE),
    ZWOASIIOError("Exposure in progress", ZWOASIErrorCode.EXPOSURE_IN_PROGRESS),
    ZWOASIIOError("General error", ZWOASIErrorCode.GENERAL_ERROR),
    ZWOASIIOError("Invalid mode", ZWOASIErrorCode.INVALID_MODE),
    ZWOASIIOError("GPS not supported", ZWOASIErrorCode.GPS_NOT_SUPPORTED),
    ZWOASIIOError("Invalid GPS version", ZWOASIErrorCode.INVALID_GPS_VERSION),
    ZWOASIIOError("Invalid GPS FPGA", ZWOASIErrorCode.INVALID_GPS_FPGA),
    ZWOASIIOError(
        "Invalid GPS parameter out of range",
        ZWOASIErrorCode.INVALID_GPS_PARAM_OUT_OF_RANGE,
    ),
    ZWOASIIOError("Invalid GPS data", ZWOASIErrorCode.INVALID_GPS_DATA),
]

# **************************************************************************************
