import shutil
import typing

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.functions.products import all_product, add_product, update_product, delete_product
from app.db import get_db

from app.routes.auth import get_current_active_user
from app.schemas.users import UserCurrent

product_router = APIRouter()


@product_router.get("", status_code=200)
async def product_all(search: str = None, status: bool = None, page: int = 1, limit: int = 20,
                      db: Session = Depends(get_db), ):
    return all_product(search=search, page=page, limit=limit,
                       db=db, active=status)


@product_router.post("/add")
async def menu_add(name: str,

                   file: typing.Optional[UploadFile] = File(None)
                   , db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    if file:
        with open("media/" + file.filename, 'wb') as image:
            shutil.copyfileobj(file.file, image)
        url = str('media/' + file.filename)
        new_menu = add_product(name=name, thisuser=current_user
                            , db=db, image_url=url, )

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@product_router.put("/update")
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
        update_product(id=id, name=name, thisuser=current_user
                       , db=db, image_url=url)

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@product_router.delete("/delete")
async def product_delete(id: int, db: Session = Depends(get_db), ):
    return delete_product(id=id, db=db)
