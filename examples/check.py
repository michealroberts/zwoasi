# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from zwo import ZWOASI_VENDOR_ID, get_all_connected_camera_ids, is_connected

# **************************************************************************************


def main() -> None:
    # Get all connected camera IDs:
    ids = get_all_connected_camera_ids()

    print(f"Connected Camera IDs: {ids}")

    # Let's assume the camera ID is 0 (e.g., only 1 camera is connected):
    id = 0

    if id not in ids:
        print(f"Camera ID {id} not found in connected camera IDs: {ids}")
        return

    connected = is_connected(vid=ZWOASI_VENDOR_ID, pid="620b")

    print(f"Camera Is Connected: {connected}")


# **************************************************************************************

if __name__ == "__main__":
    main()

# **************************************************************************************
