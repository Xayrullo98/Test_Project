from fastapi import HTTPException

from app.models.products import Products
from app.utils.pagination import pagination


def all_product(active, search, page, limit, db):
    meal = db.query(Products)
    if search:
        search_formatted = "%{}%".format(search)
        meal = meal.filter(
            Products.money.ilike(search_formatted))

    if active in [True, False]:
        meal = meal.filter(Products.active == active)

    meal = meal.order_by(Products.id.desc())
    return pagination(meal, page, limit)


def one_product(db, id):
    meal = db.query(Products).filter(Products.id == id).first()
    if meal:
        return meal
    raise HTTPException(status_code=400, detail="Bunday ma'lumot mavjud emas")


def add_product(name,image_url, thisuser, db, ):
    new_product_db = Products(
        name=name,
        image_url=image_url,


    )
    db.add(new_product_db)
    db.flush()
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def update_product(id,name,image_url, thisuser, db, ):
    one_product(db=db, id=id)
    db.query(Products).filter(Products.id == id).update({
        Products.name: name,
        Products.image_url: image_url,

    })

    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def delete_product(id, db):
    one_product(db=db, id=id)
    db.query(Products).filter(Products.id == id).update({
        Products.active: False, })
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")
