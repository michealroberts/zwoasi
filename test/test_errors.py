# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from zwoasi import ZWOASIError

# **************************************************************************************


class TestZWOASIError(unittest.TestCase):
    def test_inheritance(self):
        """Test that ZWOASIError inherits from the built-in Exception class."""
        self.assertTrue(issubclass(ZWOASIError, Exception))

    def test_error_message(self):
        """Test that the error message is correctly set and retrieved."""
        test_message = "This is a test error message."
        error = ZWOASIError(test_message)
        self.assertEqual(str(error), test_message)

    def test_raising_error(self):
        """
        Test that raising ZWOASIError with a specific message
        results in that message being available on the exception.
        """
        test_message = "An error occurred."
        with self.assertRaises(ZWOASIError) as context:
            raise ZWOASIError(test_message)
        self.assertEqual(str(context.exception), test_message)


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
