from sqlalchemy import Column, Integer, String
from app.db.session import Base

class FlightData(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    airline = Column(String, index=True)
    flight_number = Column(String)
    departure_date = Column(String)
    status = Column(String)
    origin = Column(String)
    destination = Column(String)
