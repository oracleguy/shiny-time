import sys
import types
from unittest.mock import Mock

import pytest


# Keep GPIO tests runnable on development machines without the Raspberry Pi hardware.
mcp_module = types.ModuleType("adafruit_mcp230xx.mcp23017")
mcp_module.MCP23017 = object
mcp_package = types.ModuleType("adafruit_mcp230xx")
mcp_package.__path__ = []
sys.modules["adafruit_mcp230xx"] = mcp_package
sys.modules["adafruit_mcp230xx.mcp23017"] = mcp_module
sys.modules["hardware.i2c"] = types.SimpleNamespace(GPIO_ADDRESS=0x40)
sys.modules["digitalio"] = types.SimpleNamespace(
    Pull=types.SimpleNamespace(UP=object())
)
sys.modules["busio"] = types.ModuleType("busio")

from hardware import gpio as gpio_module


@pytest.fixture
def gpio_setup(monkeypatch):
    mcp = Mock()
    monkeypatch.setattr(gpio_module, "MCP23017", Mock(return_value=mcp))
    pins = {number: Mock() for number in (1, 2)}
    mcp.get_pin.side_effect = pins.__getitem__
    return gpio_module.gpio(Mock()), mcp, pins


def test_repeated_input_setup_is_idempotent(gpio_setup):
    gpio, _, pins = gpio_setup

    gpio.setup_pins([1], "input")
    gpio.setup_pins([1], "input")

    pins[1].switch_to_input.assert_called_once()
    assert gpio.pin_directions[1] == "input"


def test_repeated_output_setup_is_idempotent(gpio_setup):
    gpio, _, pins = gpio_setup

    gpio.setup_pins([1], "output")
    gpio.setup_pins([1], "output")

    pins[1].switch_to_output.assert_called_once()
    assert gpio.pin_directions[1] == "output"


def test_changing_pin_direction_raises(gpio_setup):
    gpio, _, pins = gpio_setup
    gpio.setup_pins([1], "input")

    with pytest.raises(ValueError, match="already configured as input"):
        gpio.setup_pins([1], "output")

    pins[1].switch_to_input.assert_called_once()
    pins[1].switch_to_output.assert_not_called()


def test_invalid_direction_raises_before_touching_pins(gpio_setup):
    gpio, mcp, _ = gpio_setup

    with pytest.raises(ValueError, match="Direction must be"):
        gpio.setup_pins([1], "invalid")

    mcp.get_pin.assert_not_called()
    assert gpio.pin_directions == {}


def test_conflicting_batch_does_not_configure_other_pins(gpio_setup):
    gpio, _, pins = gpio_setup
    gpio.setup_pins([1], "input")
    gpio.setup_pins([2], "output")
    output_calls = pins[2].switch_to_output.call_count

    with pytest.raises(ValueError, match="already configured as input"):
        gpio.setup_pins([2, 1], "output")

    assert pins[2].switch_to_output.call_count == output_calls
