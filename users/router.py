from fastapi import APIRouter
from sqlalchemy import select
from database import async_session_maker
from users.models import Users

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router.get("")
async def get_users():
    async with async_session_maker() as session:
        # .__table__.columns избавляет от лишней вложенности
        query = select(Users.__table__.columns)
        result = await session.execute(query)
        return result.mappings().all()
