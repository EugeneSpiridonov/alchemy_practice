from fastapi import FastAPI
from sqladmin import Admin, ModelView

from database import engine
from users.models import Users
from users.router import router as user_router
from products.router import router as products_router
from orders.router import router as orders_router
from ordered_products.router import router as ordered_products_router
from product_photos.router import router as product_photos_router
from task_for_transactions import router as test_router


app = FastAPI()

app.include_router(user_router)
app.include_router(products_router)
app.include_router(orders_router)
app.include_router(ordered_products_router)
app.include_router(product_photos_router)
app.include_router(test_router)


# admin = Admin(app, engine)


# class UsersAdmin(ModelView, model=Users):
#     column_list = [Users.id, Users.username]


# admin.add_view(UsersAdmin)


@app.get("/")
def read_root():
    return {"Hello": "World"}
