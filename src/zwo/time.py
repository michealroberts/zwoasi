# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from ctypes import Structure as c_Structure
from ctypes import c_char, c_int
from datetime import datetime
from typing import cast

from pydantic import BaseModel, Field

# **************************************************************************************


class ZWOASI_CAMERA_DATE_TIME_CTYPE(c_Structure):
    _fields_ = [
        ("Year", c_int),
        ("Month", c_int),
        ("Day", c_int),
        ("Hour", c_int),
        ("Minute", c_int),
        ("Second", c_int),
        ("Msecond", c_int),
        ("Usecond", c_int),  # Minimum unit: 0.1us
        ("Unused", c_char * 64),
    ]


# **************************************************************************************


class ZWOASIDateTime(BaseModel):
    """
    A Pydantic model representation of the C struct ASI_DATE_TIME.
    """

    year: int = Field(
        default_factory=lambda: datetime.now().year,
        description="Year (e.g., 2025)",
        ge=1900,
        le=3000,
    )

    month: int = Field(
        default_factory=lambda: datetime.now().month,
        description="Month (1-12).",
        ge=1,
        le=12,
    )

    day: int = Field(
        default_factory=lambda: datetime.now().day,
        description="Day of the month (1-31).",
        ge=1,
        le=31,
    )

    hour: int = Field(
        default=0,
        description="Hour (0-23).",
        ge=0,
        le=23,
    )

    minute: int = Field(
        default=0,
        description="Minute (0-59).",
        ge=0,
        le=59,
    )

    second: int = Field(
        default=0,
        description="Second (0-59).",
        ge=0,
        le=59,
    )

    milliseconds: int = Field(
        default=0,
        description="Milliseconds (0-999).",
        ge=0,
        le=999,
    )

    microseconds: int = Field(
        default=0,
        description="Microseconds in 0.1µs units (0-9999).",
        ge=0,
        le=9999,
    )

    unused: str = Field(
        default="",
        description="Unused field for concatenated strings (up to 64 characters).",
        max_length=64,
    )

    @classmethod
    def from_c_types(
        cls, c_datetime: ZWOASI_CAMERA_DATE_TIME_CTYPE
    ) -> "ZWOASIDateTime":
        """
        Convert a ctypes ASI_DATE_TIME structure to a ZWOASIDateTime instance.
        """
        return cls(
            year=cast(int, c_datetime.Year),
            month=cast(int, c_datetime.Month),
            day=cast(int, c_datetime.Day),
            hour=cast(int, c_datetime.Hour),
            minute=cast(int, c_datetime.Minute),
            second=cast(int, c_datetime.Second),
            milliseconds=cast(int, c_datetime.Msecond),
            microseconds=cast(int, c_datetime.Usecond),
            unused=c_datetime.Unused.decode("utf-8").rstrip("\x00"),
        )


# **************************************************************************************
