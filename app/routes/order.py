from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.functions.order import all_orders, add_order, delete_order
from app.db import get_db

from app.routes.auth import get_current_active_user
from app.schemas.users import UserCurrent
from app.schemas.order import OrderBase

order_router = APIRouter()


@order_router.get("", status_code=200)
async def all_order(search: str = None, status: bool = None, page: int = 1, limit: int = 20,
                    db: Session = Depends(get_db)):
    return all_orders(search=search, page=page, limit=limit,
                      db=db, active=status)


@order_router.post("/add")
async def order_add(form: OrderBase, db: Session = Depends(get_db)):
    new_order = add_order(form=form
                          , db=db, )

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@order_router.delete("/delete")
async def order_delete(id: int, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    return delete_order(id=id, db=db)
