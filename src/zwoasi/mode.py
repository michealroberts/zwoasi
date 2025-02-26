# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from typing import List

from pydantic import BaseModel, Field, field_validator

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


# **************************************************************************************
