from sqlalchemy import select
from database import async_session_maker


class BaseDAO:
    """Методы для работы с БД"""

    model = None

    @classmethod
    async def find_one_or_none(cls, id: int):
        async with async_session_maker() as session:
            # .__table__.columns избавляет от лишней вложенности
            query = select(cls.model.__table__.columns).filter_by(user_id=id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            # .__table__.columns избавляет от лишней вложенности
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()
