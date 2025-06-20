from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_flight_fetch():
    response = client.get("/flight", params={
        "airline_code": "AA",
        "flight_number": "100",
        "departure_date": "2025-06-20"
    })
    assert response.status_code == 200
    assert "flight_number" in response.json()