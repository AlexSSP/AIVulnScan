from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_scan_endpoint():
    test_config = '{"services": ["nginx", "mysql"]}'
    response = client.post("/api/v1/scan", json={"config": test_config})
    assert response.status_code == 200
    assert isinstance(response.json()["vulnerabilities"], list)