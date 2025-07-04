from sqlalchemy.orm import Session
from datetime import datetime
from . import models, schemas


def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(device_name=device.device_name)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device    


def create_element_data(db: Session, element: schemas.ElementDataCreate):
    data = element.data
    avg_before = sum(data) / len(data)
    max_val = max(data)
    normalized_data = [x / max_val for x in data] if max_val != 0 else data
    avg_after = sum(normalized_data) / len(normalized_data)

    db_element = models.ElementData(
        device_id=element.device_id,
        average_before=avg_before,
        average_after=avg_after,
        data_size=len(data),
        created_date=datetime.utcnow(),
        updated_date=datetime.utcnow(),
        
    )
    db.add(db_element)
    db.commit()
    db.refresh(db_element)
    return db_element





def get_elements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ElementData).offset(skip).limit(limit).all()


def get_element_by_id(db: Session, element_id: int):
    return db.query(models.ElementData).filter(models.ElementData.id == element_id).first()


def update_device_name(db: Session, device_id: int, new_name: str):
    device = db.query(models.Device).filter(models.Device.id == device_id).first()
    if device:
        device.device_name = new_name
        db.commit()
        db.refresh(device)
    return device


def delete_element(db: Session, element_id: int):
    element = db.query(models.ElementData).filter(models.ElementData.id == element_id).first()
    if element:
        db.delete(element)
        db.commit()
    return element
