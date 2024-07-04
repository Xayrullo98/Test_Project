from pydantic import BaseModel


class RestaurantBase(BaseModel):
    name: str
    address: str


class RestaurantUpdate(RestaurantBase):
    id: int
