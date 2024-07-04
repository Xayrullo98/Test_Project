from fastapi import FastAPI

from app.routes import auth,users,restaurants,products,order,calloria,trade,discount,meals,menu

from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Test Project",
    responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
               401: {'desription': 'Unauthorized'}}
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {"message": "Welcome"}

app.include_router(
    auth.login_router,
    prefix='/auth',
    tags=['User auth section'])

app.include_router(
    users.user_router,
    prefix='/user',
    tags=['User section'])
app.include_router(
    restaurants.restaurant_router,
    prefix='/restaurant',
    tags=['Restaurant section'])

app.include_router(
    meals.meals_router,
    prefix='/meals',
    tags=['Meals section'])
app.include_router(
    menu.menu_router,
    prefix='/menu',
    tags=['Menu section'])
app.include_router(
    products.product_router,
    prefix='/product',
    tags=['Products section'])
app.include_router(
    order.order_router,
    prefix='/order',
    tags=['Order section'])
app.include_router(
    calloria.calorie_router,
    prefix='/calorie',
    tags=['Calorie section'])
app.include_router(
    trade.trade_router,
    prefix='/trade',
    tags=['Trade section'])
app.include_router(
    discount.discount_router,
    prefix='/discount',
    tags=['Discount section'])


