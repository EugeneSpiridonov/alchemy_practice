from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text(), nullable=True)
    price = Column(Integer, nullable=False)
    photos = relationship("Pr_photos", back_populates="product")
    ordered_products = relationship("OrderedProducts", back_populates="product")
