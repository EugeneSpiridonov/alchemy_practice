from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class OrderedProducts(Base):
    __tablename__ = "ordered_products"

    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    order = relationship("Orders", back_populates="ordered_products")
    product = relationship("Products", back_populates="ordered_products")
