from sqlalchemy import create_engine, Column, Integer, LargeBinary, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import insert
from sqlalchemy import desc
 
from database_handler.models import *
db_connection_string = 'mysql+pymysql://root:ronaldo@localhost/practice'
# db_connection_string = 'mysql+pymysql://root:mysql_123@localhost/code_vault'
# db_connection_string = 'mysql+pymysql://root:mysql_123@localhost/code_vault'
# db_connection_string = 'postgresql+psycopg2://user:password@host:port/database_name'
# db_connection_string = 'oracle+cx_oracle://user:password@host:port/?service_name=my_service_name'
# db_connection_string = 'db2://{user}:{password}@{host}:{port}/{database}'


def get_session_obj():
    print("#DB connection...")
    engine = create_engine(db_connection_string)
    DBBaseHandler.metadata.create_all(engine)
    print("#DB ORM Ready")
    print("#Making session obj")
    Session = sessionmaker(bind=engine)     # Session banate hain database ke liye
    print("sessionmaker is ready")
    session = Session()                     # Session object activate karte hain
    print("#Session obj is active")
    return session

def insert_fans_into_db(session):
  choice = int(input("How enter number of rows to insert fans:")) 
  
  for i in range(choice):
    namevalue = str(input("Enter FAN brand name:"))
    ratevalue = int(input("Enter Rate of FAN :"))
    inserting_data_query = insert(TableFans).values(name=namevalue, rate=ratevalue  )
    result = session.execute(inserting_data_query)
    

  # Transaction commit karte hain taki data save ho jaye
  session.commit()


def read_fans_into_db(session):
  result=session.query(TableFans).all()
  return result
    
  



def insert_stock_of_fans_into_db(session): 
  x=True
  while x:
    try:
      fan_id_value = str(input("Enter Fan_id:"))
      qtyvalue = int(input("Enter qty:"))
      inserting_data_query = insert(TableStockOfFans).values(name='', qty=qtyvalue, fan_id=fan_id_value)
      result = session.execute(inserting_data_query)
      print("Last StockRowId: %s" %result.lastrowid)
    except:
      x=False 

  # Transaction commit karte hain taki data save ho jaye
  session.commit()