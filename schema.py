from sqlite3 import connect

DBPATH = "final_project.db"


def schema(dbpath=DBPATH):
    with connect(dbpath) as connection:
        cursor = connection.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"
        cursor.execute(DROPSQL.format(tablename="np_accounts"))
        SQL = """ CREATE TABLE np_accounts (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name VARCHAR,
                ein VARCHAR,
                email VARCHAR NOT NULL UNIQUE,
                password_hash VARCHAR
        );"""
        # username VARCHAR NOT NULL UNIQUE,

        cursor.execute(SQL)

        cursor.execute(DROPSQL.format(tablename="shipper_accounts"))
        SQL = """ CREATE TABLE shipper_accounts (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name VARCHAR,
                email VARCHAR NOT NULL UNIQUE,
                password_hash VARCHAR
        );"""
        # username VARCHAR NOT NULL UNIQUE,

        cursor.execute(SQL)

        cursor.execute(DROPSQL.format(tablename="routes"))
        SQL = """ CREATE TABLE routes (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                shipper_account_id INTEGER,
                departure_location VARCHAR,
                departure_date INTEGER,
                arrival_location VARCHAR,
                arrival_date INTEGER,
                total_containers INTEGER,
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


schema()
