from sqlalchemy import text

def inserting_customer_data(engine,data):
  print('data:',data)
  __new_row_id = 0
  if data['customerID']:
    print("TODO")
  else:  
    __insert_formDict_query = text('''
      INSERT INTO customer (name, email, phone, product, processor)
      VALUES (:name, :email, :phone, :product, :processor);
    ''')
   
    try:
      with engine.connect() as conn:
        result = conn.execute(__insert_formDict_query, data)
        conn.commit()
        __new_row_id = result.lastrowid
        
        print("DATA ENTERED")
    except Exception as e:
      print("Error:", e)
  return {'status': 200, 'id': __new_row_id}


def update_customer_data(engine,data):
  print('data:',data)
  data = False
  if data['customerID']: 
    __update_row_qry='''update customer set name='%s', email='%s', phone=%s, product='%s', processor='%s' where id=%s;'''%(
        data['name'],
        data['email'],
        data['phone'],
        data['product'],
        data['processor'],
        data['customerID'],
      )   
    with engine.connect() as conn:
      result = conn.execute(text(__update_row_qry))
      conn.commit() 
      print("DATA Updated")
    lastest_customer_data = get_customer_data_by_id(data['customerID'])   
  return {'status': 200, 'lastest_customer_data': lastest_customer_data}
 

def get_customer_data(engine):
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

def delete_customer_data(engine,id):
  result={"status": 200, "isDeleted": False}
  with engine.connect() as conn:
      delete_customer_by_id_query=text("delete from customer where id=%s;" % id)
      conn.execute(delete_customer_by_id_query) 
      conn.commit() 
      result["isDeleted"]=True
      print("row_id_deleted:", id)
      return result

def get_customer_data_by_id(engine,id):
  customer_dict={"status": 200, "id": False}
  with engine.connect() as conn:
      get_customer_by_id_query=text("select * from customer where id=%s;" % id)
      row_tupple = conn.execute(get_customer_by_id_query).fetchone()
      print(row_tupple)
      if row_tupple: 
        customer_dict={
          "id": row_tupple[0],
          "created_on": row_tupple[1].strftime("%Y-%m-%d %I:%M:%S %p"), #%H = 24 hours %I = 12 hours %p = AM/PM
          "name": row_tupple[2],
          "email":row_tupple[3],
          "phone":row_tupple[4],
          "product":row_tupple[5],
          "processor":row_tupple[6] 
        }
      return customer_dict