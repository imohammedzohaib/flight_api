from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.cache.redis_cache import get_cached_flight_data
from app.tasks.background import fetch_and_store_flight_info

router = APIRouter()

@router.get("/flight-info")
async def get_flight_info(
    airline_code: str,
    flight_number: str,
    departure_date: str,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    cache_key = f"{airline_code}-{flight_number}-{departure_date}"
    cached_data = get_cached_flight_data(cache_key)
    
    if cached_data:
        return cached_data

    background_tasks.add_task(fetch_and_store_flight_info, airline_code, flight_number, departure_date)
    return {"message": "Processing. Data will be available soon."}
