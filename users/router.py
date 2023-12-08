from fastapi import APIRouter

from users.dao import UserDAO
from users.schema import SUser

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router.get("")
async def get_users() -> list[SUser]:
    return await UserDAO.find_all()
