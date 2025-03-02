# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from ctypes import Structure as c_Structure
from ctypes import c_char, c_int, c_long

from pydantic import BaseModel, Field

# **************************************************************************************


class ZWOASI_CAMERA_CAPABILITIES_CTYPE(c_Structure):
    _fields_ = [
        ("Name", c_char * 64),
        ("Description", c_char * 128),
        ("MaxValue", c_long),
        ("MinValue", c_long),
        ("DefaultValue", c_long),
        ("IsAutoSupported", c_int),
        ("IsWritable", c_int),
        ("ControlType", c_int),
        ("Unused", c_char * 32),
    ]


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

    @classmethod
    def from_c_types(
        cls, c_capabilities: ZWOASI_CAMERA_CAPABILITIES_CTYPE
    ) -> "ZWOASICameraCapabilities":
        """
        Convert a ctypes ZWOASI_CAMERA_CAPABILITIES_CTYPE structure to a ZWOASICameraCapabilities instance.
        """
        name = c_capabilities.Name.decode("utf-8").rstrip("\x00")

        description = c_capabilities.Description.decode("utf-8").rstrip("\x00")

        return cls(
            name=name,
            description=description,
            maximum_value=c_capabilities.MaxValue,
            minimum_value=c_capabilities.MinValue,
            default_value=c_capabilities.DefaultValue,
            is_auto_supported=bool(c_capabilities.IsAutoSupported),
            is_writable=bool(c_capabilities.IsWritable),
            control_type=c_capabilities.ControlType,
            unused=c_capabilities.Unused.decode("utf-8").rstrip("\x00"),
        )


# **************************************************************************************
