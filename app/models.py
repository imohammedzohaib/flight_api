from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    airline_code = Column(String)
    flight_number = Column(String)
    departure_date = Column(String)
    status = Column(String)
    departure_time = Column(String)
    arrival_time = Column(String)