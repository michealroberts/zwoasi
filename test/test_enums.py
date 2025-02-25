# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from zwoasi import (
    ZWOASIBayerPattern,
    ZWOASICameraMode,
    ZWOASIFlipStatus,
    ZWOASIGuideDirection,
    ZWOASIImageType,
)

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


class TestZWOASIGuideDirection(unittest.TestCase):
    def test_enum_values(self):
        """
        Ensure that each enum member has the correct numeric value.
        """
        self.assertEqual(ZWOASIGuideDirection.NORTH, 0)
        self.assertEqual(ZWOASIGuideDirection.SOUTH, 1)
        self.assertEqual(ZWOASIGuideDirection.EAST, 2)
        self.assertEqual(ZWOASIGuideDirection.WEST, 3)

    def test_enum_member_by_name(self):
        """
        Access enum members by name and ensure they match the expected value.
        """
        self.assertIs(ZWOASIGuideDirection["NORTH"], ZWOASIGuideDirection.NORTH)
        self.assertIs(ZWOASIGuideDirection["SOUTH"], ZWOASIGuideDirection.SOUTH)
        self.assertIs(ZWOASIGuideDirection["EAST"], ZWOASIGuideDirection.EAST)
        self.assertIs(ZWOASIGuideDirection["WEST"], ZWOASIGuideDirection.WEST)

    def test_enum_member_from_int(self):
        """
        Cast integers to the enum and ensure they map to the correct members.
        """
        self.assertIs(ZWOASIGuideDirection(0), ZWOASIGuideDirection.NORTH)
        self.assertIs(ZWOASIGuideDirection(1), ZWOASIGuideDirection.SOUTH)
        self.assertIs(ZWOASIGuideDirection(2), ZWOASIGuideDirection.EAST)
        self.assertIs(ZWOASIGuideDirection(3), ZWOASIGuideDirection.WEST)


# **************************************************************************************


class TestZWOASIFlipStatus(unittest.TestCase):
    def test_enum_values(self):
        """
        Ensure that each enum member has the correct numeric value.
        """
        self.assertEqual(ZWOASIFlipStatus.NONE, 0)
        self.assertEqual(ZWOASIFlipStatus.HORIZ, 1)
        self.assertEqual(ZWOASIFlipStatus.VERT, 2)
        self.assertEqual(ZWOASIFlipStatus.BOTH, 3)

    def test_enum_member_by_name(self):
        """
        Access enum members by name and ensure they match the expected value.
        """
        self.assertIs(ZWOASIFlipStatus["NONE"], ZWOASIFlipStatus.NONE)
        self.assertIs(ZWOASIFlipStatus["HORIZ"], ZWOASIFlipStatus.HORIZ)
        self.assertIs(ZWOASIFlipStatus["VERT"], ZWOASIFlipStatus.VERT)
        self.assertIs(ZWOASIFlipStatus["BOTH"], ZWOASIFlipStatus.BOTH)

    def test_enum_member_from_int(self):
        """
        Cast integers to the enum and ensure they map to the correct members.
        """
        self.assertIs(ZWOASIFlipStatus(0), ZWOASIFlipStatus.NONE)
        self.assertIs(ZWOASIFlipStatus(1), ZWOASIFlipStatus.HORIZ)
        self.assertIs(ZWOASIFlipStatus(2), ZWOASIFlipStatus.VERT)
        self.assertIs(ZWOASIFlipStatus(3), ZWOASIFlipStatus.BOTH)


# **************************************************************************************


class TestZWOASICameraMode(unittest.TestCase):
    def test_enum_values(self):
        """
        Verify that the integer values match the C enum specification.
        """
        self.assertEqual(ZWOASICameraMode.NORMAL, 0)
        self.assertEqual(ZWOASICameraMode.TRIGGER_SOFT_EDGE, 1)
        self.assertEqual(ZWOASICameraMode.TRIGGER_RISE_EDGE, 2)
        self.assertEqual(ZWOASICameraMode.TRIGGER_FALL_EDGE, 3)
        self.assertEqual(ZWOASICameraMode.TRIGGER_SOFT_LEVEL, 4)
        self.assertEqual(ZWOASICameraMode.TRIGGER_HIGH_LEVEL, 5)
        self.assertEqual(ZWOASICameraMode.TRIGGER_LOW_LEVEL, 6)
        self.assertEqual(ZWOASICameraMode.END, -1)

    def test_enum_member_by_name(self):
        """
        Access enum members by name to ensure they match the expected values.
        """
        self.assertIs(ZWOASICameraMode["NORMAL"], ZWOASICameraMode.NORMAL)
        self.assertIs(
            ZWOASICameraMode["TRIGGER_SOFT_EDGE"], ZWOASICameraMode.TRIGGER_SOFT_EDGE
        )
        self.assertIs(
            ZWOASICameraMode["TRIGGER_RISE_EDGE"], ZWOASICameraMode.TRIGGER_RISE_EDGE
        )
        self.assertIs(
            ZWOASICameraMode["TRIGGER_FALL_EDGE"], ZWOASICameraMode.TRIGGER_FALL_EDGE
        )
        self.assertIs(
            ZWOASICameraMode["TRIGGER_SOFT_LEVEL"], ZWOASICameraMode.TRIGGER_SOFT_LEVEL
        )
        self.assertIs(
            ZWOASICameraMode["TRIGGER_HIGH_LEVEL"], ZWOASICameraMode.TRIGGER_HIGH_LEVEL
        )
        self.assertIs(
            ZWOASICameraMode["TRIGGER_LOW_LEVEL"], ZWOASICameraMode.TRIGGER_LOW_LEVEL
        )
        self.assertIs(ZWOASICameraMode["END"], ZWOASICameraMode.END)

    def test_enum_member_from_int(self):
        """
        Cast integers to the enum to ensure they resolve to the correct members.
        """
        self.assertIs(ZWOASICameraMode(0), ZWOASICameraMode.NORMAL)
        self.assertIs(ZWOASICameraMode(1), ZWOASICameraMode.TRIGGER_SOFT_EDGE)
        self.assertIs(ZWOASICameraMode(2), ZWOASICameraMode.TRIGGER_RISE_EDGE)
        self.assertIs(ZWOASICameraMode(3), ZWOASICameraMode.TRIGGER_FALL_EDGE)
        self.assertIs(ZWOASICameraMode(4), ZWOASICameraMode.TRIGGER_SOFT_LEVEL)
        self.assertIs(ZWOASICameraMode(5), ZWOASICameraMode.TRIGGER_HIGH_LEVEL)
        self.assertIs(ZWOASICameraMode(6), ZWOASICameraMode.TRIGGER_LOW_LEVEL)
        self.assertIs(ZWOASICameraMode(-1), ZWOASICameraMode.END)
