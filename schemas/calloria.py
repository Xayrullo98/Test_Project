from pydantic import BaseModel


class CalorieBase(BaseModel):
    name: str
    quantity: float
    meal_id: int


class CalorieUpdate(CalorieBase):
    id: int
