from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from functions.discount import all_discounts, add_discount, update_discounts, delete_discount
from db import get_db

from routes.auth import get_current_active_user
from schemas.users import UserCurrent
from schemas.discount import DiscountBase, DiscountUpdate

discount_router = APIRouter()


@discount_router.get("", status_code=200)
async def all_discount(search: str = None, status: bool = None, page: int = 1, limit: int = 20,
                       db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    return all_discounts(search=search, page=page, limit=limit,
                         db=db, active=status)


@discount_router.post("/add")
async def discount_add(form: DiscountBase, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    new_discount = add_discount(form=form, thisuser=current_user
                                , db=db, )

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@discount_router.put("/update")
async def discount_update(
        form: DiscountUpdate, db: Session = Depends(get_db),
        current_user: UserCurrent = Depends(
            get_current_active_user)):
    new_discount = update_discounts(form=form, thisuser=current_user
                                    , db=db, )

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@discount_router.delete("/delete")
async def discount_delete(id: int, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    return delete_discount(id=id, db=db)
