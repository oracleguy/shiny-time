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
