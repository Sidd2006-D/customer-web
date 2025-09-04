from database_handler.models import *


def get_customer_data(session):
    data = []
    with session.begin() as session_obj:
        for obj in session_obj.query(CustomerModel).all():
            data.append({"id": obj.id, "name": obj.name, "basePrice": obj.base_price})
    return data


def create_new_order_with_line_items(session, data):
    result = {'newOrderid': 0}
    item_list = data['item_list'] 
    with session.begin() as session_obj:
      customer = session_obj.get(CustomerModel, data['customer_id'])
      items_object_list = []
      tax_amount=0.0
      sub_total=0.0
      grand_total=0.0
      for d in item_list:
          item=CustomerOrderItemsModel()
          item.product_id = d['id']
          item.product_name = d['name']
          item.quantity = d['qty']
          item.rate = d['rate']
          item.tax_rate = d['tax_rate'] 
          #Exclusive Tax Cal
          item_sub_total = item.rate * item.quantity;
          item.tax_amount = round(item_sub_total * (item.tax_rate / 100), 2)
          item.line_total = round(item_sub_total + item.tax_amount, 2)
          items_object_list.append(item)
          sub_total += item_sub_total
          tax_amount += item.tax_amount
          grand_total += item.line_total
      customer_order=CustomerOrderModel()  
      customer_order.customer_id = customer.id  
      customer_order.customer_name = customer.name  
      customer_order.base_price = data['selectedBasePrice'] 
      customer_order.product_count = items_object_list.__len__()
      customer_order.tax_amount = round(tax_amount,2)
      customer_order.sub_total = round(sub_total,2)
      customer_order.grand_total = round(grand_total, 2)
      local_date = datetime.now().date()
      customer_order.date = local_date
      customer_order.month = local_date.replace(day=1)
      session_obj.add(customer_order) 
      session_obj.flush()
      newOrderid = customer_order.id
      result ['newOrderid']=newOrderid
      for obj in items_object_list:
        obj.order_id = newOrderid
      print(items_object_list)  
      session_obj.bulk_save_objects(items_object_list)
      session_obj.commit()
      return result


def inserting_product_price_list_wise(session, data):
    result = {}
    obj = ProductWisePriceModel()
    obj.rate = data["rate"]
    obj.price_list_id = data["price_list_id"]
    obj.product_id = data["product_id"]
    with session.begin() as session_obj:
        session_obj.add(obj)
        session_obj.flush()
        result = {
            "id": obj.id,
            "price_list_id": obj.price_list_id,
            "product_id": obj.product_id,
            "rate": obj.rate,
        }
    return result


def get_product_data(session):
    data = []
    with session.begin() as session_obj:
        for obj in session_obj.query(ProductModel).all():
            data.append(
                {
                    "id": obj.id,
                    "name": obj.name,
                    # "rate": obj.rate,  # Removed: no longer in ProductModel
                    "taxRate": obj.tax_rate,
                }
            )
    return data


def get_product_wise_price_data(session):
    data = []
    with session.begin() as session_obj:
        for obj in session_obj.query(ProductWisePriceModel).all():
            data.append(
                {
                    "basePriceId": "%s" % obj.price_list_id,
                    "productId": "%s" % obj.product_id,
                    "rate": obj.rate,
                }
            )
    return data


def inserting_customer_info(session, data):
    result = {"newRowId": 0}
    customerObj = CustomerModel()
    customerObj.name = data["name"].upper()
    customerObj.base_price = data["base_price"]

    with session.begin() as session_obj:
        session_obj.add(customerObj)
        session_obj.flush()
        result = {
            "name": customerObj.name,
            "base_price": customerObj.base_price,
            "newRowId": customerObj.id,
        }
        session_obj.commit()
    return result


def get_base_pricescreen_data(session):
    result = {
        "bp_list": [],
        "p_list": [],
    }
    with session.begin() as session_obj:
        bp = []
        for obj in session_obj.query(PriceListModel).all():
            bp.append(
                {
                    "id": obj.id,
                    "name": obj.name,
                }
            )
        result["bp_list"] = bp
        p = []
        for obj in session_obj.query(ProductModel).all():
            p.append(
                {
                    "id": obj.id,
                    "name": obj.name,
                }
            )
        result["p_list"] = p

    return result


def get_baseprices_data(session):
    result = {
        "bp_list": [],
        "p_list": [],
    }
    with session.begin() as session_obj:
        bp = []
        for obj in session_obj.query(PriceListModel).all():
            bp.append(
                {
                    "id": obj.id,
                    "name": obj.name,
                }
            )
        return bp


def get_all_customers(session):
    with session.begin() as session_obj:
        data = []
        for obj in session_obj.query(CustomerModel).all():
            data.append(
                {
                    "id": obj.id,
                    "name": obj.name,
                    "base_price": obj.base_price,
                }
            )

        return data


def inserting_product_info(session, data):
    result = {
        "newRowId": 0,
    }
    productObj = ProductModel()
    productObj.name = data["name"].strip().upper()
    # productObj.rate = data["rate"]  # Removed: no longer in ProductModel
    productObj.tax_rate = data["tax"]
    with session.begin() as session_obj:
        session_obj.add(productObj)
        session_obj.flush()
        result = {
            "newRowId": productObj.id,
            "name": productObj.name,
            # "rate": productObj.rate,  # Removed: no longer in ProductModel
            "tax_rate": productObj.tax_rate,
        }
        session_obj.commit()

    return result


def inserting_baseprice(session, base_price_name):
    result = {
        "newRowId": 0,
    }
    obj = PriceListModel()
    obj.name = base_price_name.strip().upper()
    with session.begin() as session_obj:
        try:
            session_obj.add(obj)
            session_obj.flush()
            result = {
                "newRowId": obj.id,
                "name": obj.name,
            }
            session_obj.commit()
        except Exception as msg:
            print("DB ERROR: ", msg)

    return result
