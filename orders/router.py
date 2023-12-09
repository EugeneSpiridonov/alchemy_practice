from fastapi import APIRouter

from orders.dao import OrderDAO
from orders.schema import SOrders


router = APIRouter(
    prefix="/orders",
    tags=["Заказы"],
)


@router.get("")
async def get_orders() -> list[SOrders]:
    return await OrderDAO.find_all()
