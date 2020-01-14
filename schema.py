import sqlite3

DBPATH = "final_project.db"


def schema(DBPATH):
    with sqlite3.connect(DBPATH) as connection:
        cursor = connection.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"
        cursor.execute(DROPSQL.format(tablename="np_accounts"))
        SQL = """ CREATE TABLE np_accounts (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name VARCHAR NOT NULL,
                username VARCHAR NOT NULL,
                password_hash VARCHAR
        );"""
        cursor.execute(SQL)

        cursor.execute(DROPSQL.format(tablename="shipper_accounts"))
        SQL = """ CREATE TABLE shipper_accounts (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name VARCHAR,
                username VARCHAR,
                password_hash VARCHAR
        );"""
        cursor.execute(SQL)

        cursor.execute(DROPSQL.format(tablename="routes"))
        SQL = """ CREATE TABLE routes (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                shipper_account_id INTEGER
                start_location VARCHAR,
                stop_location VARCHAR,
                available_containers INTEGER,
                FOREIGN KEY( shipper_account_id) REFERENCES shipper_accounts(pk)
        );"""
        cursor.execute(SQL)

        cursor.execute(DROPSQL.format(tablename="partnerships"))
        SQL = """ CREATE TABLE partnerships (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                np_account_id INTEGER,
                route_id INTEGER,
                containers INTEGER,
                FOREIGN KEY (np_account_id) REFERENCES np_accounts(pk),
                FOREIGN KEY (route_id) REFERENCES routes(pk)
        );"""
        cursor.execute(SQL)


schema(DBPATH)
