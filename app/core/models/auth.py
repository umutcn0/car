import datetime
from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Float,
    Integer,
    String,
    ForeignKey,
    DateTime,
)
from .base import Base


class Auth(Base):
    __tablename__ = "auth"

    id = Column(Integer, primary_key=True, index=True)
    date: datetime.datetime = Column(
        Date, default=datetime.datetime.now(), nullable=True
    )
    token: str = Column(String, nullable=False)
    expire_time: datetime.datetime = Column(DateTime, nullable=False)
