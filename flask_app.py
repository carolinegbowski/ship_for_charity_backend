from flask import Flask, request, jsonify
from flask_cors import CORS
from util import hash_password, check_password
from sqlite3 import connect

app = Flask(__name__)
CORS(app)
DBPATH = "final_project.db"


@app.route("/api/np_create_account", methods=["POST"])
def create_account():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    password = bytes(password, "utf-8")
    hashed_password = hash_password(password)
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO shipper_accounts (
        username, password_hash) VALUES (?, ?);"""
        values = (username, hashed_password)
        cursor.execute(SQL, values)

        SQL = """SELECT pk FROM shipper_accounts
        WHERE username=?;"""

        np_pk = cursor.execute(SQL, values).fetchone()
        return jsonify({"pk": np_pk})
        return jsonify({"non_profit_pk": np_pk})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/shipper_create_account", methods=["POST"])
def shipper_account():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    password = bytes(password, "utf-8")
    hashed_password = hash_password(password)
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO shipper_accounts (
        username, password_hash) VALUES (?, ?);"""
        values = (username, hashed_password)
        cursor.execute(SQL, values)

        SQL = """SELECT pk FROM shipper_accounts
        WHERE username=? AND password_hash=?;"""

        shipper_pk = cursor.execute(SQL, values).fetchone()[0]
        return jsonify({"pk": shipper_pk})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/shipper_login", methods=["POST"])
def shipper_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    password = bytes(password, "utf-8")
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        password_hash = """SELECT hashed_password FROM shipper_accounts
                    WHERE username=?;"""

        password_hash = cursor.execute(password_hash,).fetchone()[0]
        if check_password(password, password_hash):
            SQL = """SELECT pk FROM shipper_accounts
                    WHERE username=?;"""
            shipper_pk = cursor.execute(SQL, (username,)).fetchone()[0]
            return jsonify({"pk": shipper_pk})
            return jsonify({"shipper_pk": shipper_pk})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/np_login", methods=["POST"])
def np_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    password = bytes(password, "utf-8")
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        password_hash = """SELECT hashed_password FROM shipper_accounts
                        WHERE username=?;"""
        password_hash = cursor.execute(password_hash,).fetchone()[0]
        if check_password(password, password_hash):
            SQL = """SELECT pk FROM shipper_accounts
                    WHERE username=?;"""
            np_pk = cursor.execute(SQL, (username,)).fetchone()[0]
        return jsonify({"pk": np_pk})

        return jsonify({"non_profit_pk": np_pk})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/shipper_previous_routes", methods=["POST"])
def shipper_previous_routes():
    pass


@app.route("/api/np_previous_routes", methods=["POST"])
def np_previous_routes():
    pass


@app.route("/api/shipper_open_routes", methods=["POST"])
def shipper_open_routes():
    pass


if __name__ == "__main__":
    app.run(debug=True)
