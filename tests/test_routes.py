from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_flight_info():
    response = client.get("/flight-info?airline_code=AA&flight_number=100&departure_date=2025-06-25")
    assert response.status_code == 200
