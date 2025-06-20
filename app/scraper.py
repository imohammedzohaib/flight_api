import requests
from bs4 import BeautifulSoup

def scrape_flight_data(airline_code, flight_number, departure_date):
    search_url = "https://www.flightstats.com/v2/flight-tracker/search"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Dummy data (replace with actual scraping logic)
    flight_info = {
        "airline_code": airline_code,
        "flight_number": flight_number,
        "departure_date": departure_date,
        "status": "Scheduled",
        "departure_time": "10:00 AM",
        "arrival_time": "1:00 PM"
    }

    return flight_info