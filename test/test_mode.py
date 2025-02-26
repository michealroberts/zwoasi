# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from pydantic import ValidationError

from zwoasi import ZWOASICameraSupportedMode

# **************************************************************************************


class TestZWOASICameraSupportedMode(unittest.TestCase):
    def test_default_instance(self):
        """Test that the default instance has an empty supported_mode list."""
        mode = ZWOASICameraSupportedMode()
        self.assertEqual(mode.supported_mode, [])

    def test_valid_supported_mode(self):
        """Test that a supported_mode list with <= 16 items is valid."""
        # Test with a list of 10 items.
        valid_list = list(range(10))
        mode = ZWOASICameraSupportedMode(supported_mode=valid_list)
        self.assertEqual(mode.supported_mode, valid_list)

        # Test with exactly 16 items.
        valid_list_16 = list(range(16))
        mode = ZWOASICameraSupportedMode(supported_mode=valid_list_16)
        self.assertEqual(mode.supported_mode, valid_list_16)

    def test_invalid_supported_mode(self):
        """Test that a supported_mode list with more than 16 items raises a ValidationError."""
        invalid_list = list(range(17))
        with self.assertRaises(ValidationError) as context:
            ZWOASICameraSupportedMode(supported_mode=invalid_list)
        self.assertIn(
            "supported_mode must contain at most 16 items", str(context.exception)
        )


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
