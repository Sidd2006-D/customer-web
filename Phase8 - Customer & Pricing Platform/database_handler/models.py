from sqlalchemy import ForeignKey
from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, Date
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base, relationship


DBBaseHandler = declarative_base()


class CustomerModel(DBBaseHandler):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    base_price = Column(String(255))


class ProductModel(DBBaseHandler):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    # rate = Column(Integer, default=0)
    tax_rate = Column(Float, default=0)


class PriceListModel(DBBaseHandler):
    __tablename__ = "price_list"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)


class ProductWisePriceModel(DBBaseHandler):
    __tablename__ = "product_wise_price"
    id = Column(Integer, primary_key=True)
    rate = Column(Integer, default=0)
    price_list_id = Column(Integer, ForeignKey("price_list.id"))
    product_id = Column(Integer, ForeignKey("product.id"))


class CustomerOrderModel(DBBaseHandler):
    __tablename__ = "customer_order"
    id = Column(Integer, primary_key=True, autoincrement=True) 
    created_on = Column(DateTime(timezone=False), server_default=func.now())
    updated_on = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())
    date = Column(Date, nullable=False)
    month = Column(Date, nullable=False)
    customer_id = Column(Integer, nullable=False)
    customer_name = Column(String(255), nullable=False)
    base_price = Column(String(100), nullable=False)
    product_count = Column(Integer, nullable=False)
    tax_amount = Column(Float, nullable=False)
    sub_total = Column(Float, nullable=False)
    grand_total = Column(Float, nullable=False)


class CustomerOrderItemsModel(DBBaseHandler):
    __tablename__ = "customer_order_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("customer_order.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    product_name = Column(String(255))
    quantity = Column(Integer)
    rate = Column(Float)
    tax_rate = Column(Float)
    tax_amount = Column(Float)
    line_total = Column(Float) #Exclusive Tax Calculation
