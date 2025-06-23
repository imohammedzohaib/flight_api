import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException

def scrape_flight_data(airline_code: str, flight_number: str, departure_date: str) -> dict:
    url = "https://www.flightstats.com/v2/flight-tracker/search"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        return {
            "airline": airline_code,
            "flight_number": flight_number,
            "departure_date": departure_date,
            "status": "On Time",  # Simulated
            "origin": "JFK",
            "destination": "LAX"
        }
    except Exception:
        raise HTTPException(status_code=500, detail="Flight data extraction failed")
