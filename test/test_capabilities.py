# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from zwoasi import ZWOASI_CAMERA_CAPABILITIES_CTYPE, ZWOASICameraCapabilities

# **************************************************************************************


class TestZWOASI_CAMERA_CAPABILITIES_CTYPE(unittest.TestCase):
    def test_field_assignment(self):
        # Create an instance and assign test values.
        caps = ZWOASI_CAMERA_CAPABILITIES_CTYPE()
        caps.Name = b"Exposure\x00"
        caps.Description = b"Exposure control for camera\x00"
        caps.MaxValue = 10000
        caps.MinValue = 10
        caps.DefaultValue = 100
        caps.IsAutoSupported = 1
        caps.IsWritable = 1
        caps.ControlType = 2
        caps.Unused = b"unused\x00"

        self.assertEqual(caps.Name.decode("utf-8").rstrip("\x00"), "Exposure")
        self.assertEqual(
            caps.Description.decode("utf-8").rstrip("\x00"),
            "Exposure control for camera",
        )
        self.assertEqual(caps.MaxValue, 10000)
        self.assertEqual(caps.MinValue, 10)
        self.assertEqual(caps.DefaultValue, 100)
        self.assertEqual(caps.IsAutoSupported, 1)
        self.assertEqual(caps.IsWritable, 1)
        self.assertEqual(caps.ControlType, 2)
        self.assertEqual(caps.Unused.decode("utf-8").rstrip("\x00"), "unused")


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

    def test_from_c_types(self):
        # Create an instance of the C structure with sample values.
        caps = ZWOASI_CAMERA_CAPABILITIES_CTYPE()
        caps.Name = b"Exposure\x00"
        caps.Description = b"Controls the exposure time\x00"
        caps.MaxValue = 10000
        caps.MinValue = 10
        caps.DefaultValue = 100
        caps.IsAutoSupported = 1
        caps.IsWritable = 1
        caps.ControlType = 2
        caps.Unused = b"unused_data\x00"

        # Convert to the Pydantic model.
        model = ZWOASICameraCapabilities.from_c_types(caps)
        self.assertEqual(model.name, "Exposure")
        self.assertEqual(model.description, "Controls the exposure time")
        self.assertEqual(model.maximum_value, 10000)
        self.assertEqual(model.minimum_value, 10)
        self.assertEqual(model.default_value, 100)
        self.assertTrue(model.is_auto_supported)
        self.assertTrue(model.is_writable)
        self.assertEqual(model.control_type, 2)
        self.assertEqual(model.unused, "unused_data")


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
