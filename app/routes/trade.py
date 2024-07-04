
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from functions.trade import all_trade, add_trade, update_trade, delete_trade
from app.db import get_db

from routes.auth import get_current_active_user
from schemas.users import UserCurrent
from schemas.trade import TradeBase, TradeUpdate

trade_router = APIRouter()


@trade_router.get("", status_code=200)
async def trade_all(search: str = None, status: bool = None, page: int = 1, limit: int = 20,
                         db: Session = Depends(get_db), ):
    return all_trade(search=search, page=page, limit=limit,
                           db=db, active=status)


@trade_router.post("/add")
async def trade_add(form: TradeBase, db: Session = Depends(get_db), ):
    add_trade(form=form, thisuser=1 , db=db, )

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@trade_router.put("/update")
async def trade_update(
        form: TradeUpdate, db: Session = Depends(get_db),
        current_user: UserCurrent = Depends(
            get_current_active_user)):
    new_trade = update_trade(form=form, thisuser=current_user
                                        , db=db, )

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@trade_router.delete("/delete")
async def trade_delete(id: int, db: Session = Depends(get_db),):
    return delete_trade(id=id, db=db)
