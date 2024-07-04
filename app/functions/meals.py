from fastapi import HTTPException

from app.models.meals import Meals
from app.utils.pagination import pagination


def all_meals(active, search, page, limit, db):
    meal = db.query(Meals)
    if search:
        search_formatted = "%{}%".format(search)
        meal = meal.filter(
            Meals.money.ilike(search_formatted))

    if active in [True, False]:
        meal = meal.filter(Meals.active == active)

    meal = meal.order_by(Meals.id.desc())
    return pagination(meal, page, limit)


def one_meal(db, id):
    meal = db.query(Meals).filter(Meals.id == id).first()
    if meal:
        return meal
    raise HTTPException(status_code=400, detail="Bunday ma'lumot mavjud emas")


def add_meal(name, type,picture,price,thisuser, db, ):
    new_meals_db = Meals(
        name=name,
        type=type,
        picture=picture,
        price=price,
    )
    db.add(new_meals_db)
    db.flush()
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def update_meals(form, thisuser, db, ):
    one_meal(db=db, id=form.id)
    db.query(Meals).filter(Meals.id == form.id).update({
        Meals.type: form.type,
        Meals.picture: form.picture,
        Meals.price: form.price
    })

    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def delete_meal(id, db):
    one_meal(db=db, id=id)
    db.query(Meals).filter(Meals.id == id).update({
        Meals.active: False, })
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")
