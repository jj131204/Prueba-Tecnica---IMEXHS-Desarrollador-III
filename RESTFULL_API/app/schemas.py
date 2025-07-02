from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime


class DeviceBase(BaseModel):
    device_name: str


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    id: int

    class Config:
        orm_mode = True


class ElementDataBase(BaseModel):
    device_id: int
    data: List[float] = Field(..., example=[1.0, 2.5, 3.3])

    @validator("data")
    def validate_all_numbers(cls, value):
        if not all(isinstance(v, (int, float)) for v in value):
            raise ValueError("Todos los elementos de 'data' deben ser números.")
        if len(value) == 0:
            raise ValueError("La lista 'data' no puede estar vacía.")
        return value


class ElementDataCreate(ElementDataBase):
    pass


class ElementData(ElementDataBase):
    id: int
    average_before: float
    average_after: float
    data_size: int
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True
