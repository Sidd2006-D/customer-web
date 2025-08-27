from database_handler.models import *


def get_customer_data(session):
    data = []
    with session.begin() as session_obj:
        for obj in session_obj.query(CustomerModel).all():
            data.append({"id": obj.id, "name": obj.name, "basePrice": obj.base_price})
    return data


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
                    "rate": obj.rate,
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
    productObj.rate = data["rate"]
    productObj.tax_rate = data["tax"]
    with session.begin() as session_obj:
        session_obj.add(productObj)
        session_obj.flush()
        result = {
            "newRowId": productObj.id,
            "name": productObj.name,
            "rate": productObj.rate,
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
