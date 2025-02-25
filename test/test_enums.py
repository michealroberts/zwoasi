# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from zwoasi import (
    ZWOASIBayerPattern,
    ZWOASIBool,
    ZWOASICameraMode,
    ZWOASIControlType,
    ZWOASIErrorCode,
    ZWOASIExposureStatus,
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
        self.assertEqual(ZWOASIFlipStatus.HORIZONTAL, 1)
        self.assertEqual(ZWOASIFlipStatus.VERTICAL, 2)
        self.assertEqual(ZWOASIFlipStatus.BOTH, 3)

    def test_enum_member_by_name(self):
        """
        Access enum members by name and ensure they match the expected value.
        """
        self.assertIs(ZWOASIFlipStatus["NONE"], ZWOASIFlipStatus.NONE)
        self.assertIs(ZWOASIFlipStatus["HORIZONTAL"], ZWOASIFlipStatus.HORIZONTAL)
        self.assertIs(ZWOASIFlipStatus["VERTICAL"], ZWOASIFlipStatus.VERTICAL)
        self.assertIs(ZWOASIFlipStatus["BOTH"], ZWOASIFlipStatus.BOTH)

    def test_enum_member_from_int(self):
        """
        Cast integers to the enum and ensure they map to the correct members.
        """
        self.assertIs(ZWOASIFlipStatus(0), ZWOASIFlipStatus.NONE)
        self.assertIs(ZWOASIFlipStatus(1), ZWOASIFlipStatus.HORIZONTAL)
        self.assertIs(ZWOASIFlipStatus(2), ZWOASIFlipStatus.VERTICAL)
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


# **************************************************************************************


