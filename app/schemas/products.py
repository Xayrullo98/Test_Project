from pydantic import BaseModel

from app.schemas.calloria import CalorieBase,CalorieUpdate


class ProductsBase(BaseModel):
    name: str
    calories: CalorieBase


class ProductsUpdate(BaseModel):
    id: int
    name:str
    calories:CalorieUpdate
