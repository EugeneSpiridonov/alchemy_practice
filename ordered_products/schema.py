from pydantic import BaseModel


class SOrderedProducts(BaseModel):
    """Валидация полей базы данных"""

    order_id: int
    product_id: int

    class Config:
        # Валидировалось и без этой строки, но всё же:
        from_attributes = True
