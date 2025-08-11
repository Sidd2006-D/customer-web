
from database_handler.db_api import get_session_obj
from database_handler.db_api import insert_fans_into_db
from database_handler.db_api import read_fans_into_db
from database_handler.db_api import insert_stock_of_fans_into_db

def insert_fan_stock(session):
   insert_stock_of_fans_into_db(session)
   print("#Stock Done!")

def insert_fan(session):
  insert_fans_into_db(session) 
  print("#Proess Done!")

def read_fan(session):
  data=read_fans_into_db(session) 
  for row in data:
    print(f"ID: {row.id}, Name: {row.name}, Rate: {row.rate}")

def update_fan(session):
   print("#TODO")

def delete_fan(session):
   print("#TODO")

option_msg='''
Enter your choice:
\t1. Add Fans to stock"
\t2. Insert Fan"
\t3. Update Fan"
\t4. Delete Fan"
\t5. Delete Fan"
'''

def main():
  session = get_session_obj() 
  try:
    choice=int(input(option_msg))
  except:
    choice=None   
  if not choice:
    print("Invalid Choice")  
  while choice:
    if  choice==1:
      insert_fan_stock(session)
    elif choice==2:
      insert_fan(session)
    elif choice==3:
      update_fan(session)
    elif choice==4:
      delete_fan(session)
    elif choice==5:
      read_fan(session)
    else:
      print("Invalid choice")
      break
    try:
      choice=int(input(option_msg))
    except:
      choice=None





if __name__ == '__main__':
  main()