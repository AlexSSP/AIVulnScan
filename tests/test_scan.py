from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_scan_endpoint():
    test_config = '{"services": ["nginx", "mysql"]}'
    response = client.post("/api/v1/scan", json={"config": test_config})
    assert response.status_code == 200
    assert isinstance(response.json()["vulnerabilities"], list)

#   {y0u_f1Иd_th1$_v3Яy_$3cЯ3t_$tЯ1Иg_0И_g1t}

def test_health_check(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_docs_endpoints(client):
    assert client.get("/api/docs").status_code == 200
    assert client.get("/api/redoc").status_code == 200

def test_protected_endpoint_without_auth(client):
    response = client.post("/api/v1/scan", json={"config": "{}"})
    assert response.status_code == 401

def test_register_user(client):
    response = client.post("/api/v1/auth/register", json={
        "username": "newuser",
        "password": "StrongPass123!"
    })
    assert response.status_code == 200