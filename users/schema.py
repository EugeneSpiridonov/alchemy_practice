from pydantic import BaseModel


class SUser(BaseModel):
    """Валидация полей базы данных"""

    id: int
    username: str
    phone: str
    email: str
    password: str

    class Config:
        # Валидировалось и без этой строки, но всё же:
        from_attributes = True
