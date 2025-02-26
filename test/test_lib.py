# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from zwoasi.lib import ZWOASICameraLib

# **************************************************************************************


class TestZWOASICameraLib(unittest.TestCase):
    def test_library_setup(self) -> None:
        # Version (1, 36, 0) should raise a FileNotFoundError.
        with self.assertRaises(FileNotFoundError):
            ZWOASICameraLib(version=(1, 36, 0))

        # Version (1, 37, 0) is a valid library:
        try:
            lib = ZWOASICameraLib(version=(1, 37, 0))
        except FileNotFoundError as e:
            self.fail(f"FileNotFoundError raised while creating ZWOASICameraLib: {e}")

        self.assertIsInstance(lib, ZWOASICameraLib)
        self.assertIsNotNone(lib)

        # Version (1, 38, 0) should raise a FileNotFoundError.
        with self.assertRaises(FileNotFoundError):
            ZWOASICameraLib(version=(1, 38, 0))


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
