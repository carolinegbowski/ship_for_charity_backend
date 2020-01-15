from sqlite3 import connect
from util import hash_password, check_password

DBPATH = "final_project.db"


def seed(dbpath=DBPATH):
    with connect(DBPATH) as connection:
        username = "test"
        password = b"password"
        hashed_password = hash_password(password)
        cursor = connection.cursor()
        SQL = """INSERT INTO shipper_accounts (
        username, password_hash) VALUES (?, ?);"""
        values = (username, hashed_password)
        cursor.execute(SQL, values)


def password_check(dbpath=DBPATH):
    with connect(DBPATH) as connection:
        username = "test"
        password = b"password"
        cursor = connection.cursor()
        sql = """SELECT password_hash FROM shipper_accounts WHERE username=?"""

        password_hash = cursor.execute(sql, (username,)).fetchone()[0]
        print(password_hash)
        password_hash = check_password(password, password_hash)
        if password_hash:
            pk = """ SELECT pk FROM shipper_accounts WHERE username=?"""
            user_pk = cursor.execute(pk, (username,)).fetchone()[0]
            print(user_pk)


password_check()
