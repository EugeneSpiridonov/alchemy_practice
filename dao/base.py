from sqlalchemy import select
from database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            # .__table__.columns избавляет от лишней вложенности
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()
