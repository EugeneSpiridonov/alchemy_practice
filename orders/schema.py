from pydantic import BaseModel


class SOrders(BaseModel):
    """Валидация полей базы данных"""

    id: int
    user_id: int

    class Config:
        # Валидировалось и без этой строки, но всё же:
        from_attributes = True
