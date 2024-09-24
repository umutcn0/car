from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.services.dynaconf import settings
from app.core.models.base import Base

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.db.user}:{settings.db.password}@{settings.db.host}:{settings.db.port}/{settings.db.db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


def init_db():
    # Tüm tanımlı modelleri veritabanında yaratma
    Base.metadata.create_all(engine)
