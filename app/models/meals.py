from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, DateTime, func
from sqlalchemy_utils import URLType

from app.db import Base


class Meals(Base):
    __tablename__ = "Meals"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    type = Column(Integer,ForeignKey("Menu.id"), nullable=False)
    price = Column(Float(30), nullable=False)
    image_url = Column(URLType, nullable=True)
    active = Column(Boolean, default=True, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())

