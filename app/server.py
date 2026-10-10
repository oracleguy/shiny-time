from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flask import Flask, jsonify

if TYPE_CHECKING:
    from hardware.device import Device


def create_app(device_instance: Device | None = None) -> Flask:
    """Create the web application with an injectable device implementation."""
    if device_instance is None:
        from hardware.device import Device

    app = Flask(__name__)
    app.config["DEVICE"] = device_instance if device_instance is not None else Device()

    @app.get("/api/health")
    def health() -> Any:
        return jsonify({"status": "ok"})

    @app.get("/api/status")
    def status() -> Any:
        device = app.config["DEVICE"]
        return jsonify({"board_id": device.get_board_id()})

    return app


def main(argv: list[str] | None = None) -> int:
    """Run the development server when invoked directly."""
    create_app().run(host="0.0.0.0", port=5000)
    return 0

if __name__ == "__main__":
    raise(SystemExit(main()))
