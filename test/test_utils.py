# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest
from pathlib import Path

from zwoasi.utils import get_asi_libary_path, is_hexadecimal

# **************************************************************************************


class TestGetASILibraryPathForArch(unittest.TestCase):
    def test_get_asi_libary_path(self) -> None:
        sdk_location = get_asi_libary_path("1.37")
        self.assertIsInstance(sdk_location, Path)


# **************************************************************************************


class TestIsHexadecimal(unittest.TestCase):
    def test_none(self):
        self.assertFalse(is_hexadecimal(None), "None should return False.")

    def test_empty_string(self):
        self.assertFalse(is_hexadecimal(""), "Empty string should return False.")

    def test_single_digit_zero(self):
        self.assertTrue(is_hexadecimal("0"), "'0' should be recognized as valid hex.")

    def test_single_hex_lower(self):
        self.assertTrue(is_hexadecimal("a"), "'a' should be recognized as valid hex.")
        self.assertTrue(is_hexadecimal("f"), "'f' should be recognized as valid hex.")

    def test_single_hex_upper(self):
        self.assertTrue(is_hexadecimal("A"), "'A' should be recognized as valid hex.")
        self.assertTrue(is_hexadecimal("F"), "'F' should be recognized as valid hex.")

    def test_multi_hex_lower(self):
        self.assertTrue(is_hexadecimal("12af"), "'12af' should be valid hex.")

    def test_multi_hex_upper(self):
        self.assertTrue(is_hexadecimal("12AF"), "'12AF' should be valid hex.")

    def test_with_0x_prefix_lower(self):
        # Python's int(value, 16) will interpret '0x' prefix
        self.assertTrue(is_hexadecimal("0x1a"), "'0x1a' should be valid hex.")

    def test_with_0x_prefix_upper(self):
        self.assertTrue(is_hexadecimal("0X1A"), "'0X1A' should be valid hex.")

    def test_invalid_character(self):
        self.assertFalse(is_hexadecimal("g"), "'g' should not be valid hex.")
        self.assertFalse(is_hexadecimal("G"), "'G' should not be valid hex.")

    def test_mixed_invalid_character(self):
        self.assertFalse(is_hexadecimal("12ag"), "'12ag' should not be valid hex.")

    def test_all_invalid_characters(self):
        self.assertFalse(is_hexadecimal("ZZZZ"), "'ZZZZ' should not be valid hex.")


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
