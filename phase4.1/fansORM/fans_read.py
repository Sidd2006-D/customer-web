from sqlalchemy import create_engine, Column, Integer, LargeBinary,String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import insert
from sqlalchemy import desc

# Define your database engine (e.g., SQLite for simplicity)
engine = create_engine('mysql+pymysql://root:ronaldo@localhost/practice') 

# Define your declarative base
Base = declarative_base()

class TableFans(Base):
    __tablename__ = 'fans'
    id = Column(Integer,primary_key=True)
    name=Column(String(255))
    rate = Column(Integer)
    # def _repr_(self):
    #     return f"<TableFans(id={self.id!r}, name={self.name!r}, rate={self.rate!r})>"
    
Base.metadata.create_all(engine)
print("Table(FANS) is created")

# print("#Creating session")

Session = sessionmaker(bind=engine)
print("orm binded")
session=Session()
print("#Session obj is active")


# Reading data-------------------------------------------------------------------------------------------
# result= session.query(TableFans).order_by(TableFans.id).all()

# for tableFanObj in result:
#     print('tableFanObj.id:',tableFanObj.id)
#     print('tableFanObj.name:',tableFanObj.name)
#     print('tableFanObj.rate:',tableFanObj.rate)
    

print("#Table with off set")
# read_offset_query = session.query(TableFans).offset(20).limit(10)



result = session.query(TableFans).offset(5).limit(10).all()
for tableFanObj in result:
    print('tableFanObj.id:', tableFanObj.id)
    print('tableFanObj.name:', tableFanObj.name)
    print('tableFanObj.rate:', tableFanObj.rate)




# ----------------------------------------------------------------------------------------------------



#Commiting transaction


session.close()
