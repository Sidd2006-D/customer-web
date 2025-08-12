from sqlalchemy import create_engine, Column, Integer, LargeBinary, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import select, insert, update, delete
from sqlalchemy import desc

from database_handler.models import *


def read_all_fans_row(session):
    with session.begin() as session_obj:
        data = []
        for stock in session_obj.query(TableStockOfFans).all():
            data.append(
                {
                    "stock_id": stock.id,
                    "stock_name": stock.name,
                    "qty": stock.qty,
                    "fan_id": stock.fan_id,
                    "fan_name": stock.fan.name,  # Accessed from foreign table
                    "fan_rate": stock.fan.rate,  # Also accessed from foreign table
                }
            )

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


class create_update_fan_stock:
    @staticmethod
    def add(session, data):
        with session.begin() as session_obj:
            fan_id = data["fan_id"]
            qty = data["qty"]

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

    @staticmethod
    def reduce(session, data):
        with session.begin() as session_obj:
            fan_id = data["fan_id"]
            qty = data["qty"]
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




def file_read_api(file):
    pass
    