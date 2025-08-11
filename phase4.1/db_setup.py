
DATABASE_NAME='code_vault'

from sqlalchemy import create_engine
from sqlalchemy import text
#A VARCHAR(10) column in a database can store up to 10 characters.
create_user_table_query = '''CREATE TABLE test2(
id int NOT NULL AUTO_INCREMENT,
dt DATETIME DEFAULT CURRENT_TIMESTAMP, 
name varchar(10), 
email varchar(30), 
password varchar(10), 
PRIMARY KEY (id)
);
'''
create_customer_table_query='''create table customer(
    id int not null auto_increment,
    created_on DATETIME DEFAULT CURRENT_TIMESTAMP, 
    name varchar(255),
    email  varchar(255), 
    phone  int,
    product  varchar(255),
    processor  varchar(255),  
    PRIMARY KEY(id))'''

create_student_table_query='''create table student(
    id int not null auto_increment,
    created_on DATETIME DEFAULT CURRENT_TIMESTAMP, 
    name varchar(255),
    dob date,
    class  varchar(255),
    PRIMARY KEY(id))'''

# how ""to connect with SqlDB code_vault, in sql maybe there will be multi db but we can connect with 1 db at a time. 
print(" to ConnectingDB")
engine = create_engine('mysql+pymysql://root:mysql_123@localhost/%s' %(DATABASE_NAME))

conn = engine.connect()
print("Connected to DB") 
sql_statmnt = text("drop table customer;")
# result = conn.execute(sql_statmnt)
# conn.execute(text(create_customer_table_query))
sql_statmnt = text("show tables;")
result = conn.execute(sql_statmnt)
for r in result.fetchall():
  print(r[0])
conn.commit()
conn.close()
engine.dispose()