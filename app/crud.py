from app import models
from sqlalchemy.orm import Session
from app.schemas import FlightCreate

def create_flight(db: Session, flight: FlightCreate):
    db_flight = models.Flight(**flight.dict())
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight