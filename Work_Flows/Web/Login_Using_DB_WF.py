import allure
from smart_assertions import soft_assert

from Utilities.DB_Manager import db_connector
from Work_Flows.Web.Login_WF import login_wf


class login_use_database_wf:
    @staticmethod
    @allure.step("Login with DB")
    def log_in_db():
        login_use_database_wf.db_connector()

    @staticmethod
    @allure.step("starting DB Connection")
    def db_connector():
        mydb = db_connector()
        query = "SELECT user_name, password FROM Employees WHERE comments ='correct'"
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        soft_assert(
            login_wf.login_and_verify(my_result[0], my_result[1]) == my_result[2],
            "Login Fail in: " + my_result[0] + " " + my_result[1],
        )
