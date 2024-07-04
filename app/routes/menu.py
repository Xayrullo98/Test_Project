import inspect
import shutil
import typing
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.functions.menu import all_menu, add_menu, update_menu, delete_menu
from app.db import get_db

from app.routes.auth import get_current_active_user
from app.schemas.users import UserCurrent

menu_router = APIRouter()


@menu_router.get("", status_code=200)
async def all_menu(search: str = None,
                   page: int = 1, limit: int = 20,
                   db: Session = Depends(get_db)):
    return all_menu(search=search, page=page, limit=limit,
                    db=db)


@menu_router.post("/add")
async def menu_add(name: str,

                   file: typing.Optional[UploadFile] = File(None)
                   , db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    if file:
        with open("media/" + file.filename, 'wb') as image:
            shutil.copyfileobj(file.file, image)
        url = str('media/' + file.filename)
        new_menu = add_menu(name=name, thisuser=current_user
                            , db=db, picture=url, )

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@menu_router.put("/update")
async def menu_update(
        id: int,
        name: str,
        file: typing.Optional[UploadFile] = File(None), db: Session = Depends(get_db),
        current_user: UserCurrent = Depends(
            get_current_active_user)):
    if file:
        with open("media/" + file.filename, 'wb') as image:
            shutil.copyfileobj(file.file, image)
        url = str('media/' + file.filename)
        new_menu = update_menu(id=id, name=name, thisuser=current_user
                               , db=db, picture=url)

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@menu_router.delete("/delete")
async def menu_delete(id: int, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    return delete_menu(id=id, db=db)
