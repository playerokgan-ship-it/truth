from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_sum_ok():
    r = client.get("/sum?a=2&b=3")
    assert r.status_code == 200
    assert r.json() == {"result": 5}

def test_sum_validation_error():
    r = client.get("/sum?a=aaa&b=3")
    assert r.status_code == 422  # FastAPI/Pydantic validation error