class TestZWOASIErrorCode(unittest.TestCase):
    def test_enum_values(self):
        """
        Verify that the integer values match the C enum specification.
        """
        self.assertEqual(ZWOASIErrorCode.SUCCESS, 0)
        self.assertEqual(ZWOASIErrorCode.INVALID_INDEX, 1)
        self.assertEqual(ZWOASIErrorCode.INVALID_ID, 2)
        self.assertEqual(ZWOASIErrorCode.INVALID_CONTROL_TYPE, 3)
        self.assertEqual(ZWOASIErrorCode.CAMERA_CLOSED, 4)
        self.assertEqual(ZWOASIErrorCode.CAMERA_REMOVED, 5)
        self.assertEqual(ZWOASIErrorCode.INVALID_PATH, 6)
        self.assertEqual(ZWOASIErrorCode.INVALID_FILEFORMAT, 7)
        self.assertEqual(ZWOASIErrorCode.INVALID_VIDEO_SIZE, 8)
        self.assertEqual(ZWOASIErrorCode.INVALID_IMAGE_TYPE, 9)
        self.assertEqual(ZWOASIErrorCode.START_POSITION_OUT_OF_BOUNDARY, 10)
        self.assertEqual(ZWOASIErrorCode.TIMEOUT, 11)
        self.assertEqual(ZWOASIErrorCode.INVALID_SEQUENCE, 12)
        self.assertEqual(ZWOASIErrorCode.BUFFER_TOO_SMALL, 13)
        self.assertEqual(ZWOASIErrorCode.VIDEO_MODE_ACTIVE, 14)
        self.assertEqual(ZWOASIErrorCode.EXPOSURE_IN_PROGRESS, 15)
        self.assertEqual(ZWOASIErrorCode.GENERAL_ERROR, 16)
        self.assertEqual(ZWOASIErrorCode.INVALID_MODE, 17)
        self.assertEqual(ZWOASIErrorCode.GPS_NOT_SUPPORTED, 18)
        self.assertEqual(ZWOASIErrorCode.INVALID_GPS_VERSION, 19)
        self.assertEqual(ZWOASIErrorCode.INVALID_GPS_FPGA, 20)
        self.assertEqual(ZWOASIErrorCode.INVALID_GPS_PARAM_OUT_OF_RANGE, 21)
        self.assertEqual(ZWOASIErrorCode.INVALID_GPS_DATA, 22)
        self.assertEqual(ZWOASIErrorCode.END, 23)

    def test_enum_member_by_name(self):
        """
        Access enum members by name to ensure they match the expected values.
        """
        self.assertIs(ZWOASIErrorCode["SUCCESS"], ZWOASIErrorCode.SUCCESS)
        self.assertIs(ZWOASIErrorCode["INVALID_INDEX"], ZWOASIErrorCode.INVALID_INDEX)
        self.assertIs(ZWOASIErrorCode["INVALID_ID"], ZWOASIErrorCode.INVALID_ID)
        self.assertIs(
            ZWOASIErrorCode["INVALID_CONTROL_TYPE"],
            ZWOASIErrorCode.INVALID_CONTROL_TYPE,
        )
        self.assertIs(ZWOASIErrorCode["CAMERA_CLOSED"], ZWOASIErrorCode.CAMERA_CLOSED)
        self.assertIs(
            ZWOASIErrorCode["CAMERA_REMOVED"],
            ZWOASIErrorCode.CAMERA_REMOVED,
        )
        self.assertIs(ZWOASIErrorCode["INVALID_PATH"], ZWOASIErrorCode.INVALID_PATH)
        self.assertIs(
            ZWOASIErrorCode["INVALID_FILEFORMAT"],
            ZWOASIErrorCode.INVALID_FILEFORMAT,
        )
        self.assertIs(
            ZWOASIErrorCode["INVALID_VIDEO_SIZE"], ZWOASIErrorCode.INVALID_VIDEO_SIZE
        )
        self.assertIs(
            ZWOASIErrorCode["INVALID_IMAGE_TYPE"],
            ZWOASIErrorCode.INVALID_IMAGE_TYPE,
        )
        self.assertIs(
            ZWOASIErrorCode["START_POSITION_OUT_OF_BOUNDARY"],
            ZWOASIErrorCode.START_POSITION_OUT_OF_BOUNDARY,
        )
        self.assertIs(ZWOASIErrorCode["TIMEOUT"], ZWOASIErrorCode.TIMEOUT)
        self.assertIs(
            ZWOASIErrorCode["INVALID_SEQUENCE"],
            ZWOASIErrorCode.INVALID_SEQUENCE,
        )
        self.assertIs(
            ZWOASIErrorCode["BUFFER_TOO_SMALL"],
            ZWOASIErrorCode.BUFFER_TOO_SMALL,
        )
        self.assertIs(
            ZWOASIErrorCode["VIDEO_MODE_ACTIVE"],
            ZWOASIErrorCode.VIDEO_MODE_ACTIVE,
        )
        self.assertIs(
            ZWOASIErrorCode["EXPOSURE_IN_PROGRESS"],
            ZWOASIErrorCode.EXPOSURE_IN_PROGRESS,
        )
        self.assertIs(ZWOASIErrorCode["GENERAL_ERROR"], ZWOASIErrorCode.GENERAL_ERROR)
        self.assertIs(ZWOASIErrorCode["INVALID_MODE"], ZWOASIErrorCode.INVALID_MODE)
        self.assertIs(
            ZWOASIErrorCode["GPS_NOT_SUPPORTED"],
            ZWOASIErrorCode.GPS_NOT_SUPPORTED,
        )
        self.assertIs(
            ZWOASIErrorCode["INVALID_GPS_VERSION"],
            ZWOASIErrorCode.INVALID_GPS_VERSION,
        )
        self.assertIs(
            ZWOASIErrorCode["INVALID_GPS_FPGA"],
            ZWOASIErrorCode.INVALID_GPS_FPGA,
        )
        self.assertIs(
            ZWOASIErrorCode["INVALID_GPS_PARAM_OUT_OF_RANGE"],
            ZWOASIErrorCode.INVALID_GPS_PARAM_OUT_OF_RANGE,
        )
        self.assertIs(
            ZWOASIErrorCode["INVALID_GPS_DATA"],
            ZWOASIErrorCode.INVALID_GPS_DATA,
        )
        self.assertIs(ZWOASIErrorCode["END"], ZWOASIErrorCode.END)

    def test_enum_member_from_int(self):
        """
        Cast integers to the enum to ensure they resolve to the correct members.
        """
        self.assertIs(ZWOASIErrorCode(0), ZWOASIErrorCode.SUCCESS)
        self.assertIs(ZWOASIErrorCode(1), ZWOASIErrorCode.INVALID_INDEX)
        self.assertIs(ZWOASIErrorCode(2), ZWOASIErrorCode.INVALID_ID)
        self.assertIs(ZWOASIErrorCode(3), ZWOASIErrorCode.INVALID_CONTROL_TYPE)
        self.assertIs(ZWOASIErrorCode(4), ZWOASIErrorCode.CAMERA_CLOSED)
        self.assertIs(ZWOASIErrorCode(5), ZWOASIErrorCode.CAMERA_REMOVED)
        self.assertIs(ZWOASIErrorCode(6), ZWOASIErrorCode.INVALID_PATH)
        self.assertIs(ZWOASIErrorCode(7), ZWOASIErrorCode.INVALID_FILEFORMAT)
        self.assertIs(ZWOASIErrorCode(8), ZWOASIErrorCode.INVALID_VIDEO_SIZE)
        self.assertIs(ZWOASIErrorCode(9), ZWOASIErrorCode.INVALID_IMAGE_TYPE)
        self.assertIs(
            ZWOASIErrorCode(10), ZWOASIErrorCode.START_POSITION_OUT_OF_BOUNDARY
        )
        self.assertIs(ZWOASIErrorCode(11), ZWOASIErrorCode.TIMEOUT)
        self.assertIs(ZWOASIErrorCode(12), ZWOASIErrorCode.INVALID_SEQUENCE)
        self.assertIs(ZWOASIErrorCode(13), ZWOASIErrorCode.BUFFER_TOO_SMALL)
        self.assertIs(ZWOASIErrorCode(14), ZWOASIErrorCode.VIDEO_MODE_ACTIVE)
        self.assertIs(ZWOASIErrorCode(15), ZWOASIErrorCode.EXPOSURE_IN_PROGRESS)
        self.assertIs(ZWOASIErrorCode(16), ZWOASIErrorCode.GENERAL_ERROR)
        self.assertIs(ZWOASIErrorCode(17), ZWOASIErrorCode.INVALID_MODE)
        self.assertIs(ZWOASIErrorCode(18), ZWOASIErrorCode.GPS_NOT_SUPPORTED)
        self.assertIs(ZWOASIErrorCode(19), ZWOASIErrorCode.INVALID_GPS_VERSION)
        self.assertIs(ZWOASIErrorCode(20), ZWOASIErrorCode.INVALID_GPS_FPGA)
        self.assertIs(
            ZWOASIErrorCode(21), ZWOASIErrorCode.INVALID_GPS_PARAM_OUT_OF_RANGE
        )
        self.assertIs(ZWOASIErrorCode(22), ZWOASIErrorCode.INVALID_GPS_DATA)
        self.assertIs(ZWOASIErrorCode(23), ZWOASIErrorCode.END)


