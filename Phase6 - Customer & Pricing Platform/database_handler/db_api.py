from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

from database_handler.models import DBBaseHandler

# db_connection_string = 'mysql+pymysql://root:mysql_123@localhost/code_vault'
db_connection_string = "mysql+pymysql://root:ronaldo@localhost/practice"


def get_session_obj():
    print("#DB connection...")
    engine = create_engine(db_connection_string)
    DBBaseHandler.metadata.create_all(engine)
    print("#DB ORM Ready")
    print("#Making session obj")
    Session = sessionmaker(bind=engine)
    return Session 
 
 