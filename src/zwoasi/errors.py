# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from typing import Optional

from .enums import ZWOASIErrorCode

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