# **************************************************************************************


class TestZWOASIBool(unittest.TestCase):
    def test_enum_values(self):
        """
        Verify that the integer values match the C enum specification.
        """
        self.assertEqual(ZWOASIBool.FALSE, 0)
        self.assertEqual(ZWOASIBool.TRUE, 1)

    def test_enum_member_by_name(self):
        """
        Access enum members by name to ensure they match the expected values.
        """
        self.assertIs(ZWOASIBool["FALSE"], ZWOASIBool.FALSE)
        self.assertIs(ZWOASIBool["TRUE"], ZWOASIBool.TRUE)

    def test_enum_member_from_int(self):
        """
        Cast integers to the enum to ensure they resolve to the correct members.
        """
        self.assertIs(ZWOASIBool(0), ZWOASIBool.FALSE)
        self.assertIs(ZWOASIBool(1), ZWOASIBool.TRUE)


# **************************************************************************************


class TestZWOASIControlType(unittest.TestCase):
    def test_enum_values(self):
        self.assertEqual(ZWOASIControlType.GAIN, 0)
        self.assertEqual(ZWOASIControlType.EXPOSURE, 1)
        self.assertEqual(ZWOASIControlType.GAMMA, 2)
        self.assertEqual(ZWOASIControlType.WHITE_BALANCE_RED_CHANNEL, 3)
        self.assertEqual(ZWOASIControlType.WHITE_BALANCE_BLUE_CHANNEL, 4)
        self.assertEqual(ZWOASIControlType.OFFSET, 5)
        self.assertEqual(ZWOASIControlType.BANDWIDTH_OVERLOAD, 6)
        self.assertEqual(ZWOASIControlType.OVERCLOCK, 7)
        self.assertEqual(ZWOASIControlType.TEMPERATURE_READING, 8)
        self.assertEqual(ZWOASIControlType.IMAGE_FLIP, 9)
        self.assertEqual(ZWOASIControlType.AUTO_MAXIMUM_GAIN, 10)
        self.assertEqual(ZWOASIControlType.AUTO_MAXIMUM_EXPOSURE, 11)
        self.assertEqual(ZWOASIControlType.AUTO_TARGET_BRIGHTNESS, 12)
        self.assertEqual(ZWOASIControlType.HARDWARE_BINNING, 13)
        self.assertEqual(ZWOASIControlType.HIGH_SPEED_MODE, 14)
        self.assertEqual(ZWOASIControlType.COOLER_POWER_PERCENTAGE, 15)
        self.assertEqual(ZWOASIControlType.TARGET_TEMPERATURE, 16)
        self.assertEqual(ZWOASIControlType.COOLER_ON_OFF, 17)
        self.assertEqual(ZWOASIControlType.MONOCHROME_BINNING, 18)
        self.assertEqual(ZWOASIControlType.FAN_ON_OFF, 19)
        self.assertEqual(ZWOASIControlType.PATTERN_ADJUSTMENT, 20)
        self.assertEqual(ZWOASIControlType.ANTI_DEW_HEATER, 21)
        self.assertEqual(ZWOASIControlType.FAN_SPEED_ADJUSTMENT, 22)
        self.assertEqual(ZWOASIControlType.POWER_LED_BRIGHTNESS, 23)
        self.assertEqual(ZWOASIControlType.USB_HUB_RESET, 24)
        self.assertEqual(ZWOASIControlType.GPS_SUPPORT_INDICATOR, 25)
        self.assertEqual(ZWOASIControlType.GPS_START_LINE_POSITION, 26)
        self.assertEqual(ZWOASIControlType.GPS_END_LINE_POSITION, 27)
        self.assertEqual(ZWOASIControlType.ROLLING_SHUTTER_INTERVAL, 28)

    def test_enum_member_by_name(self):
        self.assertIs(ZWOASIControlType["GAIN"], ZWOASIControlType.GAIN)
        self.assertIs(ZWOASIControlType["EXPOSURE"], ZWOASIControlType.EXPOSURE)
        self.assertIs(ZWOASIControlType["GAMMA"], ZWOASIControlType.GAMMA)
        self.assertIs(
            ZWOASIControlType["WHITE_BALANCE_RED_CHANNEL"],
            ZWOASIControlType.WHITE_BALANCE_RED_CHANNEL,
        )
        self.assertIs(
            ZWOASIControlType["WHITE_BALANCE_BLUE_CHANNEL"],
            ZWOASIControlType.WHITE_BALANCE_BLUE_CHANNEL,
        )
        self.assertIs(ZWOASIControlType["OFFSET"], ZWOASIControlType.OFFSET)
        self.assertIs(
            ZWOASIControlType["BANDWIDTH_OVERLOAD"],
            ZWOASIControlType.BANDWIDTH_OVERLOAD,
        )
        self.assertIs(ZWOASIControlType["OVERCLOCK"], ZWOASIControlType.OVERCLOCK)
        self.assertIs(
            ZWOASIControlType["TEMPERATURE_READING"],
            ZWOASIControlType.TEMPERATURE_READING,
        )
        self.assertIs(ZWOASIControlType["IMAGE_FLIP"], ZWOASIControlType.IMAGE_FLIP)
        self.assertIs(
            ZWOASIControlType["AUTO_MAXIMUM_GAIN"], ZWOASIControlType.AUTO_MAXIMUM_GAIN
        )
        self.assertIs(
            ZWOASIControlType["AUTO_MAXIMUM_EXPOSURE"],
            ZWOASIControlType.AUTO_MAXIMUM_EXPOSURE,
        )
        self.assertIs(
            ZWOASIControlType["AUTO_TARGET_BRIGHTNESS"],
            ZWOASIControlType.AUTO_TARGET_BRIGHTNESS,
        )
        self.assertIs(
            ZWOASIControlType["HARDWARE_BINNING"], ZWOASIControlType.HARDWARE_BINNING
        )
        self.assertIs(
            ZWOASIControlType["HIGH_SPEED_MODE"], ZWOASIControlType.HIGH_SPEED_MODE
        )
        self.assertIs(
            ZWOASIControlType["COOLER_POWER_PERCENTAGE"],
            ZWOASIControlType.COOLER_POWER_PERCENTAGE,
        )
        self.assertIs(
            ZWOASIControlType["TARGET_TEMPERATURE"],
            ZWOASIControlType.TARGET_TEMPERATURE,
        )
        self.assertIs(
            ZWOASIControlType["COOLER_ON_OFF"], ZWOASIControlType.COOLER_ON_OFF
        )
        self.assertIs(
            ZWOASIControlType["MONOCHROME_BINNING"],
            ZWOASIControlType.MONOCHROME_BINNING,
        )
        self.assertIs(ZWOASIControlType["FAN_ON_OFF"], ZWOASIControlType.FAN_ON_OFF)
        self.assertIs(
            ZWOASIControlType["PATTERN_ADJUSTMENT"],
            ZWOASIControlType.PATTERN_ADJUSTMENT,
        )
        self.assertIs(
            ZWOASIControlType["ANTI_DEW_HEATER"], ZWOASIControlType.ANTI_DEW_HEATER
        )
        self.assertIs(
            ZWOASIControlType["FAN_SPEED_ADJUSTMENT"],
            ZWOASIControlType.FAN_SPEED_ADJUSTMENT,
        )
        self.assertIs(
            ZWOASIControlType["POWER_LED_BRIGHTNESS"],
            ZWOASIControlType.POWER_LED_BRIGHTNESS,
        )
        self.assertIs(
            ZWOASIControlType["USB_HUB_RESET"], ZWOASIControlType.USB_HUB_RESET
        )
        self.assertIs(
            ZWOASIControlType["GPS_SUPPORT_INDICATOR"],
            ZWOASIControlType.GPS_SUPPORT_INDICATOR,
        )
        self.assertIs(
            ZWOASIControlType["GPS_START_LINE_POSITION"],
            ZWOASIControlType.GPS_START_LINE_POSITION,
        )
        self.assertIs(
            ZWOASIControlType["GPS_END_LINE_POSITION"],
            ZWOASIControlType.GPS_END_LINE_POSITION,
        )
        self.assertIs(
            ZWOASIControlType["ROLLING_SHUTTER_INTERVAL"],
            ZWOASIControlType.ROLLING_SHUTTER_INTERVAL,
        )

    def test_enum_member_from_int(self):
        self.assertIs(ZWOASIControlType(0), ZWOASIControlType.GAIN)
        self.assertIs(ZWOASIControlType(1), ZWOASIControlType.EXPOSURE)
        self.assertIs(ZWOASIControlType(2), ZWOASIControlType.GAMMA)
        self.assertIs(ZWOASIControlType(3), ZWOASIControlType.WHITE_BALANCE_RED_CHANNEL)
        self.assertIs(
            ZWOASIControlType(4), ZWOASIControlType.WHITE_BALANCE_BLUE_CHANNEL
        )
        self.assertIs(ZWOASIControlType(5), ZWOASIControlType.OFFSET)
        self.assertIs(ZWOASIControlType(6), ZWOASIControlType.BANDWIDTH_OVERLOAD)
        self.assertIs(ZWOASIControlType(7), ZWOASIControlType.OVERCLOCK)
        self.assertIs(ZWOASIControlType(8), ZWOASIControlType.TEMPERATURE_READING)
        self.assertIs(ZWOASIControlType(9), ZWOASIControlType.IMAGE_FLIP)
        self.assertIs(ZWOASIControlType(10), ZWOASIControlType.AUTO_MAXIMUM_GAIN)
        self.assertIs(ZWOASIControlType(11), ZWOASIControlType.AUTO_MAXIMUM_EXPOSURE)
        self.assertIs(ZWOASIControlType(12), ZWOASIControlType.AUTO_TARGET_BRIGHTNESS)
        self.assertIs(ZWOASIControlType(13), ZWOASIControlType.HARDWARE_BINNING)
        self.assertIs(ZWOASIControlType(14), ZWOASIControlType.HIGH_SPEED_MODE)
        self.assertIs(ZWOASIControlType(15), ZWOASIControlType.COOLER_POWER_PERCENTAGE)
        self.assertIs(ZWOASIControlType(16), ZWOASIControlType.TARGET_TEMPERATURE)
        self.assertIs(ZWOASIControlType(17), ZWOASIControlType.COOLER_ON_OFF)
        self.assertIs(ZWOASIControlType(18), ZWOASIControlType.MONOCHROME_BINNING)
        self.assertIs(ZWOASIControlType(19), ZWOASIControlType.FAN_ON_OFF)
        self.assertIs(ZWOASIControlType(20), ZWOASIControlType.PATTERN_ADJUSTMENT)
        self.assertIs(ZWOASIControlType(21), ZWOASIControlType.ANTI_DEW_HEATER)
        self.assertIs(ZWOASIControlType(22), ZWOASIControlType.FAN_SPEED_ADJUSTMENT)
        self.assertIs(ZWOASIControlType(23), ZWOASIControlType.POWER_LED_BRIGHTNESS)
        self.assertIs(ZWOASIControlType(24), ZWOASIControlType.USB_HUB_RESET)
        self.assertIs(ZWOASIControlType(25), ZWOASIControlType.GPS_SUPPORT_INDICATOR)
        self.assertIs(ZWOASIControlType(26), ZWOASIControlType.GPS_START_LINE_POSITION)
        self.assertIs(ZWOASIControlType(27), ZWOASIControlType.GPS_END_LINE_POSITION)
        self.assertIs(ZWOASIControlType(28), ZWOASIControlType.ROLLING_SHUTTER_INTERVAL)


