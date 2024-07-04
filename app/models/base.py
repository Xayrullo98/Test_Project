
from sqlalchemy import Column, Integer, Boolean, DateTime, func

from app.db import Base


class BaseModel(Base):
    __tablename__ = "BaseModel"
    id = Column(Integer, primary_key=True)
    active = Column(Boolean, default=True, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
