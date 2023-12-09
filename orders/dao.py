from dao.base import BaseDAO
from orders.models import Orders


class OrderDAO(BaseDAO):
    model = Orders
