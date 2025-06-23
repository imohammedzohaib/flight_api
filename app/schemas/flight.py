from pydantic import BaseModel

class FlightDataSchema(BaseModel):
    airline: str
    flight_number: str
    departure_date: str
    status: str
    origin: str
    destination: str

    class Config:
        orm_mode = True
