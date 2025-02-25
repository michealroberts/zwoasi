# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from typing import List, Optional

from pydantic import BaseModel, Field

from .enums import ZWOASIBayerPattern, ZWOASIImageType

# **************************************************************************************


class ZWOASICameraInformation(BaseModel):
    """
    A Pydantic model representation of the C struct ASI_CAMERA_INFO.
    """

    id: int = Field(
        default=0,
        description="Camera ID (starts from 0).",
    )

    name: str = Field(
        default="ZWO ASI Camera",
        description="The name of the camera (up to 64 chars).",
        max_length=64,
    )

    maximum_height: int = Field(
        default=0,
        description="Maximum height of the camera sensor.",
    )

    maximum_width: int = Field(
        default=0,
        description="Maximum width of the camera sensor.",
    )

    pixel_size: float = Field(
        default=0.0,
        description="Pixel size of the camera sensor in microns (µm).",
    )

    electrons_per_adu: float = Field(
        default=0.0,
        description="Electrons per ADU (Analog-to-Digital Unit).",
    )

    bit_depth: int = Field(
        default=1,
        description="Bit depth of the camera (e.g., 16 for 16-bit ADC).",
    )

    bayer_pattern: Optional[ZWOASIBayerPattern] = Field(
        default=None,
        description="The Bayer pattern used by the camera (if color).",
    )

    supported_binnings: List[int] = Field(
        default=[1, 2],
        description=(
            "List of supported binning factors. "
            "Ends with 0 in C (sentinel), but stored as a plain list here."
        ),
    )

    supported_video_format: List[ZWOASIImageType] = Field(
        default_factory=list,
        description=(
            "Supported video/image formats. "
            "Ends with IMG_END in C, but stored as a plain list here."
        ),
    )

    is_color: bool = Field(
        default=False,
        description="Whether the camera is a color camera.",
    )

    is_monochrome: bool = Field(
        default=True,
        description="Whether the camera is a monochromatic camera.",
    )

    is_usb3: bool = Field(
        default=False,
        description="Whether the camera is a USB 3.0 camera.",
    )

    is_usb3_host: bool = Field(
        default=False,
        description="Whether the host is USB 3.0 capable.",
    )

    has_st4_port: bool = Field(
        default=False,
        description="Whether the camera has an ST4 guide port.",
    )

    has_external_trigger: bool = Field(
        default=False,
        description="Whether the camera supports external triggering.",
    )

    has_mechanical_shutter: bool = Field(
        default=False,
        description="Whether the camera has a mechanical shutter.",
    )

    has_cooler: bool = Field(
        default=False,
        description="Whether the camera has a cooling feature.",
    )

    unused: str = Field(
        default="",
        description="Unused field (16 bytes in C).",
    )


# **************************************************************************************
