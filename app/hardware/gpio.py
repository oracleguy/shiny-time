from adafruit_mcp230xx.mcp23017 import MCP23017
from hardware.i2c import GPIO_ADDRESS
import digitalio
import busio

class gpio:
    """A class representing the GPIO expander on the I2C bus."""

    def __init__(self, i2c: busio.I2C):
        self.mcp = MCP23017(i2c, address=GPIO_ADDRESS)
        self.pin_directions: dict[int, str] = {}

    def setup_pins(self, pin_numbers: list[int], direction: str):
        """Set up the specified pins as input or output."""
        if direction not in ("input", "output"):
            raise ValueError("Direction must be 'input' or 'output'.")

        for pin_number in pin_numbers:
            configured_direction = self.pin_directions.get(pin_number)
            if configured_direction is not None and configured_direction != direction:
                raise ValueError(
                    f"Pin {pin_number} is already configured as {configured_direction}."
                )

        for pin_number in pin_numbers:
            if pin_number in self.pin_directions:
                continue
            pin = self.mcp.get_pin(pin_number)
            if direction == "input":
                pin.switch_to_input(Pull = digitalio.Pull.UP)
            elif direction == "output":
                pin.switch_to_output()
            self.pin_directions[pin_number] = direction

    def read_pin(self, pin_number: int) -> bool:
        """Read the value of the specified pin."""
        pin = self.mcp.get_pin(pin_number)
        return pin.value

    def write_pin(self, pin_number: int, value: bool):
        """Write a value to the specified pin."""
        pin = self.mcp.get_pin(pin_number)
        pin.value = value

    