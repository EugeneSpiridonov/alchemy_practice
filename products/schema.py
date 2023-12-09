from pydantic import BaseModel


class SProduct(BaseModel):
    """Валидация полей базы данных"""

    id: int
    name: str
    description: str
    price: int

    class Config:
        # Валидировалось и без этой строки, но всё же:
        from_attributes = True
