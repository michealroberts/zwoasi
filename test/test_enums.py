# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from zwoasi import ZWOASIBayerPattern

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
