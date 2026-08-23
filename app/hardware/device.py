
from hardware.i2c import get_i2c_bus

class Device:
    """A class representing a hardware device."""

    def __init__(self):
        self.i2c = get_i2c_bus()

    def __repr__(self):
        return f"Device(i2c={self.i2c})>"


device = Device()