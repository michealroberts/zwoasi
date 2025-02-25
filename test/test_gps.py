# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest
from datetime import datetime

from zwoasi import (
    ZWOASI_CAMERA_DATE_TIME_CTYPE,
    ZWOASI_GPS_DATA_CTYPE,
    ZWOASIDateTime,
    ZWOASIGPSData,
)

# **************************************************************************************


class TestZWOASI_GPS_DATA_CTYPE(unittest.TestCase):
    def test_field_assignment(self):
        # Create a ctypes structure with sample values:
        c_gps_data = ZWOASI_GPS_DATA_CTYPE()

        c_datetime = ZWOASI_CAMERA_DATE_TIME_CTYPE()
        c_datetime.Year = 2025
        c_datetime.Month = 12
        c_datetime.Day = 31
        c_datetime.Hour = 23
        c_datetime.Minute = 59
        c_datetime.Second = 58
        c_datetime.Msecond = 500
        c_datetime.Usecond = 2500
        c_datetime.Unused = b"GPS Data"
        c_gps_data.Datetime = c_datetime
        c_gps_data.Latitude = 45.1234
        c_gps_data.Longitude = -93.4567
        c_gps_data.Altitude = 5000
        c_gps_data.SatelliteNum = 8
        gps_unused = "GPS Data"
        c_gps_data.Unused = gps_unused.encode("utf-8") + b"\x00" * (
            64 - len(gps_unused)
        )

        self.assertEqual(c_gps_data.Datetime.Year, 2025)
        self.assertEqual(c_gps_data.Datetime.Month, 12)
        self.assertEqual(c_gps_data.Datetime.Day, 31)
        self.assertEqual(c_gps_data.Datetime.Hour, 23)
        self.assertEqual(c_gps_data.Datetime.Minute, 59)
        self.assertEqual(c_gps_data.Datetime.Second, 58)
        self.assertEqual(c_gps_data.Datetime.Msecond, 500)
        self.assertEqual(c_gps_data.Datetime.Usecond, 2500)
        self.assertEqual(
            c_gps_data.Datetime.Unused.decode("utf-8").rstrip("\x00"), "GPS Data"
        )
        self.assertAlmostEqual(c_gps_data.Latitude, 45.1234)
        self.assertAlmostEqual(c_gps_data.Longitude, -93.4567)
        self.assertEqual(c_gps_data.Altitude, 5000)
        self.assertEqual(c_gps_data.SatelliteNum, 8)
        self.assertEqual(c_gps_data.Unused.decode("utf-8").rstrip("\x00"), "GPS Data")


# **************************************************************************************


class TestZWOASIGPSData(unittest.TestCase):
    def test_default_instance(self):
        gps_data = ZWOASIGPSData()

        now = datetime.now()

        self.assertEqual(gps_data.datetime.year, now.year)
        self.assertEqual(gps_data.datetime.month, now.month)
        self.assertEqual(gps_data.datetime.day, now.day)
        self.assertEqual(gps_data.latitude, 0.0)
        self.assertEqual(gps_data.longitude, 0.0)
        self.assertEqual(gps_data.altitude, 0)
        self.assertEqual(gps_data.satellite_number, 0)
        self.assertEqual(gps_data.unused, "")

    def test_full_instance(self):
        gps_data = ZWOASIGPSData(
            datetime=ZWOASIDateTime(
                year=2025,
                month=12,
                day=31,
                hour=23,
                minute=59,
                second=59,
                milliseconds=500,
                microseconds=2500,
                unused="Datetime Unused",
            ),
            latitude=45.123,
            longitude=-93.456,
            altitude=5000,
            satellite_number=8,
            unused="GPS Data Unused",
        )
        self.assertEqual(gps_data.datetime.year, 2025)
        self.assertEqual(gps_data.datetime.month, 12)
        self.assertEqual(gps_data.datetime.day, 31)
        self.assertEqual(gps_data.datetime.hour, 23)
        self.assertEqual(gps_data.datetime.minute, 59)
        self.assertEqual(gps_data.datetime.second, 59)
        self.assertEqual(gps_data.datetime.milliseconds, 500)
        self.assertEqual(gps_data.datetime.microseconds, 2500)
        self.assertEqual(gps_data.datetime.unused, "Datetime Unused")
        self.assertAlmostEqual(gps_data.latitude, 45.123)
        self.assertAlmostEqual(gps_data.longitude, -93.456)
        self.assertEqual(gps_data.altitude, 5000)
        self.assertEqual(gps_data.satellite_number, 8)
        self.assertEqual(gps_data.unused, "GPS Data Unused")

    def test_from_c_types(self):
        # Create and populate a C struct instance with sample values:
        c_datetime = ZWOASI_CAMERA_DATE_TIME_CTYPE()
        c_datetime.Year = 2025
        c_datetime.Month = 12
        c_datetime.Day = 31
        c_datetime.Hour = 23
        c_datetime.Minute = 59
        c_datetime.Second = 58
        c_datetime.Msecond = 500
        c_datetime.Usecond = 2500
        dt_unused = "DatetimeUnused"
        c_datetime.Unused = dt_unused.encode("utf-8") + b"\x00" * (64 - len(dt_unused))

        c_gps_data = ZWOASI_GPS_DATA_CTYPE()
        c_gps_data.Datetime = c_datetime
        c_gps_data.Latitude = 45.1234
        c_gps_data.Longitude = -93.4567
        c_gps_data.Altitude = 5000
        c_gps_data.SatelliteNum = 8
        gps_unused = "GPSUnused"
        c_gps_data.Unused = gps_unused.encode("utf-8") + b"\x00" * (
            64 - len(gps_unused)
        )

        # Convert using from_c_types.
        gps_data = ZWOASIGPSData.from_c_types(c_gps_data)

        # Assert that the fields are correctly converted.
        self.assertEqual(gps_data.datetime.year, 2025)
        self.assertEqual(gps_data.datetime.month, 12)
        self.assertEqual(gps_data.datetime.day, 31)
        self.assertEqual(gps_data.datetime.hour, 23)
        self.assertEqual(gps_data.datetime.minute, 59)
        self.assertEqual(gps_data.datetime.second, 58)
        self.assertEqual(gps_data.datetime.milliseconds, 500)
        self.assertEqual(gps_data.datetime.microseconds, 2500)
        self.assertEqual(gps_data.datetime.unused, dt_unused)

        self.assertAlmostEqual(gps_data.latitude, 45.1234)
        self.assertAlmostEqual(gps_data.longitude, -93.4567)
        self.assertEqual(gps_data.altitude, 5000)
        self.assertEqual(gps_data.satellite_number, 8)
        self.assertEqual(gps_data.unused, gps_unused)


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
