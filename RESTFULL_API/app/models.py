from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String, unique=True, index=True)

    elements = relationship("ElementData", back_populates="device")


class ElementData(Base):
    __tablename__ = "elements"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    average_before = Column(Float)
    average_after = Column(Float)
    data_size = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    device = relationship("Device", back_populates="elements")

