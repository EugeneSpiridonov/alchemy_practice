from fastapi import APIRouter

from ordered_products.dao import OrderedDAO
from ordered_products.schema import SOrderedProducts


router = APIRouter(
    prefix="/ordered_products",
    tags=["Заказанные товары"],
)


@router.get("")
async def get_ordered_products() -> list[SOrderedProducts]:
    return await OrderedDAO.find_all()
