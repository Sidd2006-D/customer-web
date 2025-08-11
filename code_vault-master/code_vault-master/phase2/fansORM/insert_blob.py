from sqlalchemy import create_engine, Column, Integer, LargeBinary
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import insert
from sqlalchemy import desc
# Define your database engine (e.g., SQLite for simplicity)
engine = create_engine('mysql+pymysql://root:ronaldo@localhost/practice') 

# Define your declarative base
Base = declarative_base()

# Define your table with a LargeBinary column for BLOB data
class TestFile(Base):
    __tablename__ = 'test_file2'
    id = Column(Integer, primary_key=True)
    file_content = Column(LargeBinary)

print('# Create the table in the database')
Base.metadata.create_all(engine)
print('# Creation DONE[OK]')


print('# Create a session')
Session = sessionmaker(bind=engine)
session = Session()
print('sessionObj ready')

# Prepare your BLOB data (e.g., from a file or generated)
# For demonstration, let's create some dummy binary data
import datetime
my_string = "This is some binary data for the BLOB column: %s" %(datetime.datetime.now())
binary_data = bytes(my_string, "utf-8")

#with open("result.pdf", 'r') as file_obj:

print('# Construct the insert statement using the table object and insert()')
stmt = insert(TestFile).values(file_content=binary_data)

print('# Execute the statement using session.execute()')
result = session.execute(stmt)

print('# Commit the transaction')
session.commit()

print('# Verify the insertion by retrieving the data')
retrieved_data = session.query(TestFile).first()
if retrieved_data:
    print(f"Retrieved BLOB data: {retrieved_data.file_content}")
else:
    print("no data available") 
# query = session.query(User).order_by(User.name)
# Order by multiple columns
# query = session.query(User).order_by(User.last_name, User.first_name)
# Skip the first 20 users and then return the next 10
# query = session.query(User).offset(20).limit(10)
#for obj in query:
print('# closing session!')
session.close()