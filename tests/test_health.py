from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "code": "OK",
        "message": "Success",
        "data": {
            "status": "ok",
            "service": "API Sentinel AI",
            "version": "0.1.0",
        },
    }


def test_ping() -> None:
    response = client.get("/api/v1/ping")

    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "code": "OK",
        "message": "Success",
        "data": {"message": "pong"},
    }
