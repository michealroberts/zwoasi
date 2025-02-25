# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from zwoasi import ZWOASIBayerPattern, ZWOASICameraInformation, ZWOASIImageType

# **************************************************************************************


# Test suite for ZWOASICameraInformation
class TestZWOASICameraInformation(unittest.TestCase):
    def test_default_instance(self):
        """
        Test instantiation with default values.
        Since bayer_pattern is optional, it should default to None.
        """
        information = ZWOASICameraInformation()
        self.assertEqual(information.id, 0)
        self.assertEqual(information.name, "ZWO ASI Camera")
        self.assertEqual(information.maximum_height, 0)
        self.assertEqual(information.maximum_width, 0)
        self.assertEqual(information.pixel_size, 0.0)
        self.assertEqual(information.electrons_per_adu, 0.0)
        self.assertEqual(information.bit_depth, 1)
        self.assertIsNone(information.bayer_pattern)
        self.assertEqual(information.supported_binnings, [1, 2])
        self.assertEqual(information.supported_video_format, [])
        self.assertFalse(information.is_color)
        self.assertTrue(information.is_monochrome)
        self.assertFalse(information.is_usb3)
        self.assertFalse(information.is_usb3_host)
        self.assertFalse(information.has_st4_port)
        self.assertFalse(information.has_external_trigger)
        self.assertFalse(information.has_mechanical_shutter)
        self.assertFalse(information.has_cooler)
        self.assertEqual(information.unused, "")

    def test_full_instance(self):
        """
        Test instantiation with all fields explicitly set.
        """
        information = ZWOASICameraInformation(
            id=5,
            name="ZWO ASI Camera",
            maximum_height=8000,
            maximum_width=8000,
            pixel_size=5.6,
            electrons_per_adu=1.2,
            bit_depth=16,
            bayer_pattern=ZWOASIBayerPattern.BG,
            supported_binnings=[1, 2, 3, 4],
            supported_video_format=[
                ZWOASIImageType.RAW8,
                ZWOASIImageType.RGB24,
                ZWOASIImageType.END,
            ],
            is_color=True,
            is_monochrome=False,
            is_usb3=True,
            is_usb3_host=True,
            has_st4_port=True,
            has_external_trigger=True,
            has_mechanical_shutter=True,
            has_cooler=True,
            unused="unused",
        )
        self.assertEqual(information.id, 5)
        self.assertEqual(information.name, "ZWO ASI Camera")
        self.assertEqual(information.maximum_height, 8000)
        self.assertEqual(information.maximum_width, 8000)
        self.assertAlmostEqual(information.pixel_size, 5.6)
        self.assertAlmostEqual(information.electrons_per_adu, 1.2)
        self.assertEqual(information.bit_depth, 16)
        self.assertEqual(information.bayer_pattern, ZWOASIBayerPattern.BG)
        self.assertEqual(information.supported_binnings, [1, 2, 3, 4])
        self.assertEqual(
            information.supported_video_format,
            [ZWOASIImageType.RAW8, ZWOASIImageType.RGB24, ZWOASIImageType.END],
        )
        self.assertTrue(information.is_color)
        self.assertFalse(information.is_monochrome)
        self.assertTrue(information.is_usb3)
        self.assertTrue(information.is_usb3_host)
        self.assertTrue(information.has_st4_port)
        self.assertTrue(information.has_external_trigger)
        self.assertTrue(information.has_mechanical_shutter)
        self.assertTrue(information.has_cooler)
        self.assertEqual(information.unused, "unused")


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
