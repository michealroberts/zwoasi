# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from pathlib import Path
from platform import machine, system
from typing import Optional

# **************************************************************************************


def find_asi_library_parent_directory(start: Path, where: str = "sdk") -> Path:
    """
    Walk up the directory tree from `start` until a directory containing a 'sdk'
    subdirectory is found. If no such directory is found, raise an error.
    """
    current = start.resolve()

    while current != current.parent:
        if (current / where).is_dir():
            return current

        current = current.parent

    raise RuntimeError("Could not find a directory containing 'sdk'")


# **************************************************************************************


def get_asi_libary_path(version: str) -> Path:
    """
    Get the absolute path to the ZWO ASI SDK library for the current system architecture.

    Returns:
        Path: The path to the ZWO ASI SDK library file.

    Raises:
        FileNotFoundError: If the SDK library file does not exist at the expected location.
    """
    # Get the base directory by walking until we find the SDK directory:
    BASE_DIR: Path = find_asi_library_parent_directory(Path(__file__), where="sdk")

    # e.g., the system/OS name, e.g. 'Linux', 'Windows' or 'Darwin':
    sys: str = system()

    # e.g., the system architecture, e.g., "x86_64", "arm64" etc:
    architecture: str = machine()

    # Compile a list of archiectures to our driver supported architecture value:
    ARCHITECTURE_MAP = {
        # 64-bit Intel/AMD architectures:
        "x64": "x64",
        "x86_64": "x64",
        "amd64": "x64",
        "x86-64": "x64",
        # 32-bit Intel architectures:
        "i386": "x86",
        "i686": "x86",
        "x86": "x86",
        # ARM architectures:
        "armv6": "armv6",
        "armv6l": "armv6",
        "armv7": "armv7",
        "armv7l": "armv7",
        "armv8": "armv8",
        "aarch64": "armv8",
        "arm64": "armv8",
    }

    # Are we running on an ARM Mac?
    is_arm_mac: bool = sys.lower() == "darwin" and architecture.startswith("arm")

    # Unfortunately, the ZWO ASI SDK does not support ARM Macs (yet):
    if is_arm_mac:
        raise NotImplementedError(
            "ARM Macs are not yet supported by the underlying ZWO ASI SDK."
        )

    # Are we running on an older Intel Mac?
    is_darwin_mac: bool = sys.lower() == "darwin" and not is_arm_mac

    # Are we running on Windows?
    is_windows: bool = sys.lower() == "windows"

    # If we are on MacOS (e.g., darwin) then we can can look for mac:
    arch: str = (
        "mac" if is_darwin_mac else ARCHITECTURE_MAP.get(architecture, architecture)
    )

    # Direct to the dylib if the system is MacOS (e.g., darwin), otherwise default to .so:
    filename = (
        "libASICamera2.dll"
        if is_windows
        else "libASICamera2.dylib"
        if is_darwin_mac
        else "libASICamera2.so"
    )

    # Build the SDK library path using pathlib's '/' operator:
    sdk_path: Path = (
        Path(BASE_DIR)
        / "sdk"
        / "asi"
        / version.replace(".", "")
        / "lib"
        / arch
        / filename
    )

    # Verify that the sdk_location exists before proceeding:
    if not sdk_path.exists():
        raise FileNotFoundError(f"SDK library not found at: {sdk_path}")

    # Return the base sdk_path relative to where it is needed:
    return Path(sdk_path)


# **************************************************************************************


def is_hexadecimal(value: Optional[str]) -> bool:
    if not value:
        return False

    # Try converting value to an integer using base 16:
    try:
        int(value, 16)
        return True
    except ValueError:
        return False


# **************************************************************************************
