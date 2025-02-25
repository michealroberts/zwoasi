# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest
from datetime import datetime

from pydantic import ValidationError

from zwoasi import ZWOASI_CAMERA_DATE_TIME_CTYPE, ZWOASIDateTime

# **************************************************************************************


class TestZWOASI_CAMERA_DATE_TIME_CTYPE(unittest.TestCase):
    def test_field_assignment(self):
        # Create a ctypes structure with sample values:
        c_datetime = ZWOASI_CAMERA_DATE_TIME_CTYPE()
        c_datetime.Year = 2025
        c_datetime.Month = 12
        c_datetime.Day = 31
        c_datetime.Hour = 23
        c_datetime.Minute = 59
        c_datetime.Second = 58
        c_datetime.Msecond = 500
        c_datetime.Usecond = 1234
        c_datetime.Unused = b"GPS Data"

        self.assertEqual(c_datetime.Year, 2025)
        self.assertEqual(c_datetime.Month, 12)
        self.assertEqual(c_datetime.Day, 31)
        self.assertEqual(c_datetime.Hour, 23)
        self.assertEqual(c_datetime.Minute, 59)
        self.assertEqual(c_datetime.Second, 58)
        self.assertEqual(c_datetime.Msecond, 500)
        self.assertEqual(c_datetime.Usecond, 1234)
        self.assertEqual(c_datetime.Unused.decode("utf-8").rstrip("\x00"), "GPS Data")


# **************************************************************************************


class TestZWOASIDateTime(unittest.TestCase):
    def test_default_instance(self):
        dt = ZWOASIDateTime()

        now = datetime.now()

        # Instead of asserting exact equality (which might vary if run across midnight),
        # we check that the default year, month, and day are within a reasonable range.
        self.assertGreaterEqual(dt.year, 1900)
        self.assertLessEqual(dt.year, 2100)
        self.assertEqual(dt.year, now.year)

        self.assertGreaterEqual(dt.month, 1)
        self.assertLessEqual(dt.month, 12)
        self.assertEqual(dt.month, now.month)

        self.assertGreaterEqual(dt.day, 1)
        self.assertLessEqual(dt.day, 31)
        self.assertEqual(dt.day, now.day)

        self.assertEqual(dt.hour, 0)
        self.assertEqual(dt.minute, 0)
        self.assertEqual(dt.second, 0)
        self.assertEqual(dt.milliseconds, 0)
        self.assertEqual(dt.microseconds, 0)
        self.assertEqual(dt.unused, "")

    def test_valid_instance(self):
        dt = ZWOASIDateTime(
            year=2025,
            month=12,
            day=31,
            hour=23,
            minute=59,
            second=59,
            milliseconds=999,
            microseconds=5000,
            unused="GPS Data",
        )
        self.assertEqual(dt.year, 2025)
        self.assertEqual(dt.month, 12)
        self.assertEqual(dt.day, 31)
        self.assertEqual(dt.hour, 23)
        self.assertEqual(dt.minute, 59)
        self.assertEqual(dt.second, 59)
        self.assertEqual(dt.milliseconds, 999)
        self.assertEqual(dt.microseconds, 5000)
        self.assertEqual(dt.unused, "GPS Data")

    def test_invalid_values(self):
        # Test that invalid month raises a ValidationError.
        with self.assertRaises(ValidationError):
            ZWOASIDateTime(month=0)

        with self.assertRaises(ValidationError):
            ZWOASIDateTime(month=13)

        # Test that invalid day raises a ValidationError.
        with self.assertRaises(ValidationError):
            ZWOASIDateTime(day=0)

        with self.assertRaises(ValidationError):
            ZWOASIDateTime(day=32)

        # Test that invalid hour raises a ValidationError.
        with self.assertRaises(ValidationError):
            ZWOASIDateTime(hour=-1)

        # Test that invalid minute raises a ValidationError.
        with self.assertRaises(ValidationError):
            ZWOASIDateTime(minute=60)

        # Test that invalid second raises a ValidationError.
        with self.assertRaises(ValidationError):
            ZWOASIDateTime(second=60)

        # Test that invalid msecond raises a ValidationError.
        with self.assertRaises(ValidationError):
            ZWOASIDateTime(milliseconds=1000)

        # Test that invalid usecond raises a ValidationError.
        with self.assertRaises(ValidationError):
            ZWOASIDateTime(microseconds=10000)

        # Test that too long unused string raises a ValidationError.
        with self.assertRaises(ValidationError):
            ZWOASIDateTime(unused="a" * 65)

    def test_from_c_types(self):
        # Create a ctypes structure with sample values:
        c_datetime = ZWOASI_CAMERA_DATE_TIME_CTYPE()
        c_datetime.Year = 2025
        c_datetime.Month = 12
        c_datetime.Day = 31
        c_datetime.Hour = 23
        c_datetime.Minute = 59
        c_datetime.Second = 58
        c_datetime.Msecond = 500
        c_datetime.Usecond = 1234
        c_datetime.Unused = b"GPS Data"

        date = ZWOASIDateTime.from_c_types(c_datetime)

        self.assertEqual(date.year, 2025)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.day, 31)
        self.assertEqual(date.hour, 23)
        self.assertEqual(date.minute, 59)
        self.assertEqual(date.second, 58)
        self.assertEqual(date.milliseconds, 500)
        self.assertEqual(date.microseconds, 1234)
        self.assertEqual(date.unused, "GPS Data")


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
