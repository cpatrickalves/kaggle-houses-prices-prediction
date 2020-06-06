from starlette.testclient import TestClient
from api import app

client = TestClient(app)

def test_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_status_response():
    response = client.get("/")
    assert response.json() == {"status": "online"}

