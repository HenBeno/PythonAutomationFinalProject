import mysql.connector


def db_connector():
    return mysql.connector.connect(
        host="jdbc:mysql://sql6.freemysqlhosting.net:3306/sql6455264",
        database='sql6455264',
        user="sql6455264",
        password="iRpvF9AjbD"
    )
