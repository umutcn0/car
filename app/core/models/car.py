import datetime
from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Float,
    Integer,
    String,
    Index,
)
from .base import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    date: datetime.datetime = Column(
        Date, default=datetime.datetime.now(), nullable=True
    )
    year: int = Column(Integer, nullable=True, index=True)
    make: str = Column(String, nullable=True, index=True)
    model: str = Column(String, nullable=True, index=True)
    trim: str = Column(String, nullable=True, index=True)
    body: str = Column(String, nullable=True)
    transmission: str = Column(String, nullable=True)
    state: str = Column(String, nullable=True, index=True)
    condition: str = Column(String, nullable=True)
    odometer: int = Column(Integer, nullable=True)
    color: str = Column(String, nullable=True)
    interior: str = Column(String, nullable=True)
    price: float = Column(Float, nullable=True)

    def to_dict(self) -> dict:
        return {
            "date": self.date,
            "year": self.year,
            "make": self.make,
            "model": self.model,
            "trim": self.trim,
            "body": self.body,
            "transmission": self.transmission,
            "state": self.state,
            "condition": self.condition,
            "odometer": self.odometer,
            "color": self.color,
            "interior": self.interior,
            "price": self.price,
        }
