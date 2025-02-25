# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from pydantic import BaseModel, Field

# **************************************************************************************


class ZWOASICameraCapabilities(BaseModel):
    """
    A Pydantic model representation of the C struct _ASI_CONTROL_CAPS.
    """

    name: str = Field(
        default="",
        description="The name of the camera capability (up to 64 chars).",
        max_length=64,
    )

    description: str = Field(
        default="",
        description="Description of the control.",
        max_length=128,
    )

    minimum_value: int = Field(
        default=0,
        description="Minimum allowed value.",
    )

    maximum_value: int = Field(
        default=0,
        description="Maximum allowed value.",
    )

    default_value: int = Field(
        default=0,
        description="Default value of the control.",
    )

    is_auto_supported: bool = Field(
        default=False,
        description="Whether auto mode is supported.",
    )

    is_writable: bool = Field(
        default=False,
        description="Whether the control is writable.",
    )

    control_type: int = Field(
        default=0,
        description="Control type identifier.",
    )

    unused: str = Field(
        default="",
        description="Unused field (16 bytes in C).",
    )


# **************************************************************************************
