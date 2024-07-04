from fastapi import HTTPException

from models.menu import Menu
from utils.pagination import pagination


def all_menu(active, search, page, limit, db):
    meal = db.query(Menu)
    if search:
        search_formatted = "%{}%".format(search)
        meal = meal.filter(
            Menu.money.ilike(search_formatted))

    if active in [True, False]:
        meal = meal.filter(Menu.active == active)

    meal = meal.order_by(Menu.id.desc())
    return pagination(meal, page, limit)


def one_menu(db, id):
    meal = db.query(Menu).filter(Menu.id == id).first()
    if meal:
        return meal
    raise HTTPException(status_code=400, detail="Bunday ma'lumot mavjud emas")


def add_menu(name, picture,thisuser, db, ):
    new_menu_db = Menu(
        name=name,
        image_url=picture,

    )
    db.add(new_menu_db)
    db.flush()
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def update_menu(id,name,picture, thisuser, db, ):
    one_menu(db=db, id=id)
    db.query(Menu).filsqater(Menu.id == id).update({
        Menu.name: name,
        Menu.picture: picture,
    })

    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def delete_menu(id, db):
    one_menu(db=db, id=id)
    db.query(Menu).filter(Menu.id == id).update({
        Menu.active: False, })
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")
