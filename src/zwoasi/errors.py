# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************


class ZWOASIError(Exception):
    """
    Exception class for errors returned from the :mod:`zwoasi` module.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


# **************************************************************************************
