from fastapi import HTTPException

from app.models.order import Orders
from app.utils.pagination import pagination


def all_orders(active, search, page, limit, db):
    meal = db.query(Orders)
    if search:
        search_formatted = "%{}%".format(search)
        meal = meal.filter(
            Orders.money.ilike(search_formatted))

    if active in [True, False]:
        meal = meal.filter(Orders.active == active)

    meal = meal.order_by(Orders.id.desc())
    return pagination(meal, page, limit)


def one_order(db, id):
    meal = db.query(Orders).filter(Orders.id == id).first()
    if meal:
        return meal
    raise HTTPException(status_code=400, detail="Bunday ma'lumot mavjud emas")


def add_order(form,  db, ):
    new_orders_db = Orders(

    )
    db.add(new_orders_db)
    db.flush()
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def delete_order(id, db):
    one_order(db=db, id=id)
    db.query(Orders).filter(Orders.id == id).update({
        Orders.active: False, })
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")
