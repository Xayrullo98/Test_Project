from pydantic import BaseModel

from schemas.calloria import CalorieBase,CalorieUpdate


class ProductsBase(BaseModel):
    name: str
    calories: CalorieBase


class ProductsUpdate(BaseModel):
    id: int
    name:str
    calories:CalorieUpdate
