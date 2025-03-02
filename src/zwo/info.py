# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from ctypes import Structure as c_Structure
from ctypes import c_char, c_double, c_float, c_int, c_long
from typing import List, Optional, cast

from pydantic import BaseModel, Field

from .enums import ZWOASIBayerPattern, ZWOASIImageType

# **************************************************************************************


class ZWOASI_CAMERA_INFORMATION_CTYPE(c_Structure):
    _fields_ = [
        ("Name", c_char * 64),
        ("CameraID", c_int),
        ("MaxHeight", c_long),
        ("MaxWidth", c_long),
        ("IsColorCam", c_int),
        ("BayerPattern", c_int),
        ("SupportedBins", c_int * 16),
        ("SupportedVideoFormat", c_int * 8),
        ("PixelSize", c_double),
        ("MechanicalShutter", c_int),
        ("ST4Port", c_int),
        ("IsCoolerCam", c_int),
        ("IsUSB3Host", c_int),
        ("IsUSB3Camera", c_int),
        ("ElecPerADU", c_float),
        ("BitDepth", c_int),
        ("IsTriggerCam", c_int),
        ("Unused", c_char * 16),
    ]


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

    supported_image_formats: List[ZWOASIImageType] = Field(
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

    @classmethod
    def from_c_types(
        cls, c_info: "ZWOASI_CAMERA_INFORMATION_CTYPE"
    ) -> "ZWOASICameraInformation":
        """
        Convert a ctypes ASI_CAMERA_INFO structure to a ZWOASICameraInformation instance.
        """
        name = c_info.Name.decode("utf-8").rstrip("\x00")

        # Convert BayerPattern if non-zero to ZWOASIBayerPattern enum:
        bayer_pattern = (
            ZWOASIBayerPattern(c_info.BayerPattern)
            if c_info.BayerPattern != 0
            else None
        )

        # Process SupportedBins: stop when a 0 is encountered:
        supported_binnings: List[int] = []
        for i in range(16):
            value = c_info.SupportedBins[i]
            if value == 0:
                break
            supported_binnings.append(value)

        # Process SupportedVideoFormat: stop when ZWOASIImageType.ND is encountered:
        supported_image_formats: List[ZWOASIImageType] = []
        for i in range(8):
            value = c_info.SupportedVideoFormat[i]
            if value == ZWOASIImageType.END.value:
                break
            supported_image_formats.append(ZWOASIImageType(value))

        return cls(
            id=cast(int, c_info.CameraID),
            name=name,
            maximum_height=cast(int, c_info.MaxHeight),
            maximum_width=cast(int, c_info.MaxWidth),
            pixel_size=cast(float, c_info.PixelSize),
            electrons_per_adu=cast(float, c_info.ElecPerADU),
            bit_depth=cast(int, c_info.BitDepth),
            bayer_pattern=bayer_pattern,
            supported_binnings=supported_binnings,
            supported_image_formats=supported_image_formats,
            is_color=bool(c_info.IsColorCam),
            is_monochrome=not bool(c_info.IsColorCam),
            is_usb3=bool(c_info.IsUSB3Camera),
            is_usb3_host=bool(c_info.IsUSB3Host),
            has_st4_port=bool(c_info.ST4Port),
            has_external_trigger=bool(c_info.IsTriggerCam),
            has_mechanical_shutter=bool(c_info.MechanicalShutter),
            has_cooler=bool(c_info.IsCoolerCam),
            unused=c_info.Unused.decode("utf-8").rstrip("\x00"),
        )


# **************************************************************************************
