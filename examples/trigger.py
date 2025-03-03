# **************************************************************************************

# @package        zwoasi
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from time import sleep

from zwo import (
    ZWOASICamera,
    ZWOASICameraParams,
    ZWOASITriggerOutput,
    get_all_connected_camera_ids,
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

    # Create a new camera parameters instance (for demonstration purposes we are
    # connecting to a ASI62000M Pro model) which has a pid of "" (empty string):
    params: ZWOASICameraParams = ZWOASICameraParams(pid="620b")

    # Create a new camera instance:
    zwo = ZWOASICamera(id, params)

    # Get the camera id (should be 0):
    cid = zwo.get_id()

    # Get the camera name:
    name = zwo.get_name()

    print(f"Camera ID: {cid}, Name: {name}")

    # Check if the camera is ready, if not return:
    if not zwo.is_ready():
        return

    zwo.set_soft_trigger_io_configuration(
        pin=ZWOASITriggerOutput.PINA,
        high=True,
        delay=100,
        duration=1000,
    )

    # Get the camera's triggering I/O configuration for Pin A:
    config = zwo.get_soft_trigger_io_configuration(pin=ZWOASITriggerOutput.PINA)

    # Send a software start trigger to the camera:
    zwo.send_soft_trigger(start=True)

    # Wait for 2 seconds:
    sleep(2)

    # Send a software stop trigger to the camera:
    zwo.send_soft_trigger(start=False)

    print(f"Camera Trigger I/O Configuration [Pin A]: {config}")

    zwo.set_soft_trigger_io_configuration(
        pin=ZWOASITriggerOutput.PINB,
        high=False,
        delay=100,
        duration=1000,
    )

    # Get the camera's triggering I/O configuration for Pin B:
    config = zwo.get_soft_trigger_io_configuration(pin=ZWOASITriggerOutput.PINB)

    print(f"Camera Trigger I/O Configuration [Pin B]: {config}")


# **************************************************************************************

if __name__ == "__main__":
    main()

# **************************************************************************************
