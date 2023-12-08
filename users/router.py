from fastapi import APIRouter

from users.dao import UserDAO

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router.get("")
async def get_users():
    return await UserDAO.find_all()
