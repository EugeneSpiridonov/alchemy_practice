from dao.base import BaseDAO
from products.models import Products


class ProductDAO(BaseDAO):
    model = Products
