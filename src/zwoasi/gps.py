# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from pydantic import BaseModel, Field

from .time import ZWOASIDateTime

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


# **************************************************************************************
