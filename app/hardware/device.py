
from hardware.i2c import get_i2c_bus, DISPLAY_ADDRESS
from adafruit_ht16k33.segments import BigSeg7x4
from hardware.gpio import gpio
from hardware.buttons import buttons
import board

class Device:
    """A class representing the hardware device for the clock."""

    def __init__(self):
        self.i2c = get_i2c_bus()
        self.display = BigSeg7x4(self.i2c, address=DISPLAY_ADDRESS)
        self.gpio = gpio(self.i2c)
        self.buttons = buttons(self.gpio)

    def __repr__(self):
        return f"Device(i2c={self.i2c}, display={self.display}, gpio={self.gpio})>"

    def get_board_id(self) -> str | None:
        """Get the board ID from the device."""
        return board.board_id

    def set_display_value(self, value: str):
        """Set the display value on the device."""
        self.display.print(value)
        return

    def set_display_brightness(self, brightness: int):
        """Set the display brightness on the device."""
        self.display.brightness = brightness
        return


device = Device()