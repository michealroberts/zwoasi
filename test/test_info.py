# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from zwoasi import (
    ZWOASI_CAMERA_INFORMATION_CTYPE,
    ZWOASIBayerPattern,
    ZWOASICameraInformation,
    ZWOASIImageType,
)

# **************************************************************************************


class TestZWOASI_CAMERA_INFORMATION_CTYPE(unittest.TestCase):
    def test_field_assignment(self):
        # Create a ctypes structure with sample values:
        c_info = ZWOASI_CAMERA_INFORMATION_CTYPE()
        c_info.Name = b"ZWO ASI Camera\x00"
        c_info.CameraID = 1
        c_info.MaxHeight = 1080
        c_info.MaxWidth = 1920
        c_info.PixelSize = 5.6
        c_info.ElecPerADU = 1.2
        c_info.BitDepth = 16
        c_info.BayerPattern = 1

        # Set up supported_binnings: [1, 2, 3, 4] then 0 sentinel:
        supported_binnings = [1, 2, 3, 4]
        for i in range(16):
            if i < len(supported_binnings):
                c_info.SupportedBins[i] = supported_binnings[i]
            else:
                c_info.SupportedBins[i] = 0

        # Set up supported_video_format: [RAW8, RGB24, END] (END is sentinel).
        # For testing, RAW8=0, RGB24=1, END=-1:
        supported_video_format = [
            ZWOASIImageType.RAW8.value,
            ZWOASIImageType.RGB24.value,
            ZWOASIImageType.END.value,
        ]

        for i in range(8):
            if i < len(supported_video_format):
                c_info.SupportedVideoFormat[i] = supported_video_format[i]
            else:
                c_info.SupportedVideoFormat[i] = -1

        c_info.IsColorCam = 1
        c_info.MechanicalShutter = 0
        c_info.ST4Port = 1
        c_info.IsCoolerCam = 0
        c_info.IsUSB3Host = 1
        c_info.IsUSB3Camera = 0
        c_info.IsTriggerCam = 1
        c_info.Unused = b"unused\x00"

        self.assertEqual(c_info.Name.decode("utf-8").rstrip("\x00"), "ZWO ASI Camera")
        self.assertEqual(c_info.CameraID, 1)
        self.assertEqual(c_info.MaxHeight, 1080)
        self.assertEqual(c_info.MaxWidth, 1920)
        self.assertEqual(c_info.BayerPattern, ZWOASIBayerPattern.BG)
        self.assertAlmostEqual(c_info.PixelSize, 5.6)
        self.assertAlmostEqual(c_info.ElecPerADU, 1.2)
        self.assertEqual(c_info.BitDepth, 16)

        for i in range(len(supported_binnings)):
            self.assertEqual(c_info.SupportedBins[i], supported_binnings[i])

        for i in range(len(supported_binnings), 16):
            self.assertEqual(c_info.SupportedBins[i], 0)

        self.assertEqual(c_info.SupportedVideoFormat[0], 0)
        self.assertEqual(c_info.SupportedVideoFormat[1], 1)
        self.assertEqual(c_info.SupportedVideoFormat[2], -1)

        for i in range(3, 8):
            self.assertEqual(c_info.SupportedVideoFormat[i], -1)

        self.assertEqual(c_info.IsColorCam, 1)
        self.assertEqual(c_info.MechanicalShutter, 0)
        self.assertEqual(c_info.ST4Port, 1)
        self.assertEqual(c_info.IsCoolerCam, 0)
        self.assertEqual(c_info.IsUSB3Host, 1)
        self.assertEqual(c_info.IsUSB3Camera, 0)
        self.assertEqual(c_info.IsTriggerCam, 1)
        self.assertEqual(c_info.Unused.decode("utf-8").rstrip("\x00"), "unused")


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
