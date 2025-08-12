import eel
import csv
import io
import base64
from database_handler.db_api import get_session_obj
from database_handler.db_api import read_fans_from_db
from database_handler.db_api import insert_fans_into_db
from database_handler.db_api import update_fan_stock_into_db_add
from database_handler.db_api import update_fan_stock_into_db_reduce
from database_handler.db_api import delete_fan_stock_into_db
from database_handler.db_api import file_read_from_db

session = None


def main():
    session = get_session_obj()
    # end of business logix

    eel.init("web")
    try:

        @eel.expose  # expose this function to javascript
        def say_hello(arg):
            print("ServerSide:", arg)

        @eel.expose  # expose this function to javascript
        def get_all_fan_data():
            return read_fans_from_db(session)

        @eel.expose
        def inserting_data(fan_dict):
            return insert_fans_into_db(session, fan_dict)

        @eel.expose
        def file_read(fileData, fileName, fileType):
            print("file_read")
            print(fileData, fileName, fileType)
            # 1. Extract the Base64 encoded string
            base64_string = fileData.split(",")[1]

            # 2. Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_string)
            decoded_string = decoded_bytes.decode(
                "utf-8"
            )  # Assuming UTF-8 encoding for CSV

            # 3. Create a file object
            csv_file_obj = io.StringIO(decoded_string)

            # 4. Parse the CSV data
            csv_reader = csv.reader(csv_file_obj)

            # Read header
            header = next(csv_reader)
            print(f"Header: {header}")

            # Read rows
            allFileDta = []
            for row in csv_reader:
                d = {"name": row[0], "price": int(row[1])}
                # d = {}
                # for index, h in enumerate(header):
                #     d[h] = row[index]
                allFileDta.append(d)
            print(f"Rows: {allFileDta}")
            return allFileDta  # file_read_from_db(session, file)

        @eel.expose
        def update_fan_stock_add(data):
            return update_fan_stock_into_db_add(session, data)

        @eel.expose
        def update_fan_stock_reduce(data):
            return update_fan_stock_into_db_reduce(session, data)

        @eel.expose
        def delete_fan_stock(data):
            return delete_fan_stock_into_db(session, data)

        screen_w = 960
        screen_h = 720

        eel.start("home.html", size=(screen_w, screen_h), port=3030)  # start
        print("closed Succcessfully")
    except Exception as e:
        print("error:", e)


if __name__ == "__main__":
    main()
