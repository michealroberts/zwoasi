# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest
from typing import Optional

from zwoasi import (
    ZWOASIError,
    ZWOASIExposureError,
    ZWOASIExposureStatus,
    ZWOASIIOError,
)

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


class TestZWOASIIOError(unittest.TestCase):
    def test_inheritance(self):
        """Test that ZWOASIIOError inherits from ZWOASIError."""
        self.assertTrue(issubclass(ZWOASIIOError, ZWOASIError))

    def test_error_message(self):
        """Test that the error message is correctly set for ZWOASIIOError."""
        test_message = "I/O error occurred."
        error = ZWOASIIOError(test_message)
        self.assertEqual(str(error), test_message)

    def test_error_code_default(self):
        """
        Test that if no error_code is provided, it defaults to None.
        """
        test_message = "I/O error occurred."
        error = ZWOASIIOError(test_message)
        self.assertIsNone(error.error_code)

    def test_error_code_custom(self):
        """
        Test that a custom error_code is correctly assigned to ZWOASIIOError.
        """
        test_message = "I/O error occurred."
        test_code = 42
        error = ZWOASIIOError(test_message, error_code=test_code)
        self.assertEqual(error.error_code, test_code)

    def test_raising_error_with_code(self):
        """
        Test raising ZWOASIIOError with a specific error_code and verifying it.
        """
        test_message = "I/O error with code."
        test_code = 500
        with self.assertRaises(ZWOASIIOError) as context:
            raise ZWOASIIOError(test_message, error_code=test_code)
        self.assertEqual(str(context.exception), test_message)
        self.assertEqual(context.exception.error_code, test_code)


# **************************************************************************************


class TestZWOASIExposureError(unittest.TestCase):
    def test_inheritance(self):
        """Test that ZWOASIExposureError inherits from ZWOASIError."""
        self.assertTrue(issubclass(ZWOASIExposureError, ZWOASIError))

    def test_error_message(self):
        """Test that the error message is correctly set and retrieved."""
        test_message = "Exposure error occurred."
        error = ZWOASIExposureError(test_message)
        self.assertEqual(str(error), test_message)

    def test_status_code_default(self):
        """Test that if no status_code is provided, it defaults to None."""
        test_message = "Exposure error occurred."
        error = ZWOASIExposureError(test_message)
        self.assertIsNone(error.status_code)

    def test_status_code_custom(self) -> None:
        """Test that a custom status_code is correctly assigned to ZWOASIExposureError."""
        test_message = "Exposure error with code."
        # For testing, we can simulate a status code with an int or a ZWOASIExposureStatus instance.
        # Here we'll assume ZWOASIExposureStatus is an IntEnum.
        test_status: Optional[ZWOASIExposureStatus] = ZWOASIExposureStatus(1)
        error = ZWOASIExposureError(test_message, status_code=test_status)
        self.assertEqual(error.status_code, 1)

    def test_raising_error_with_status(self) -> None:
        """Test that raising ZWOASIExposureError provides the correct message and status_code."""
        test_message = "Exposure failed."
        test_status = ZWOASIExposureStatus(3)  # Example status code.
        with self.assertRaises(ZWOASIExposureError) as context:
            raise ZWOASIExposureError(test_message, status_code=test_status)
        self.assertEqual(str(context.exception), test_message)
        self.assertEqual(context.exception.status_code, test_status)


# **************************************************************************************

if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
