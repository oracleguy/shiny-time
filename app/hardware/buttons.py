from hardware.gpio import gpio

BUTTON_COUNT = 4

class buttons:
    """A class representing the buttons on the hardware device."""

    def __init__(self, gpio: gpio):
        self.gpio = gpio
        self.button_states = [False] * BUTTON_COUNT
        self.lamp_states = [False] * BUTTON_COUNT

    def read_buttons(self) -> list[bool]:
        """Read the current state of the buttons."""
        for i in range(BUTTON_COUNT):
            self.button_states[i] = self.gpio.read_pin(i)
        return self.button_states

    def setup_buttons(self):
        """Set up the buttons as input pins."""
        self.gpio.setup_pins(list(range(BUTTON_COUNT)), "input")
        self.gpio.setup_pins(list(range(BUTTON_COUNT - 1, BUTTON_COUNT * 2)), "output")

    def set_lamp_state(self, button_index: int, state: bool):
        """Set the state of the lamp associated with a button."""
        if 0 <= button_index < BUTTON_COUNT:
            self.lamp_states[button_index] = state
            self.gpio.write_pin(button_index + BUTTON_COUNT, state)
        else:
            raise IndexError("Button index out of range.")

    def get_lamp_states(self) -> list[bool]:
        """Get the current state of the lamps."""
        return self.lamp_states
    