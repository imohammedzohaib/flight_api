from app.core.celery_utils import celery_app
from app.services.scraper import scrape_flight_data
from app.db.session import SessionLocal
from app.models.flight import FlightData
from app.cache.redis_cache import set_cached_flight_data

@celery_app.task
def fetch_and_store_flight_info(airline_code, flight_number, departure_date):
    db = SessionLocal()
    data = scrape_flight_data(airline_code, flight_number, departure_date)
    flight = FlightData(**data)
    db.add(flight)
    db.commit()
    set_cached_flight_data(f"{airline_code}-{flight_number}-{departure_date}", data)
