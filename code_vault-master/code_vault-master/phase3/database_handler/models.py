from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, LargeBinary, String
from sqlalchemy.orm import declarative_base


DBBaseHandler = declarative_base()

# TableFans class banate hain, jo fans table ko represent karta hai
class TableFans(DBBaseHandler):
    __tablename__ = 'fans'
    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String(255))              # Fan ka brand name
    rate = Column(Integer)      
 
class TableStockOfFans(DBBaseHandler):
    __tablename__ = 'stock_of_fan'
    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String(255))              # Fan ka brand name
    qty = Column(Integer)      
    fan_id = Column(Integer, ForeignKey('fans.id')) # Foreign key definition