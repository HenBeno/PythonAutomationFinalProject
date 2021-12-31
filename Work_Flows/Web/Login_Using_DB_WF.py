import allure
from smart_assertions import soft_assert

from Utilities.CommOps import get_data
from Utilities.DB_Manager import db_manager
from Work_Flows.Web.Login_WF import login_wf

my_db = None


class login_use_database_wf:
    @staticmethod
    @allure.step("Login with DB WF")
    def log_in_db():
        login_use_database_wf.db_connector()
        login_use_database_wf.get_data_by_sql()
        login_use_database_wf.close_db_connection()

    @staticmethod
    @allure.step("Start db connection")
    def db_connector():
        globals()["my_db"] = db_manager.setup_db_connection()

    @staticmethod
    @allure.step("Get data from db and login")
    def get_data_by_sql():
        query = get_data("Select_Statement")
        my_cursor = my_db.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        soft_assert(
            login_wf.login_and_verify(my_result[0], my_result[1]) == my_result[2],
            "Login Fail in: " + my_result[0] + " " + my_result[1],
        )

    @staticmethod
    @allure.step("Close db Connection")
    def close_db_connection():
        db_manager.close_connection()
