from fastapi import APIRouter

from products.dao import ProductDAO
from products.schema import SProduct


router = APIRouter(
    prefix="/products",
    tags=["Товары"],
)


@router.get("")
async def get_products() -> list[SProduct]:
    return await ProductDAO.find_all()
