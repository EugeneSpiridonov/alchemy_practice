from fastapi import APIRouter, HTTPException
from sqlalchemy import Column, Integer, Float
from database import Base, async_session_maker


class Test_order(Base):
    __tablename__ = "test_orders"
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, nullable=False)
    total_amount = Column(Float)


router = APIRouter(
    prefix="/create_order",
    tags=["TEST"],
)


# Транзакция
@router.post("")
async def create_order():
    try:
        async with async_session_maker.begin() as session:
            # Вставка нового заказа
            new_order = Test_order(customer_id=107, total_amount=900.00)
            session.add(new_order)

            # Попытка вставить пустой заказ (без указания customer_id)
            empty_order = Test_order(total_amount=300.00)
            session.add(empty_order)

            # # Вставка дополнительных товаров в заказ
            # order_item1 = Test_order(customer_id=102, total_amount=600.00)
            # # order_item1 = OrderItem(order_id=new_order.order_id, product_id=201, quantity=2)
            # order_item2 = Test_order(customer_id=103, total_amount=777.77)
            # session.add_all([order_item1, order_item2])

    except Exception as e:
        # Обработка ошибок и откат транзакции
        return HTTPException(status_code=500, detail="Transaction failed")

    # Возвращаем успешный ответ
    return {"message": "Заказ создан успешно!"}
