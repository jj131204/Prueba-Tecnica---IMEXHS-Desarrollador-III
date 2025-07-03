from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, crud, models
from ..database import SessionLocal

router = APIRouter(
    prefix="/api/elements",
    tags=["elements"]
)

# Dependency para obtener la sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Crear un nuevo dispositivo
@router.post("/device/", response_model=schemas.Device)
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    return crud.create_device(db, device)


# Crear un nuevo elemento de datos
@router.post("/", response_model=schemas.ElementData)
def create_element(element: schemas.ElementDataCreate, db: Session = Depends(get_db)):
    return crud.create_element_data(db, element)


# Obtener todos los elementos con filtros opcionales
@router.get("/", response_model=List[schemas.ElementData])
def get_elements(
    db: Session = Depends(get_db),
    created_date: Optional[str] = Query(None),
    average_before: Optional[float] = Query(None),
    average_after: Optional[float] = Query(None),
    data_size: Optional[int] = Query(None)
):
    query = db.query(models.ElementData)

    if created_date:
        query = query.filter(models.ElementData.created_date >= created_date)
    if average_before is not None:
        query = query.filter(models.ElementData.average_before > average_before)
    if average_after is not None:
        query = query.filter(models.ElementData.average_after < average_after)
    if data_size is not None:
        query = query.filter(models.ElementData.data_size == data_size)

    return query.all()


# Obtener un solo elemento por ID
@router.get("/{element_id}", response_model=schemas.ElementData)
def get_element(element_id: int, db: Session = Depends(get_db)):
    result = crud.get_element_by_id(db, element_id)
    if not result:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    return result


# Actualizar nombre del dispositivo
@router.put("/device/{device_id}", response_model=schemas.Device)
def update_device(device_id: int, name_update: schemas.DeviceCreate, db: Session = Depends(get_db)):
    updated = crud.update_device_name(db, device_id, name_update.device_name)
    if not updated:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return updated


# Eliminar un elemento por ID
@router.delete("/{element_id}")
def delete_element(element_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_element(db, element_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    return {"message": f"Elemento {element_id} eliminado correctamente"}
