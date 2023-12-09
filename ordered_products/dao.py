from dao.base import BaseDAO
from ordered_products.models import OrderedProducts


class OrderedDAO(BaseDAO):
    model = OrderedProducts
