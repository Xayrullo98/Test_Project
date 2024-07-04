from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, DateTime, func

from app.db import Base


class Calorie(Base):
    __tablename__ = "Calorie"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    quantity = Column(Float, nullable=True)
    meal_id = Column(Integer, ForeignKey("Meals.id"), nullable=True)
    active = Column(Boolean, default=True, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
