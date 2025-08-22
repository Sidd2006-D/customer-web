from sqlalchemy import create_engine, Column, Integer, LargeBinary, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import select, insert, update, delete
from sqlalchemy import desc

from database_handler.models import *


def read_all_fans_row(session):
    with session.begin() as session_obj:
        data = []
        for obj in session_obj.query(TableFans).all():
            data.append(
                {
                    "fan_id": obj.id,
                    "fan_name": obj.name, 
                    "fan_rate": obj.rate, 
                }
            )

        return data
def read_all_fanStock_row(session):
    with session.begin() as session_obj:
        data = []
        for obj in session_obj.query(TableStockOfFans).all():
            data.append(
                {
                    "fan_id": obj.id,
                    "fan_name": obj.name, 
                    "fan_qty": obj.qty, 
                }
            )
        print(data)
        return data


def insert_fan_row(session, data):
    """
    Inserts a fan and its stock entry in one transaction.
    """
    with session.begin() as session_obj:
        # Create parent fan entry
        new_fan = TableFans(name=data["name"], rate=data["rate"])

        # Create stock entry linked to the fan  
        stock_entry = TableStockOfFans(name=data["name"], qty=data["qty"])

        # Attach stock entry to fan
        new_fan.stock_entries.append(stock_entry)

        # Add fan (stock gets added automatically because of relationship)
        session_obj.add(new_fan)

    print(f"Fan '{data['name']}' with stock '({data['qty']})' inserted successfully!")

class FanStockApi:
    session = None
    data = None
    def __init__(self, session, data):
       self.session = session
       self.data = data
 
    def add(self):
        with self.session.begin() as session_obj:
            fan_id = self.data["fan_id"]
            qty = self.data["qty"]

            fan_obj = session_obj.get(TableFans, fan_id)
            print("-------------")
            print(fan_obj)
            print("-------------")
            if not fan_obj:
                return "Selected object is not available!"
            print("Selected Fan id:", fan_obj.id, ", name:", fan_obj.name)
            try:
                query_filter = session_obj.query(TableStockOfFans).filter_by(
                    fan_id=fan_obj.id
                )
                row_count = query_filter.count()
                print("row_count:", row_count)
                stock_obj = query_filter.one()
            except:
                stock_obj = None
            if stock_obj:
                print("Before Update:", stock_obj.qty)
                stock_obj.qty += qty
                print("After Update:", stock_obj.qty)
                session_obj.commit()
                print("Stock was there, stock updated")
                return "Stock was there, stock updated"
            else:
                stock = TableStockOfFans()
                stock.fan_id = fan_obj.id
                stock.name = fan_obj.name
                stock.qty = qty
                session_obj.add(stock)
                session_obj.commit()
                print("Stock was not there, stock inserted")
                return "Stock was not there, stock inserted"
 
    def reduce(self):
        with self.session.begin() as session_obj:
            fan_id = self.data["fan_id"]
            qty = self.data["qty"]
            fan_obj = session_obj.get(TableFans, fan_id)
            print("-------------")
            print(fan_obj)
            print("-------------")
            if not fan_obj:
                return "Selected object is not available!"
            print("Selected Fan id:", fan_obj.id, ", name:", fan_obj.name)
            try:
                query_filter = session_obj.query(TableStockOfFans).filter_by(
                    fan_id=fan_obj.id
                )
                row_count = query_filter.count()
                print("row_count:", row_count)
                stock_obj = query_filter.one()
            except:
                return "No stock found for this fan!"
            print("Before Reduction:", stock_obj.qty)
            if stock_obj.qty < qty:
                return "Not enough stock to reduce!"
            stock_obj.qty -= qty

            print("After Reduction:", stock_obj.qty)
            session_obj.commit()
            print("Stock reduced successfully")

            return "Stock was there, stock updated"


def delete_fan_stock(session, data):
    with session.begin() as session_obj:
        id = data["fan_id"]
        name = data["fan_name"]
        fan_row = session_obj.query(TableFans).get(id)
        if fan_row:
            session_obj.delete(fan_row)
            session_obj.commit()
            print(f"{name} data is deleted")
            return f"{name} data is deleted"
        else:
            print("Fan not found.")
            return "Fan not found."
