from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from users.router import router as user_router

app = FastAPI()

app.include_router(user_router)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    return {"Hello": "World"}
