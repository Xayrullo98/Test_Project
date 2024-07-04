from pydantic import BaseModel
from pydantic.datetime_parse import date


class DiscountBase(BaseModel):
    money: float
    meal_id: int
    start_date: date
    end_date: date


class DiscountUpdate(DiscountBase):
    id: int
