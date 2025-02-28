# zwoasi

Modern, type-safe, zero-dependency Python library for controlling ZWO ASI astronomical cameras.

## Installation

```bash
pip install zwo
```

or

using your preferred environment / package manager of choice, e.g., `poetry`, `conda` or `uv`:

```bash
poetry add zwo
```

```bash
conda install zwo
```

```bash
uv add zwo
```

## Linux Setup

To check if you any ZWO ASI cameras connected, run the following command:

```bash
lsusb | grep 03c3
```

You should see something like this as your output:

```bash
Bus 001 Device 016: ID 03c3:620b ZWO ASI6200MM Pro
```

To allow non-root users to access the ASI camera, you need to create a udev rule. The following command will copy the rule to the correct location:

```bash
sudo install /zwoasi/sdk/137/lib/asi.rules /lib/udev/asi-rules.d
```

```bash
sudo udevadm control --reload-rules && udevadm trigger
```

Once you have done this, check that the camera is accessible by running the following command:

```bash
ls -l /dev/bus/usb/$(lsusb | grep 03c3:620b | awk '{print $2}')/$(lsusb | grep 03c3:620b | awk '{print $4}' | tr -d :)
```

You should see something like this:

```bash
crw-rw-rw- 1 root root 189, 0 Jan  1 00:00 /dev/bus/usb/001/001
```

i.e., the camera is accessible by all users with permissions `crw-rw-rw-` with a mode of `MODE=0666`.

Then when you have verified these steps, run the following command:

```bash
cat /sys/module/usbcore/parameters/usbfs_memory_mb
```

If the output is anything other than `200`, something has gone wrong. To fix, simply follow the steps above again.

Once you have verified that the camera is accessible, if you reconnect the camera by unplugging it from the UBS port and plugging it back in, you can now use the `zwo` library to control the camera.

## Windows Setup

Unfortunately, ZWO ASI does not directly support .dll files for Windows. However, you can use the `zwo` library on Windows by using the Windows Subsystem for Linux (WSL) and following the Linux setup instructions above and passing through USB devices to the WSL from your host machine.

## Usage

```python
from zwo import import ZWOASICamera, ZWOASICameraParams

# Let's assume the camera ID is 0 (e.g., only 1 camera is connected):
id = 0

# Create a new camera parameters instance (for demonstration purposes we are
# connecting to a ASI62000M Pro model) which has a pid of "620b":
# N.B. Replace the pid with the correct one for your camera model.
pid: str = "620b"

params: ZWOASICameraParams = ZWOASICameraParams(pid=pid)

# Create a new camera instance:
zwo = ZWOASICamera(id, params)

# Check if the camera is ready:
is_ready = zwo.is_ready()

if not is_ready:
    print("Camera is not ready!")
    exit(1)
```

As the zwo instance is fully typed, you can use your IDE's autocompletion to see all the available methods and properties.

We have also provided further usage examples in the [examples](./examples) directory.

---

### License

This project is licensed under the terms of the MIT license.

Pulse Streamer