# **************************************************************************************


class TestASIExposureStatus(unittest.TestCase):
    def test_enum_values(self):
        self.assertEqual(ZWOASIExposureStatus.IDLE, 0)
        self.assertEqual(ZWOASIExposureStatus.WORKING, 1)
        self.assertEqual(ZWOASIExposureStatus.SUCCESS, 2)
        self.assertEqual(ZWOASIExposureStatus.FAILED, 3)

    def test_enum_member_by_name(self):
        self.assertIs(ZWOASIExposureStatus["IDLE"], ZWOASIExposureStatus.IDLE)
        self.assertIs(ZWOASIExposureStatus["WORKING"], ZWOASIExposureStatus.WORKING)
        self.assertIs(ZWOASIExposureStatus["SUCCESS"], ZWOASIExposureStatus.SUCCESS)
        self.assertIs(ZWOASIExposureStatus["FAILED"], ZWOASIExposureStatus.FAILED)

    def test_enum_member_from_int(self):
        self.assertIs(ZWOASIExposureStatus(0), ZWOASIExposureStatus.IDLE)
        self.assertIs(ZWOASIExposureStatus(1), ZWOASIExposureStatus.WORKING)
        self.assertIs(ZWOASIExposureStatus(2), ZWOASIExposureStatus.SUCCESS)
        self.assertIs(ZWOASIExposureStatus(3), ZWOASIExposureStatus.FAILED)


# **************************************************************************************
