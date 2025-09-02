from database_handler.models import *

def fetch_all_orders_row(session):
  data = []
  with session.begin() as session_obj: 
    for obj in session_obj.query(CustomerOrderModel).all():
      data.append({ 
        "id": obj.id,  
        "date": obj.date.strftime("%d-%m-%Y"),  
        "customer_name": obj.customer_name, 
        "base_price": obj.base_price,
        "product_count": obj.product_count,
        "tax_amount": obj.tax_amount,
        "sub_total": obj.sub_total,
        "grand_total": obj.grand_total,
        })   
  return data


def get_order_details_by_id(session, order_id):
  order_items=[]
  order={
        "id": 0,}
  with session.begin() as session_obj:
    obj = session_obj.get(CustomerOrderModel, order_id)
    print("order:",order)
    order = { 
        "id": obj.id,  
        "date": obj.date.strftime("%d-%m-%Y"),  
        "created_on": obj.created_on.strftime("%d-%m-%Y %H:%M:%S"),  
        "customer_name": obj.customer_name, 
        "base_price": obj.base_price,
        "product_count": obj.product_count,
        "tax_amount": obj.tax_amount,
        "sub_total": obj.sub_total,
        "grand_total": obj.grand_total,
        }
    for item_obj in session_obj.query(CustomerOrderItemsModel).filter_by(order_id=obj.id).all():
      order_items.append({
        'id': item_obj.id,  
        'product_name': item_obj.product_name,  
        'quantity': item_obj.quantity,  
        'rate': item_obj.rate,  
        'tax_rate': item_obj.tax_rate,  
        'tax_amount': item_obj.tax_amount,  
        'line_total': item_obj.line_total,  

      })
    order['order_items']=order_items  
    return order 