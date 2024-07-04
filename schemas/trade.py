from pydantic import BaseModel


class TradeBase(BaseModel):
    meal_id: int
    order_id: int
    number: float


class TradeUpdate(TradeBase):
    id: int
