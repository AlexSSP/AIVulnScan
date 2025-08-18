from fastapi.testclient import TestClient
from app.main import app
from test_helpers import get_test_config
import time

client = TestClient(app)

def test_scan_endpoint(auth_client):
    terraform_config = get_test_config("terraform")
    response = auth_client.post("/api/v1/scan", json={
        "config": terraform_config,
        "config_type": "terraform"
    })
    assert response.status_code == 200
    results = response.json()["vulnerabilities"]
    assert isinstance(results, list)
    assert len(results) > 0


def test_async_scan(auth_client):
    k8s_config = get_test_config("kubernetes")
    response = auth_client.post("/api/v1/scan/async", json={
        "config": k8s_config,
        "config_type": "kubernetes"
    })
    assert response.status_code == 202
    task_id = response.json()["task_id"]

    time.sleep(1)
    status_response = auth_client.get(f"/api/v1/admin/task/{task_id}")
    assert status_response.status_code == 200

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