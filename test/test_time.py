# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest
from datetime import datetime

from pydantic import ValidationError

from zwoasi import ZWOASIDateTime

# **************************************************************************************


class TestASIDateTime(unittest.TestCase):
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


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
