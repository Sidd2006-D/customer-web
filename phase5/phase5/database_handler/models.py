from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, LargeBinary, String
from sqlalchemy.orm import declarative_base, relationship


DBBaseHandler = declarative_base()


class TableFans(DBBaseHandler):
    __tablename__ = "fans"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    rate = Column(Integer)

    # Optional: one-to-many relationship
    stock_entries = relationship(
        "TableStockOfFans", back_populates="fan", cascade="all,delete"
    )


class TableStockOfFans(DBBaseHandler):
    __tablename__ = "stock_of_fan"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    qty = Column(Integer, default=0)
    fan_id = Column(Integer, ForeignKey("fans.id"))

    # This gives you access to the related fan object
    fan = relationship("TableFans", back_populates="stock_entries")
