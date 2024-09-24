import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field


class CarSchema(BaseModel):
    year: Optional[int] = Field(default=None)
    make: Optional[str] = Field(default=None)
    model: Optional[str] = Field(default=None)
    trim: Optional[str] = Field(default=None)
    body: Optional[str] = Field(default=None)
    transmission: Optional[str] = Field(default=None)
    state: Optional[str] = Field(default=None)
    condition: Optional[str] = Field(default=None)
    odometer: Optional[int] = Field(default=None)
    color: Optional[str] = Field(default=None)
    interior: Optional[str] = Field(default=None)
    price: Optional[float] = Field(default=None)

    def to_dict(self) -> dict:
        return {
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
