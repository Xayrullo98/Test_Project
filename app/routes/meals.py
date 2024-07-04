import shutil
import typing

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.functions.meals import all_meals, add_meal, delete_meal
from app.db import get_db

from app.routes.auth import get_current_active_user
from app.schemas.users import UserCurrent

meals_router = APIRouter()


@meals_router.get("", status_code=200)
async def all_meals(search: str = None, status: bool = None, page: int = 1, limit: int = 20,
                    db: Session = Depends(get_db), ):
    return all_meals(search=search, page=page, limit=limit,
                     db=db, active=status)


@meals_router.post("/add")
async def menu_add(name: str,
                   type_id: int,
                   price: float,
                   file: typing.Optional[UploadFile] = File(None)
                   , db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    if file:
        with open("media/" + file.filename, 'wb') as image:
            shutil.copyfileobj(file.file, image)
        url = str('media/' + file.filename)
        new_menu = add_meal(name=name, thisuser=current_user
                            , db=db, picture=url, type=type_id, price=price)

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


# @menu_router.put("/update")
# async def menu_update(
#         id: int,
#         name: str,
#
#         files: typing.Optional[typing.List[UploadFile]] = File(None), db: Session = Depends(get_db),
#         current_user: UserCurrent = Depends(
#             get_current_active_user)):
#     new_menu = update_menu(id=id, title=title, thisuser=current_user
#                            , db=db, description=description)
#     if files:
#         for file in files:
#             with open("media/" + file.filename, 'wb') as image:
#                 shutil.copyfileobj(file.file, image)
#             url = str('media/' + file.filename)
#             update_file(source_id=new_menu.id, source='menu', image_url=url, user=current_user, db=db, )


@meals_router.delete("/delete")
async def menu_delete(id: int, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    return delete_meal(id=id, db=db)
