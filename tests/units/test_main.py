from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_server_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK", "message": "Server is up and running."}
