# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from ctypes import Structure as c_Structure
from ctypes import c_int
from typing import List

from pydantic import BaseModel, Field, field_validator

# **************************************************************************************


class ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE(c_Structure):
    _fields_ = [
        ("SupportedCameraMode", c_int * 16),
    ]


# **************************************************************************************


class ZWOASICameraSupportedMode(BaseModel):
    """
    A Pydantic model representation of the C struct _ASI_SUPPORTED_MODE.
    """

    supported_mode: List[int] = Field(
        default_factory=list,
        description="List of supported camera modes (up to 16 integers).",
    )

    @field_validator("supported_mode")
    def validate_length(cls, v: List[int]) -> List[int]:
        if len(v) <= 16:
            return v

        raise ValueError("supported_mode must contain at most 16 items")

    @classmethod
    def from_c_types(
        cls, c_mode: "ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE"
    ) -> "ZWOASICameraSupportedMode":
        # Process SupportedCameraMode: stop when a 0 is encountered:
        modes: List[int] = []
        for i in range(16):
            value = c_mode.SupportedCameraMode[i]
            if value == 0:
                break
            modes.append(value)
        return cls(supported_mode=modes)


# **************************************************************************************
