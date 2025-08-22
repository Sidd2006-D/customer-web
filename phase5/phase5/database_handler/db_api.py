from sqlalchemy import create_engine, Column, Integer, LargeBinary, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import insert
from sqlalchemy import desc

from database_handler.models import *
from fans_api.fans import read_all_fans_row, insert_fan_row, delete_fan_stock
from fans_api.fans import FanStockApi
from fans_api.fans import read_all_fanStock_row

# db_connection_string = 'mysql+pymysql://root:mysql_123@localhost/code_vault'
db_connection_string = "mysql+pymysql://root:ronaldo@localhost/practice"
# db_connection_string = 'postgresql+psycopg2://user:password@host:port/database_name'
# db_connection_string = 'oracle+cx_oracle://user:password@host:port/?service_name=my_service_name'
# db_connection_string = 'db2://{user}:{password}@{host}:{port}/{database}'


def get_session_obj():
    print("#DB connection...")
    engine = create_engine(db_connection_string)
    DBBaseHandler.metadata.create_all(engine)
    print("#DB ORM Ready")
    print("#Making session obj")
    Session = sessionmaker(bind=engine)  # Session banate hain database ke liye
    return Session
    # print("sessionmaker is ready")
    # session = Session()                     # Session object activate karte hain
    # print("#Session obj is active")
    # return session

def read_fans_from_db(session):
    return read_all_fans_row(session)

def read_fanStock_from_db(session):
    return read_all_fanStock_row(session)


def insert_fans_into_db(session, fan_dict):
    return insert_fan_row(session, fan_dict)


def update_fan_stock_into_db_add(session, data):
    fanstockApi = FanStockApi(session, data)
    return fanstockApi.add() 

def update_fan_stock_into_db_reduce(session, data):
    fanstockApi = FanStockApi(session, data)
    return fanstockApi.reduce() 

def delete_fan_stock_into_db(session, data):
    return delete_fan_stock(session, data)

def insert_stock_of_fans_into_db(session):
    x = True
    while x:
        try:
            fan_id_value = str(input("Enter Fan_id:"))
            qtyvalue = int(input("Enter qty:"))
            inserting_data_query = insert(TableStockOfFans).values(
                name="", qty=qtyvalue, fan_id=fan_id_value
            )
            result = session.execute(inserting_data_query)
            print("Last StockRowId: %s" % result.lastrowid)
        except:
            x = False

    # Transaction commit karte hain taki data save ho jaye
    session.commit()
