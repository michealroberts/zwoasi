# **************************************************************************************

# @package        zwo
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from zwo import (
    ZWOASI_VENDOR_ID,
    ZWOASICamera,
    ZWOASICameraParams,
    get_all_connected_camera_ids,
    is_connected,
)

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

    # Create a new camera parameters instance (for demonstration purposes we are
    # connecting to a ASI62000M Pro model) which has a pid of "" (empty string):
    params: ZWOASICameraParams = ZWOASICameraParams(pid="620b")

    # Create a new camera instance:
    zwo = ZWOASICamera(id, params)

    # Get the camera id (should be 0):
    cid = zwo.get_id()

    # Get the camera name:
    name = zwo.get_name()

    # Disconnect from the camera:
    zwo.disconnect()

    print(f"Camera ID: {cid}, Name: {name} Disconnected Successfully")


# **************************************************************************************

if __name__ == "__main__":
    main()

# **************************************************************************************
