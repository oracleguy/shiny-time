
from hardware.i2c import get_i2c_bus, DISPLAY_ADDRESS, GPIO_ADDRESS
from adafruit_ht16k33.segments import BigSeg7x4

class Device:
    """A class representing the hardware device for the clock."""

    def __init__(self):
        self.i2c = get_i2c_bus()
        self.display = BigSeg7x4(self.i2c, address=DISPLAY_ADDRESS)

    def __repr__(self):
        return f"Device(i2c={self.i2c}, display={self.display})>"

    def set_display_value(self, value: str):
        """Set the display value on the device."""
        self.display.print(value)
        return

    def set_display_brightness(self, brightness: int):
        """Set the display brightness on the device."""
        self.display.brightness = brightness
        return


device = Device()