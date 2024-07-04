
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from functions.restaurants import all_restaurants, add_restaurant, update_restaurants, delete_restaurant
from app.db import get_db

from routes.auth import get_current_active_user
from schemas.users import UserCurrent
from schemas.restaurants import RestaurantBase, RestaurantUpdate

restaurant_router = APIRouter()


@restaurant_router.get("", status_code=200)
async def restaurant_all(search: str = None, status: bool = None, page: int = 1, limit: int = 20,
                         db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    return all_restaurants(search=search, page=page, limit=limit,
                           db=db, active=status)


@restaurant_router.post("/add")
async def restaurant_add(form: RestaurantBase, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    new_restaurant = add_restaurant(form=form, thisuser=current_user
                                    , db=db, )

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@restaurant_router.put("/update")
async def restaurant_update(
        form: RestaurantUpdate, db: Session = Depends(get_db),
        current_user: UserCurrent = Depends(
            get_current_active_user)):
    new_restaurant = update_restaurants(form=form, thisuser=current_user
                                        , db=db, )

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@restaurant_router.delete("/delete")
async def restaurant_delete(id: int, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    return delete_restaurant(id=id, db=db)
