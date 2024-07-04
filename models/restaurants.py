from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, func

from db import Base


class Restaurant(Base):
    __tablename__ = "Restaurant"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    address = Column(Text, nullable=True)
    active = Column(Boolean, default=True, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
