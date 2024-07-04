from pydantic import BaseModel


class OrderBase(BaseModel):
    pass


class OrderUpdate(OrderBase):
    id: int
