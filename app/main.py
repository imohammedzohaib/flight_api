from fastapi import FastAPI, Query
from app.scraper import scrape_flight_data
from app.database import SessionLocal, engine
from app import models, crud
from app.schemas import FlightCreate, FlightResponse
from app.celery_worker import background_scrape_task
from app.cache import get_cached_flight, set_cached_flight

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/flight", response_model=FlightResponse)
def get_flight(
    airline_code: str = Query(...),
    flight_number: str = Query(...),
    departure_date: str = Query(...)
):
    cache_key = f"{airline_code}_{flight_number}_{departure_date}"
    cached_data = get_cached_flight(cache_key)

    if cached_data:
        return cached_data

    db = SessionLocal()
    flight_data = scrape_flight_data(airline_code, flight_number, departure_date)

    if not flight_data:
        return {"message": "No data found"}

    flight_obj = crud.create_flight(db, FlightCreate(**flight_data))
    db.close()

    set_cached_flight(cache_key, flight_obj.__dict__)
    background_scrape_task.delay(airline_code, flight_number, departure_date)

    return flight_obj