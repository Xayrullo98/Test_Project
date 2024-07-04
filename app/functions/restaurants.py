from fastapi import HTTPException

from app.models import Restaurant
from utils.pagination import pagination


def all_restaurants(active, search, page, limit, db):
    restaurants = db.query(Restaurant)
    if search:
        search_formatted = "%{}%".format(search)
        restaurants = restaurants.filter(
            Restaurant.name.ilike(search_formatted))

    if active in [True, False]:
        restaurants = restaurants.filter(Restaurant.active == active)

    restaurants = restaurants.order_by(Restaurant.id.desc())
    return pagination(restaurants, page, limit)


def one_restaurant(db, id):
    restaurant = db.query(Restaurant).filter(Restaurant.id == id).first()
    if restaurant:
        return restaurant
    raise HTTPException(status_code=400, detail="Bunday ma'lumot mavjud emas")


def add_restaurant(form, thisuser, db, ):
    new_restaurants_db = Restaurant(
        name=form.name,
        address=form.address,
    )
    db.add(new_restaurants_db)
    db.flush()
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def update_restaurants(form, thisuser, db, ):
    one_restaurant(db=db, id=form.id)
    db.query(Restaurant).filter(Restaurant.id == form.id).update({
        Restaurant.name: form.name,
        Restaurant.address: form.address,
    })

    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def delete_restaurant(id, db):
    one_restaurant(db=db, id=id)
    db.query(Restaurant).filter(Restaurant.id == id).update({
        Restaurant.active: False, })
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")
