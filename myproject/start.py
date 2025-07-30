import eel
from api_provider.student_crud_api import insert_student_data
from api_provider.student_crud_api import get_student_list_data
from api_provider.student_crud_api import update_student_data_by_id
from api_provider.student_crud_api import delete_student_data_by_id
from api_provider.customer_grid_api import inserting_customer_data
from api_provider.customer_grid_api import get_customer_data_by_id
from api_provider.customer_grid_api import delete_customer_data
from api_provider.customer_grid_api import get_customer_data
from api_provider.customer_grid_api import update_customer_data

eel.init("web")
# Set web files folder and optionally specify which file types to check for eel.expose()
#   *Default allowed_extensions are: ['.js', '.html', '.txt', '.htm', '.xhtml']
#eel.init('web', allowed_extensions=['.js', '.html'])

from sqlalchemy import text,create_engine
# mysql_conn_url = 'mysql+pymysql://root:ronaldo@localhost/practice'  # db name is 'practice', password is 'ronaldo'
# engine = create_engine(mysql_conn_url)
print('connecting database')
# ...existing code...
db_user = 'root'
db_password = 'ronaldo'
db_host = 'localhost'
db_name = 'practice'
mysql_conn_url = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
engine = create_engine(mysql_conn_url)
# ...existing code...
# day 3

@eel.expose
def get_all_students():
  return get_student_list_data(engine)


@eel.expose
def update_student():
  return update_student_data_by_id(engine)

@eel.expose
def delete_student():
  return delete_student_data_by_id(engine)

  
@eel.expose
def insert_student(formData_dict):
  return insert_student_data(engine, formData_dict)

@eel.expose
def insert_customer(formData_dict):
   return inserting_customer(engine, formData_dict)

@eel.expose
def update_customer(formData_dict):
  return update_customer_data(engine, formData_dict)

#day 4th 16thJuly25
@eel.expose
def get_list_of_all_customer():
  return get_customer_data(engine)

@eel.expose
def get_customer_by_id(id):
  return get_customer_data_by_id(engine,id)
    
@eel.expose
def delete_customer_by_id(id):
  return delete_customer_data(engine,id)
   
# end of business logix
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
    
