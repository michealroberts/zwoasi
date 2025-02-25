# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest
from datetime import datetime

from zwoasi import ZWOASIDateTime, ZWOASIGPSData

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


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
