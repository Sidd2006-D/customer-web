from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, Float, String
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
    rate = Column(Integer, default=0) 
    tax_rate = Column(Float, default=0)

class PriceListModel(DBBaseHandler):
    __tablename__ = "price_list"
    id = Column(Integer, primary_key=True)
    name = Column(String(255),  unique=True)   

class ProductWisePriceModel(DBBaseHandler):
    __tablename__ = "product_wise_price"
    id = Column(Integer, primary_key=True)
    rate = Column(Integer, default=0)
    price_list_id = Column(Integer, ForeignKey("price_list.id"))
    product_id = Column(Integer, ForeignKey("product.id")) 
     