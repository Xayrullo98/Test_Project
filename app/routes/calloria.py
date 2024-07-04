from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.functions.calloria import all_calorie, add_calorie, update_calorie, delete_calorie
from app.db import get_db

from app.routes.auth import get_current_active_user
from app.schemas.users import UserCurrent
from app.schemas.calloria import CalorieBase, CalorieUpdate

calorie_router = APIRouter()


@calorie_router.get("", status_code=200)
async def calorie_all(search: str = None, status: bool = None, page: int = 1, limit: int = 20,
                      db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    return all_calorie(search=search, page=page, limit=limit,
                       db=db, active=status)


@calorie_router.post("/add")
async def calorie_add(form: CalorieBase, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    new_calorie = add_calorie(form=form, thisuser=current_user
                              , db=db, )

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@calorie_router.put("/update")
async def calorie_update(
        form: CalorieUpdate, db: Session = Depends(get_db),
        current_user: UserCurrent = Depends(
            get_current_active_user)):
    new_calorie = update_calorie(form=form, thisuser=current_user
                                 , db=db, )

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@calorie_router.delete("/delete")
async def calorie_delete(id: int, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    return delete_calorie(id=id, db=db)
