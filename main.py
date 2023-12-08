from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    # Это просто для теста :)
    users = "meow"
    return templates.TemplateResponse(
        "index.html", {"request": request, "users": users}
    )
