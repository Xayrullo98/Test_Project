from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, Boolean, DateTime, func
from sqlalchemy_utils import URLType

from db import Base
from models.base import BaseModel


class Meals(Base):
    __tablename__ = "Meals"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    type = Column(Integer,ForeignKey("Menu.id"), nullable=False)
    price = Column(Float(30), nullable=False)
    image_url = Column(URLType, nullable=True)
    active = Column(Boolean, default=True, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())

