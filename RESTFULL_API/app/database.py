from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cambia estos valores por los tuyos
DB_USER = "postgres"
DB_PASSWORD = "admin123"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "sensor_db"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
