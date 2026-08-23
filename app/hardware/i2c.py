import board
import busio

DISPLAY_ADDRESS = 0x70
GPIO_ADDRESS = 0x40

def get_i2c_bus() -> busio.I2C:
    """Get the I2C bus for the current platform."""
    return busio.I2C(board.SCL, board.SDA)