![pypi](https://img.shields.io/pypi/v/zwo.svg)
![versions](https://img.shields.io/pypi/pyversions/zwo.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![zwoasi/test](https://github.com/michealroberts/zwoasi/actions/workflows/test.yml/badge.svg)](https://github.com/michealroberts/zwoasi/actions/workflows/test.yml)

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

N.B. The `03c3` is the vendor ID for ZWO.

You should see something like this as your output:

```bash
Bus 001 Device 016: ID 03c3:620b ZWO ASI6200MM Pro
```

To allow non-root users to access the ASI camera, you need to create a udev rule. Firstly, create the .rules file:

```bash
cat <<EOF > asi.rules
ACTION=="add", ATTR{idVendor}=="03c3", RUN+="/bin/sh -c '/bin/echo 200 >/sys/module/usbcore/parameters/usbfs_memory_mb'"
SUBSYSTEMS=="usb", ATTR{idVendor}=="03c3", MODE="0666"
EOF
```

The following command will copy the rule to the correct location:

```bash
sudo install asi.rules /lib/udev/rules.d
```

```bash
sudo udevadm control --reload-rules && sudo udevadm trigger
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

## MacOS Setup

There is no additional setup required for MacOS.

## Windows Setup

There is no additional setup required for Windows.

## Usage

```python
from zwo import ZWOASICamera, ZWOASICameraParams

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

## Milestones

- [X] Type-safe modern 3.6+ Python
- [X] Portable .h, .so and .dylib files for Linux and MacOS
- [ ] Portable .dll files for Windows
- [X] Fully unit tested
- [X] Simpler API (modelled around the ASCOM Alpaca API)
- [X] Integration testing with HIL testing (hardware-in-the-loop)
- [X] Zero-external dependencies (no numpy, astropy etc for portability)
- [X] Example API usage
- [X] Fully supported ZWO ASI Camera operations
- [ ] Fully supported ZWO Electronic Automatic Focuser operations
- [ ] Fully supported ZWO Filter Wheel operations
- [X] Fully seasoned recipes for usage with numpy, astropy et al.
- [ ] ASCOM Alpaca APIs w/Fast API

---

### Miscellaneous

For more information on the ZWO ASI SDK, please visit the [ZWO ASI SDK](https://www.zwoastro.com/software/) website.

### Disclaimer

This project is not affiliated with ZWO ASI in any way. It is a community-driven project. All trademarks and logos are the property of their respective owners. The ZWO ASI SDK is the property of ZWO ASI.

### License

This project is licensed under the terms of the MIT license.