from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, Boolean, DateTime, func
from sqlalchemy_utils import URLType

from app.db import Base


class Trades(Base):
    __tablename__ = "Trades"
    id = Column(Integer, primary_key=True)
    meal_id = Column(Integer,ForeignKey("Meals.id"), nullable=False)
    order_id = Column(Integer,ForeignKey("Orders.id"), nullable=False)
    number = Column(Float, nullable=True,default=0)
    active = Column(Boolean, default=True, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())

