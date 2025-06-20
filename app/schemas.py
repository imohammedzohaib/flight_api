from pydantic import BaseModel

class FlightCreate(BaseModel):
    airline_code: str
    flight_number: str
    departure_date: str
    status: str
    departure_time: str
    arrival_time: str

class FlightResponse(FlightCreate):
    id: int