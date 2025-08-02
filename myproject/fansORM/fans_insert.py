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
    
# print('# Create the table (Fans) in the database')

Base.metadata.create_all(engine)
print("Table(FANS) is created")

# print("#Creating session")

Session = sessionmaker(bind=engine)
print("orm binded")
session=Session()
print("#Session obj is active")


# Inserting data_______________________________________________________________________________
namevalue=str(input("Enter FAN brand name:"))
ratevalue=int(input("Enter Rate of FAN :"))

print("inserting data into FAN table!")

inserting_data_query = insert(TableFans).values(name=namevalue,rate=ratevalue)

# print('# Execute the statement using session.execute()')
result = session.execute(inserting_data_query)
# ----------------------------------------------------------------------------------------------------



#Commiting transaction
session.commit()

session.close()
