from fastapi import HTTPException

from models.trade import Trades
from utils.pagination import pagination


def all_trade(active, search, page, limit, db):
    meal = db.query(Trades)
    if search:
        search_formatted = "%{}%".format(search)
        meal = meal.filter(
            Trades.money.ilike(search_formatted))

    if active in [True, False]:
        meal = meal.filter(Trades.active == active)

    meal = meal.order_by(Trades.id.desc())
    return pagination(meal, page, limit)


def one_trade(db, id):
    meal = db.query(Trades).filter(Trades.id == id).first()
    if meal:
        return meal
    raise HTTPException(status_code=400, detail="Bunday ma'lumot mavjud emas")


def add_trade(form, thisuser, db, ):
    new_trade_db = Trades(
        meal_id=form.meal_id,
        order_id=form.order_id,
        number=form.number,

    )
    db.add(new_trade_db)
    db.flush()
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def update_trade(form, thisuser, db, ):
    one_trade(db=db, id=form.id)
    db.query(Trades).filter(Trades.id == form.id).update({
        Trades.meal_id: form.meal_id,
        Trades.order_id: form.order_id,
        Trades.number: form.number,

    })

    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def delete_trade(id, db):
    one_trade(db=db, id=id)
    db.query(Trades).filter(Trades.id == id).update({
        Trades.active: False, })
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")
