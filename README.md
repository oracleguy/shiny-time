# Shiny Time
Digital clock and multi-mode countdown timer. Displays the current time or different countdown timers with web configuration.

# Buttons

There are two configurable buttons that when pressed will show the countdown in days to a specific date. There are two day countdown modes:
- Specific Day: A day that repeats once per year. ex. Birthday
- Specific Date: A specific day and year. ex: some special event

The modes and the dates are configurable in the web interface.

The day countdown timer should always show the whole day remaining. For example if the countdown was to December 25th, any time on December 24th, it would read "1".

# Time Countdown Timers

The time countdown timers are used to run shorter countdown timers. When a countdown timer is running, the device displays the time remaining instead of the current time. The countdown timers can be started via the web interface.

# Web Interface

The web interface displays what the device is currently displaying. This interface lets set certain options and start and stop timers.

# Hardware

The device is based on a Raspberry Pi Zero 2W.

## GPIO Expander

The buttons and their integrated lights will be connected to a GPIO epander. This expander is connected via the I2C bus and wires two interrupt pins to the Pi.

## Seven Segment Display

The seven segment display will be used to display the current time or the countdown timers. This display will be connected via the I2C bus.

## Web application architecture

The web interface will be generated as a mostly static site with Zola. It will
not initially use a full single-page application framework such as React or
Angular. A small amount of JavaScript can call the Python API and update the
dashboard, while keeping the interface lightweight for the Raspberry Pi Zero
2W.

The Python application uses Flask 3.1.3 and exposes the WSGI application
through the application factory `create_app`. The production server is
Waitress 3.0.2. The development server can be started with `make server`; the
production WSGI server can be started with `make production-server`.

The application factory accepts an optional device implementation:

```python
app = create_app(device_instance=fake_device)
```

This keeps hardware construction out of module import time and allows the web
application to be tested without Raspberry Pi hardware. In production,
`create_app()` constructs the real device when the application starts.

The API is organized around device state and user actions rather than direct
GPIO operations. Physical buttons and web requests should eventually use the
same application services and timer state machine. The initial endpoints are:

```text
GET /api/health   Basic service health check
GET /api/status   Current device status
```

Timer, configuration, and Wi-Fi setup endpoints will be added behind this
boundary. The frontend and API are intended to be served from the same origin,
so cross-origin configuration should not be necessary.

## HTTP and network security

The device will serve HTTP locally rather than requiring HTTPS certificates on
the Raspberry Pi. This applies to both the normal home-LAN interface and the
setup portal at `http://192.168.4.1`. The setup hotspot is isolated and the
setup authorization code is a physical-presence check, not high-security
authentication.

The device must not be exposed directly to the public Internet or through
router port forwarding. Users who need remote access or who are on an
untrusted network should provide the security boundary outside the device,
using a VPN or a reverse proxy that terminates HTTPS. The application should
never log Wi-Fi passwords.
