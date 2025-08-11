database_name='code_vault'

from sqlalchemy import text,create_engine

# create_user_table_query='''create table user_data1(
#     id int not null auto_increment,
#     dt DATETIME DEFAULT CURRENT_TIMESTAMP,
#     name varchar(12),
#     email  varchar(30),
#     password varchar(10),
#         PRIMARY KEY(id)
#         )'''
        
engine = create_engine(f'mysql+pymysql://root:mysql_123@localhost/{database_name}')
print('connecting database')








def insert_data():
    with engine.connect() as conn:
        print("connection start")
        choice = str(input("you want to enter data in database? yes or no: ").strip().lower())
        while choice == 'yes':
            name = str(input("Enter name:"))
            email = str(input("Enter email:")) 
            passw = str(input("Enter password:")) 
            query = conn.execute(text(f'''Insert into user_data1
                                     (name,email,password)
                values("{name}","{email}","{passw}")'''))
            choice = str(input("you want to enter data in database? yes or no:"))
            
        conn.commit()
        
        print("data inserted")
        
def fetch_data():
    with engine.connect() as conn:
        print("connection start")
        limit_choice = input("Do you want to limit the number of rows fetched? yes or no: ").strip().lower()
        if limit_choice == "yes":
            try:
                limit = int(input("Enter the limit (number of rows): "))
                query = f"select * from price_list2 limit {limit}"
            except ValueError:
                print("Invalid limit, fetching all rows.")
                query = "select * from price_list2"
        else:
            query = "select * from user_data1"
        result = conn.execute(text(query))
  
        
    
        
        for row in result.fetchall():
            print(row)
        conn.commit()
        
def update_data():
            with engine.connect() as conn:
                print("connection start")
                field = input("Update by (id/name/password): ").strip().lower()
                value = input(f"Enter the {field} to update: ").strip()
                column_to_update = input("Which column do you want to update? (name/email/password): ").strip().lower()
                new_value = input(f"Enter new value for {column_to_update}: ").strip()
                query = text(f"UPDATE user_data1 SET {column_to_update} = :new_value WHERE {field} = :value")
                result = conn.execute(query, {"new_value": new_value, "value": value})
                conn.commit()
                print(f"{result.rowcount} row(s) updated.")

def delete_data():
            with engine.connect() as conn:
                print("connection start")
                field = input("Delete by (id/name/password): ").strip().lower()
                value = input(f"Enter the {field} to delete: ").strip()
                query = text(f"DELETE FROM user_data1 WHERE {field} = :value")
                result = conn.execute(query, {"value": value})
                conn.commit()
                print(f"{result.rowcount} row(s) deleted.")
                
                
print("What do you want to do with database:")
print("\t1. Read data")
print("\t2. Insert data")
print("\t3. Update data")
print("\t4. Delete data")

try:
  option=int(input("Choose any option from above:"))
except:
  option=None   
while option==1 or  2 or 3 or 4 :
    if  option==1:
        fetch_data()
    elif option==2:
        insert_data()
    elif option==3:
        update_data()
    elif option==4:
        delete_data()
    else :
        print("Invalid option")
        break
        
    option=int(input("Choose any option from above:"))

print("connection close")
engine.dispose()