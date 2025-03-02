# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from pydantic import ValidationError

from zwo import ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE, ZWOASICameraSupportedMode

# **************************************************************************************


class TestZWOASI_CAMERA_SUPPORTED_MODE_CTYPE(unittest.TestCase):
    def test_full_assignment(self):
        """Test that all 16 values can be assigned and read correctly."""
        instance = ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE()
        test_modes = list(range(1, 17))  # [1, 2, ..., 16]
        for i in range(16):
            instance.SupportedCameraMode[i] = test_modes[i]

        for i in range(16):
            self.assertEqual(instance.SupportedCameraMode[i], test_modes[i])

    def test_partial_assignment_with_sentinel(self):
        """
        Test that if only part of the array is assigned and the remainder is zero,
        the structure reflects the sentinel value (0) for unassigned positions.
        """
        instance = ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE()
        test_modes = [10, 20, 30, 40]  # fewer than 16 values
        for i in range(16):
            if i < len(test_modes):
                instance.SupportedCameraMode[i] = test_modes[i]
            else:
                instance.SupportedCameraMode[i] = 0

        for i in range(len(test_modes)):
            self.assertEqual(instance.SupportedCameraMode[i], test_modes[i])
        for i in range(len(test_modes), 16):
            self.assertEqual(instance.SupportedCameraMode[i], 0)


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

    def test_from_c_types_full(self):
        """Test conversion when all 16 modes are set."""
        c_mode = ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE()
        test_modes = list(range(1, 17))  # [1, 2, ..., 16]
        for i in range(16):
            c_mode.SupportedCameraMode[i] = test_modes[i]
        model = ZWOASICameraSupportedMode.from_c_types(c_mode)
        # Since no sentinel encountered, our logic stops at first 0,
        # but here all 16 values are non-zero, so we return the full list.
        self.assertEqual(model.supported_mode, test_modes)

    def test_from_c_types_partial(self):
        """Test conversion when only part of the array is set and then a 0 is encountered."""
        c_mode = ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE()
        test_modes = [10, 20, 30, 40]
        # Fill array: first four values, then 0 for the rest.
        for i in range(16):
            c_mode.SupportedCameraMode[i] = test_modes[i] if i < len(test_modes) else 0
        model = ZWOASICameraSupportedMode.from_c_types(c_mode)
        self.assertEqual(model.supported_mode, test_modes)

    def test_from_c_types_empty(self):
        """Test conversion when the array is all zeros."""
        c_mode = ZWOASI_CAMERA_SUPPORTED_MODE_CTYPE()
        for i in range(16):
            c_mode.SupportedCameraMode[i] = 0
        model = ZWOASICameraSupportedMode.from_c_types(c_mode)
        self.assertEqual(model.supported_mode, [])


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
