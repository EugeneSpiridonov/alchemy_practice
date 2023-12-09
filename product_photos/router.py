from fastapi import APIRouter

from product_photos.dao import Pr_photosDAO
from product_photos.schema import SProduct_photos


router = APIRouter(
    prefix="/product_photos",
    tags=["Фото товаров"],
)


@router.get("")
async def get_product_photos() -> list[SProduct_photos]:
    return await Pr_photosDAO.find_all()
