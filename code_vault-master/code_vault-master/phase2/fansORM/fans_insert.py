from sqlalchemy import create_engine, Column, Integer, LargeBinary, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import insert
from sqlalchemy import desc

engine = create_engine('mysql+pymysql://root:ronaldo@localhost/practice') 

# ORM ke liye base class define karte hain
Base = declarative_base()

# TableFans class banate hain, jo fans table ko represent karta hai
class TableFans(Base):
    __tablename__ = 'fans'
    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String(255))              # Fan ka brand name
    rate = Column(Integer)                  # Fan ka rate

# Table create karte hain agar exist nahi karti
Base.metadata.create_all(engine)
print("Table(FANS) is created")


Session = sessionmaker(bind=engine)     # Session banate hain database ke liye
print("orm binded")
session = Session()                     # Session object activate karte hain
print("#Session obj is active")


choice = int(input("How many data you want to enter:"))


for i in range(choice):

    namevalue = str(input("Enter FAN brand name:"))
    ratevalue = int(input("Enter Rate of FAN :"))

    print("inserting data into FAN table!")

    # Insert query banate hain ORM ke through
    inserting_data_query = insert(TableFans).values(name=namevalue, rate=ratevalue)

    result = session.execute(inserting_data_query)
    

# Transaction commit karte hain taki data save ho jaye
session.commit()
    

