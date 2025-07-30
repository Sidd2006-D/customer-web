from sqlalchemy import text
from datetime import datetime
def calculate_age(dob, today):
    """
    Calculates the age in years from a given birth date.

    Args:
        dob (date): A datetime.date object representing the birth date.

    Returns:
        int: The age in full years.
    """ 
    age = today.year - dob.year
    
    # Adjust age if the birthday in the current year has not yet occurred
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age

def get_student_list_data(engine):
  student_list=[]
  student_dict={}
  print('get_student_list_data')
  try:
      with engine.connect() as conn:
        getData_query=text('select * from student;')
        result=conn.execute(getData_query)
        current_date_time = datetime.now() # get system current datetime
        today = current_date_time.date() #getting date from datetime object
        for row_tupple in result: 
          dob = row_tupple[3]
          age=calculate_age(dob, today)
          student_dict={
          "id": row_tupple[0],
          # "created_on": row_tupple[1], # because 2nd col is datetime obj in sql and js will not accept it so we use here string convesion 
          "created_on": row_tupple[1].strftime("%Y-%m-%d %I:%M:%S %p"), #%H = 24 hours %I = 12 hours %p = AM/PM
          "name": row_tupple[2],
          "dob": dob.strftime("%Y-%m-%d"),
          "class_val": row_tupple[4],
          "age": "%s Yr" %age,
          } 
          student_list.append(student_dict)
  except Exception as e:
    print("Error:", e)
  return student_list

  

def get_student_data_by_id(engine, id):
  result={"status": 200, "isDeleted": False}
  print('get_student_data_by_id:',id)
  #TODO
  return result

def insert_student_data(engine, data):
  __new_row_id = 0
  print('data:',data)
  with engine.connect() as conn:
    insert_query=text('insert into student(name, class, dob) values("%s", "%s", "%s");' %(
      data['name'],
      data['class'],
      data['dob'], 
      ) 
      )
    result=conn.execute( insert_query)
    print("inserted successfully")
    conn.commit()  
    __new_row_id = result.lastrowid
         
  return result,__new_row_id


def update_student_data_by_id(engine, data):
  __new_row_id = 0
  print('data:',data)
  with engine.connect() as conn:

    update_query=text('update student set name="%s",class="%s",dob="%s" where id="%s";'%(
      data['name'],
      data['class'],
      data['dob'],
    )
    )
    result=conn.execute(update_query)
    conn.commit()
    __new_row_id = result.lastrowid
  
    return result,__new_row_id
  # 
  
def delete_student_data_by_id(engine,id):
  
  result={"status": 200, "isDeleted": False}
  print('deleting_student_data_by_id:')
  delete_query=text('delete from student where id=:id;')
  result=conn.execute(delete_query)
  conn.commit()
  __new_row_id = result.lastrowid
  
 
  return result