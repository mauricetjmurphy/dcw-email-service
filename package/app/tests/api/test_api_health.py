from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.main import api_router 
from app.main import app

app.include_router(api_router)

# Create a TestClient for the app
client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
