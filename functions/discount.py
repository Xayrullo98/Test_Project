from fastapi import HTTPException

from models.discount import Discount
from utils.pagination import pagination


def all_discounts(active, search, page, limit, db):
    discount = db.query(Discount)
    if search:
        search_formatted = "%{}%".format(search)
        discount = discount.filter(
            Discount.money.ilike(search_formatted))

    if active in [True, False]:
        discount = discount.filter(Discount.active == active)

    discount = discount.order_by(Discount.id.desc())
    return pagination(discount, page, limit)


def one_discount(db, id):
    discount = db.query(Discount).filter(Discount.id == id).first()
    if discount:
        return discount
    raise HTTPException(status_code=400, detail="Bunday ma'lumot mavjud emas")


def add_discount(form, thisuser, db, ):
    new_discounts_db = Discount(
        money=form.money,
        start_date=form.start_date,
        end_date=form.end_date,
    )
    db.add(new_discounts_db)
    db.flush()
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def update_discounts(form, thisuser, db, ):
    one_discount(db=db, id=form.id)
    db.query(Discount).filter(Discount.id == form.id).update({
        Discount.money: form.money,
        Discount.start_date: form.start_date,
        Discount.end_date: form.end_date
    })

    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def delete_discount(id, db):
    one_discount(db=db, id=id)
    db.query(Discount).filter(Discount.id == id).update({
        Discount.active: False, })
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")
