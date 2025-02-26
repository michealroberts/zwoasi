# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from pathlib import Path
from platform import machine, system

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

    # If we are on MacOS (e.g., darwin) then we can can look for mac:
    arch: str = (
        "mac"
        if sys.lower() == "darwin"
        else ARCHITECTURE_MAP.get(architecture, architecture)
    )

    # Direct to the dylib if the system is MacOS (e.g., darwin), otherwise default to .so:
    filename = "libASICamera2.dylib" if sys.lower() == "darwin" else "libASICamera2.so"

    # Build the SDK library path using pathlib's '/' operator:
    sdk_path: Path = (
        Path(BASE_DIR) / "sdk" / version.replace(".", "") / "lib" / arch / filename
    )

    # Verify that the sdk_location exists before proceeding:
    if not sdk_path.exists():
        raise FileNotFoundError(f"SDK library not found at: {sdk_path}")

    # Return the base sdk_path relative to where it is needed:
    return Path(sdk_path)


# **************************************************************************************
