# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from ctypes import Structure as c_Structure
from ctypes import c_char, c_double, c_int
from typing import cast

from pydantic import BaseModel, Field

from .time import ZWOASI_CAMERA_DATE_TIME_CTYPE, ZWOASIDateTime

# **************************************************************************************


class ZWOASI_GPS_DATA_CTYPE(c_Structure):
    _fields_ = [
        ("Datetime", ZWOASI_CAMERA_DATE_TIME_CTYPE),
        ("Latitude", c_double),
        ("Longitude", c_double),
        ("Altitude", c_int),
        ("SatelliteNum", c_int),
        ("Unused", c_char * 64),
    ]


# **************************************************************************************


class ZWOASIGPSData(BaseModel):
    """
    A Pydantic model representation of the C struct ASI_GPS_DATA.
    """

    datetime: ZWOASIDateTime = Field(
        default_factory=ZWOASIDateTime,
        description="Date and time of the GPS reading.",
    )

    latitude: float = Field(
        default=0.0,
        description="Latitude (+: North, -: South).",
    )

    longitude: float = Field(
        default=0.0,
        description="Longitude (+: East, -: West).",
    )

    altitude: int = Field(
        default=0,
        description="Altitude in 0.1 m units, maximum 99999",
        ge=0,
        le=99999,
    )

    satellite_number: int = Field(
        default=0,
        description="Number of satellites, maximum 99",
        ge=0,
        le=99,
    )

    unused: str = Field(
        default="",
        description="Unused field (up to 64 characters).",
        max_length=64,
    )

    @classmethod
    def from_c_types(cls, c_gps_data: "ZWOASI_GPS_DATA_CTYPE") -> "ZWOASIGPSData":
        """
        Convert a ctypes ASI_GPS_DATA structure to a ZWOASIGPSData instance.
        """
        return cls(
            datetime=ZWOASIDateTime.from_c_types(c_gps_data.Datetime),
            latitude=cast(float, c_gps_data.Latitude),
            longitude=cast(float, c_gps_data.Longitude),
            altitude=cast(int, c_gps_data.Altitude),
            satellite_number=cast(int, c_gps_data.SatelliteNum),
            unused=c_gps_data.Unused.decode("utf-8").rstrip("\x00"),
        )


# **************************************************************************************
