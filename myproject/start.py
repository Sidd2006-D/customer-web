import eel
eel.init("web")
# Set web files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
#eel.init('web', allowed_extensions=['.js', '.html'])

database_name='practice'

from sqlalchemy import text,create_engine

engine = create_engine(f'mysql+pymysql://root:ronaldo@localhost/{database_name}')
print('connecting database')

# day 3
@eel.expose
def savecustomer(formData_dict):
  print('formData_dict:',formData_dict)
  __new_row_id = 0
  __insert_formDict_query = text('''
    INSERT INTO customer (name, email, phone, product, processor)
    VALUES (:name, :email, :phone, :product, :processor)
  ''')
  try:
    with engine.connect() as conn:
      result = conn.execute(__insert_formDict_query, formData_dict)
      conn.commit()
      __new_row_id = result.lastrowid
      
      print("DATA ENTERED")
  except Exception as e:
    print("Error:", e)
  return {'status': 200, 'id': __new_row_id}
 
#day 4th 16thJuly25
@eel.expose
def get_list_of_all_customer():
  customer_list = []
  try:
    with engine.connect() as conn:
      for row_tupple in  conn.execute(text("select * from customer;")): 
        customer_dict={
          "id": row_tupple[0],
          # "created_on": row_tupple[1], # because 2nd col is datetime obj in sql and js will not accept it so we use here string convesion 
          "created_on": row_tupple[1].strftime("%Y-%m-%d %I:%M:%S %p"), #%H = 24 hours %I = 12 hours %p = AM/PM
          "name": row_tupple[2],
          "email":row_tupple[3],
          "phone":row_tupple[4],
          "product":row_tupple[5],
          "processor":row_tupple[6]
        }
        customer_list.append(customer_dict)
  except Exception as e:
    print("Error:", e)
  return customer_list


@eel.expose
def get_stu_info():
  student_list = []
  try:
    with engine.connect() as conn:
      for row_tupple in  conn.execute(text("select * from student;")): 
        student_dict={
          "id": row_tupple[0],
          # "created_on": row_tupple[1], # because 2nd col is datetime obj in sql and js will not accept it so we use here string convesion 
          "created_on": row_tupple[1].strftime("%Y-%m-%d %I:%M:%S %p"), #%H = 24 hours %I = 12 hours %p = AM/PM
          "name": row_tupple[2],
          "class":row_tupple[3],
          "section":row_tupple[4],
          "roll_no":row_tupple[5],
          
        }
        student_list.append(student_dict)
  except Exception as e:
    print("Error:", e)
  return student_list
# Set web files folder

@eel.expose
def get_customer_by_id(id):
  customer_list=[]
  with engine.connect() as conn:
      get_customer_by_id_query=text("select * from customer where id={id};")
      
      for row_tupple in  conn.execute(get_customer_by_id_query): 
        customer_dict={
          "id": row_tupple[0],
          # "created_on": row_tupple[1], # because 2nd col is datetime obj in sql and js will not accept it so we use here string convesion 
          "created_on": row_tupple[1].strftime("%Y-%m-%d %I:%M:%S %p"), #%H = 24 hours %I = 12 hours %p = AM/PM
          "name": row_tupple[2],
          "class":row_tupple[3],
          "section":row_tupple[4],
          "roll_no":row_tupple[5],
        }
      
        customer_list.append(customer_dict)
        return customer_list
      





try:

    @eel.expose             #expose this function to javascript
    def  say_hello(arg):
         print('ServerSide:',arg)
    screen_w=960
    screen_h=720

    eel.start('home.html',size=(screen_w,screen_h),port=2021)#start
    print("closed Succcessfully")
except Exception as  e:
    print('error:',e)
    
