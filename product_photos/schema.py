from pydantic import BaseModel


class SProduct_photos(BaseModel):
    """Валидация полей базы данных"""

    id: int
    url: str
    product_id: int

    class Config:
        # Валидировалось и без этой строки, но всё же:
        from_attributes = True
