from fastapi import HTTPException

from models.calloria import Calorie
from utils.pagination import pagination


def all_calorie(active, search, page, limit, db):
    callorie = db.query(Calorie)
    if search:
        search_formatted = "%{}%".format(search)
        callorie = callorie.filter(
            Calorie.money.ilike(search_formatted))

    if active in [True, False]:
        callorie = callorie.filter(Calorie.active == active)

    callorie = callorie.order_by(Calorie.id.desc())
    return pagination(callorie, page, limit)


def one_calorie(db, id):
    callorie = db.query(Calorie).filter(Calorie.id == id).first()
    if callorie:
        return callorie
    raise HTTPException(status_code=400, detail="Bunday ma'lumot mavjud emas")


def add_calorie(form, thisuser, db, ):
    new_calorie_db = Calorie(
        name=form.money,
        quantity=form.quantity,
        meal_id=form.meal_id,

    )
    db.add(new_calorie_db)
    db.flush()
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def update_calorie(form, thisuser, db, ):
    one_calorie(db=db, id=form.id)
    db.query(Calorie).filter(Calorie.id == form.id).update({
        Calorie.name: form.name,
        Calorie.quantity: form.quantity,

    })

    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def delete_calorie(id, db):
    one_calorie(db=db, id=id)
    db.query(Calorie).filter(Calorie.id == id).update({
        Calorie.active: False, })
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")
