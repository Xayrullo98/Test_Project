from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy_utils import URLType

from app.db import Base


class Products(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    image_url = Column(URLType, nullable=True)
    active = Column(Boolean, default=True, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())

