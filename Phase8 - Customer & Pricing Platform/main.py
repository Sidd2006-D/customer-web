import eel
from openpyxl import Workbook
from database_handler.db_api import get_session_obj
from database_handler import reports
from masters import master_data_api

session = None


def main():
    session = get_session_obj()
    eel.init("web")
    try:

        @eel.expose  # expose this function to javascript
        def say_hello(arg):
            print("ServerSide:", arg)

        @eel.expose  # expose this function to javascript
        def get_customer_list():
            data = master_data_api.get_all_customers(session)
            return data

        @eel.expose  # expose this function to javascript
        def saving_productInfo(data):
            return master_data_api.inserting_product_info(session, data)

        @eel.expose  # expose this function to javascript
        def saving_base_price(basePriceTitle):
            return master_data_api.inserting_baseprice(session, basePriceTitle)

        @eel.expose  # expose this function to javascript
        def load_baseprice_screen_data():
            return master_data_api.get_base_pricescreen_data(session)

        @eel.expose
        def load_product_screen_data():
            return master_data_api.get_product_data(session)

        @eel.expose
        def saving_customer_info(data):
            print(data)
            return master_data_api.inserting_customer_info(session, data)

        @eel.expose
        def saving_product_price_list_wise(data):
            return master_data_api.inserting_product_price_list_wise(session, data)

        @eel.expose
        def load_customer_screen_data():
            return master_data_api.get_customer_data(session)
        
        @eel.expose
        def create_new_order(data):
         return master_data_api.create_new_order_with_line_items(session, data)
        
        @eel.expose
        def load_order_grid_all_rows():
         return reports.fetch_all_orders_row(session)
       
        @eel.expose
        def get_order_details_by_id(order_id):
         return reports.get_order_details_by_id(session, order_id)
    

        @eel.expose
        def load_master_for_order_cretaion():
            return {
                "customerMasterList": master_data_api.get_customer_data(session),
                "basePriceMasterList": master_data_api.get_baseprices_data(session),
                "productMasterList": master_data_api.get_product_data(session),
                "productWisePriceMasterList": master_data_api.get_product_wise_price_data(
                    session
                ),
            }

        eel.start("home.html", size=(960, 720), port=3030)  # start
        print("closed Succcessfully")
    except Exception as e:
        print("error:", e)


if __name__ == "__main__":
    main()
