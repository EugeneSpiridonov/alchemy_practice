from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Pr_photos(Base):
    __tablename__ = "product_photo"

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    product_id = Column(ForeignKey("products.id"), primary_key=True)
    product = relationship("Products", back_populates="photos")
