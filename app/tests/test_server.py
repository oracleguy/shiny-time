from server import create_app


class FakeDevice:
    def get_board_id(self):
        return "test-board"


def test_create_app_accepts_an_injected_device():
    app = create_app(device_instance=FakeDevice())

    response = app.test_client().get("/api/status")

    assert response.status_code == 200
    assert response.json == {"board_id": "test-board"}


def test_health_endpoint():
    app = create_app(device_instance=FakeDevice())

    response = app.test_client().get("/api/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}
