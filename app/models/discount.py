from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, func, Boolean

from app.db import Base


class Discount(Base):
    __tablename__ = "Discount"
    id = Column(Integer, primary_key=True)
    money = Column(Float, nullable=False)
    meal_id = Column(Integer,ForeignKey("Meals.id"), nullable=False)
    start_date = Column(DateTime(timezone=True))
    end_date = Column(DateTime(timezone=True))
    active = Column(Boolean, default=True, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())

