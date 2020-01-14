from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlite3 import connect

app = Flask(__name__)
CORS(app)
DBPATH = "final_project.db"


@app.route("/api/np_create_account", methods=["POST"])
def create_account():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO shipper_accounts (
        username, password) VALUES (?, ?);"""
        values = (username, password)
        cursor.execute(SQL, values)

        SQL = """SELECT pk FROM shipper_accounts
        WHERE username=? AND password=?;"""

        np_pk = cursor.execute(SQL, values).fetchone()[0]
        return jsonify({"non_profit_pk": np_pk})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/shipper_create_account", methods=["POST"])
def shipper_account():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO shipper_accounts (
        username, password) VALUES (?, ?);"""
        values = (username, password)
        cursor.execute(SQL, values)

        SQL = """SELECT pk FROM shipper_accounts
        WHERE username=? AND password=?;"""

        shipper_pk = cursor.execute(SQL, values).fetchone()[0]
        return jsonify({"shipper_pk": shipper_pk})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/shipper_login", methods=["POST"])
def shipper_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """SELECT pk FROM shipper_accounts
        WHERE username=? AND password=?;"""
        shipper_pk = cursor.execute(SQL, (username, password)).fetchone()[0]
        return jsonify({"shipper_pk": shipper_pk})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/np_login", methods=["POST"])
def np_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """SELECT username, password FROM np_accounts
        WHERE username=?;"""
        np_pk = cursor.execute(SQL, (username, password)).fetchone()[0]
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
