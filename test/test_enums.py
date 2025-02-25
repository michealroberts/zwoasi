# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from zwoasi import ZWOASIBayerPattern, ZWOASIImageType

# **************************************************************************************


class TestASIBayerPattern(unittest.TestCase):
    """
    Ensure that each enum member has the correct numeric value.
    """

    def test_enum_values(self):
        self.assertEqual(ZWOASIBayerPattern.RG, 0)
        self.assertEqual(ZWOASIBayerPattern.BG, 1)
        self.assertEqual(ZWOASIBayerPattern.GR, 2)
        self.assertEqual(ZWOASIBayerPattern.GB, 3)

    def test_enum_member_by_name(self):
        """
        Access enum members by name and ensure they match the expected value.
        """
        self.assertIs(ZWOASIBayerPattern["RG"], ZWOASIBayerPattern.RG)
        self.assertIs(ZWOASIBayerPattern["BG"], ZWOASIBayerPattern.BG)
        self.assertIs(ZWOASIBayerPattern["GR"], ZWOASIBayerPattern.GR)
        self.assertIs(ZWOASIBayerPattern["GB"], ZWOASIBayerPattern.GB)

    def test_enum_member_from_int(self):
        """
        Cast integers to the enum and ensure they map to the correct members.
        """
        self.assertIs(ZWOASIBayerPattern(0), ZWOASIBayerPattern.RG)
        self.assertIs(ZWOASIBayerPattern(1), ZWOASIBayerPattern.BG)
        self.assertIs(ZWOASIBayerPattern(2), ZWOASIBayerPattern.GR)
        self.assertIs(ZWOASIBayerPattern(3), ZWOASIBayerPattern.GB)


# **************************************************************************************


class TestZWOASIImageType(unittest.TestCase):
    def test_enum_values(self):
        """
        Ensure that each enum member has the correct numeric value.
        """
        self.assertEqual(ZWOASIImageType.RAW8, 0)
        self.assertEqual(ZWOASIImageType.RGB24, 1)
        self.assertEqual(ZWOASIImageType.RAW16, 2)
        self.assertEqual(ZWOASIImageType.Y8, 3)
        self.assertEqual(ZWOASIImageType.END, -1)

    def test_enum_member_by_name(self):
        """
        Access enum members by name and ensure they match the expected value.
        """
        self.assertIs(ZWOASIImageType["RAW8"], ZWOASIImageType.RAW8)
        self.assertIs(ZWOASIImageType["RGB24"], ZWOASIImageType.RGB24)
        self.assertIs(ZWOASIImageType["RAW16"], ZWOASIImageType.RAW16)
        self.assertIs(ZWOASIImageType["Y8"], ZWOASIImageType.Y8)
        self.assertIs(ZWOASIImageType["END"], ZWOASIImageType.END)

    def test_enum_member_from_int(self):
        """
        Cast integers to the enum and ensure they map to the correct members.
        """
        self.assertIs(ZWOASIImageType(0), ZWOASIImageType.RAW8)
        self.assertIs(ZWOASIImageType(1), ZWOASIImageType.RGB24)
        self.assertIs(ZWOASIImageType(2), ZWOASIImageType.RAW16)
        self.assertIs(ZWOASIImageType(3), ZWOASIImageType.Y8)
        self.assertIs(ZWOASIImageType(-1), ZWOASIImageType.END)


# **************************************************************************************
