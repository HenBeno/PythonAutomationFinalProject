import mysql.connector

from Utilities.CommOps import get_data

my_db = None


class db_manager:
    @staticmethod
    def setup_db_connection():
        my_db = mysql.connector.connect(
            host=get_data("conf", "db_host"),
            database=get_data("conf", "db_name"),
            user=get_data("conf", "db_name"),
            password=get_data("conf", "db_password"),
        )
        globals()["my_db"] = my_db

    @staticmethod
    def close_connection():
        my_db.close()
