from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, Boolean, DateTime, func
from sqlalchemy_utils import URLType

from db import Base


class Orders(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True)
    meal = Column(Integer,ForeignKey("Meals.id"), nullable=False)
    number = Column(Float, nullable=True,default=0)
    active = Column(Boolean, default=True, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())

