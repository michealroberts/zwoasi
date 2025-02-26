# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest
from pathlib import Path

from zwoasi.utils import get_asi_libary_path

# **************************************************************************************


class TestGetASILibraryPathForArch(unittest.TestCase):
    def test_get_asi_libary_path(self) -> None:
        sdk_location = get_asi_libary_path("1.37")
        self.assertIsInstance(sdk_location, Path)


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
