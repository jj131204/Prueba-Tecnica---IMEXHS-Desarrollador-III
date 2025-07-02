from fastapi import FastAPI
from .database import engine, Base
from .routers import elements

app = FastAPI(
    title="Sensor Data API",
    description="API para recibir y analizar datos de sensores con PostgreSQL.",
    version="1.0.0"
)

# Crear las tablas si no existen (puedes reemplazar esto con Alembic en proyectos grandes)
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(elements.router)
