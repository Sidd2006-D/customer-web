# To run this project you need to install the following packages:
#     pip install eel , sqlalchemy ,pymysql

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

from database_handler.models import DBBaseHandler

# db_connection_string = 'mysql+pymysql://root:mysql_123@localhost/code_vault'
db_connection_string = "mysql+pymysql://root:ronaldo@localhost/practice"

# username = "root"
# password = "ronaldo"
# host = "localhost"
# database = "practice"
# db_type = "mysql+pymysql"

# db_connection_string = f"{db_type}://{username}:{password}@{host}/{database}"

def get_session_obj():
    print("#DB connection...")
    engine = create_engine(db_connection_string)
    DBBaseHandler.metadata.create_all(engine)
    print("#DB ORM Ready")
    print("WELCOME TO MY PROJECT")
    Session = sessionmaker(bind=engine)
    return Session 



 
 