# 4番目に作成

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from .database import Base

class LocationDB(Base):
    __tablename__ = "locations_db"
    location_id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String, index=True)

class TravelDB(Base):
    __tablename__ = "travels_db"
    travel_id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations_db.location_id", ondelete="SET NULL"), nullable=False)
    departure_month = Column(Integer)
    days = Column(Integer)