# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from zwoasi import ZWOASICameraCapabilities

# **************************************************************************************


class TestZWOASICameraCapabilities(unittest.TestCase):
    def test_default_instance(self):
        """Test that the model returns the expected default values."""
        capability = ZWOASICameraCapabilities()
        self.assertEqual(capability.name, "")
        self.assertEqual(capability.description, "")
        self.assertEqual(capability.minimum_value, 0)
        self.assertEqual(capability.maximum_value, 0)
        self.assertEqual(capability.default_value, 0)
        self.assertFalse(capability.is_auto_supported)
        self.assertFalse(capability.is_writable)
        self.assertEqual(capability.control_type, 0)
        self.assertEqual(capability.unused, "")

    def test_full_instance(self):
        """Test that the model returns the expected values when explicitly set."""
        capability = ZWOASICameraCapabilities(
            name="Exposure",
            description="Controls the exposure time.",
            minimum_value=10,
            maximum_value=10000,
            default_value=100,
            is_auto_supported=True,
            is_writable=True,
            control_type=2,
            unused="unused_data",
        )
        self.assertEqual(capability.name, "Exposure")
        self.assertEqual(capability.description, "Controls the exposure time.")
        self.assertEqual(capability.minimum_value, 10)
        self.assertEqual(capability.maximum_value, 10000)
        self.assertEqual(capability.default_value, 100)
        self.assertTrue(capability.is_auto_supported)
        self.assertTrue(capability.is_writable)
        self.assertEqual(capability.control_type, 2)
        self.assertEqual(capability.unused, "unused_data")


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
