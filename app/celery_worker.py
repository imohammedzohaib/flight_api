from celery import Celery

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def background_scrape_task(airline_code, flight_number, departure_date):
    from app.scraper import scrape_flight_data
    from app.database import SessionLocal
    from app.schemas import FlightCreate
    from app.crud import create_flight

    db = SessionLocal()
    flight_data = scrape_flight_data(airline_code, flight_number, departure_date)
    if flight_data:
        create_flight(db, FlightCreate(**flight_data))
    db.close()