import eel
from openpyxl import Workbook 
from database_handler.db_api import get_session_obj
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
        data=master_data_api.get_all_customers(session)
        return data    

      @eel.expose  # expose this function to javascript
      def saving_productInfo(data):
        return master_data_api.inserting_product_info(session,data) 
      
      @eel.expose  # expose this function to javascript
      def saving_base_price(basePriceTitle):
        return master_data_api.inserting_baseprice(session,basePriceTitle) 
      
      @eel.expose  # expose this function to javascript
      def load_baseprice_screen_data():
        return master_data_api.get_product_base_price_data(session) 
      @eel.expose  
      def load_product_screen_data():
        return master_data_api.get_product_data(session) 
        
      @eel.expose
      def saving_customer_info(data):
        print(data)
        return master_data_api.inserting_customer_info(session,data)
      
      @eel.expose
      def saving_product_price_list_wise(data):
        return master_data_api.inserting_product_price_list_wise(session,data)
  
      
      eel.start("home.html", size=(960, 720), port=3030)  # start
      print("closed Succcessfully")
    except Exception as e:
      print("error:", e)


if __name__ == "__main__":
  main()
