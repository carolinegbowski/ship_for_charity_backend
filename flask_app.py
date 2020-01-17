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
        SQL = """INSERT INTO np_accounts (
        username, password_hash) VALUES (?, ?);"""
        values = (username, hashed_password)
        cursor.execute(SQL, values)

        SQL = """SELECT pk FROM np_accounts
        WHERE username=? AND password_hash=?;"""

        np_pk = cursor.execute(SQL, values).fetchone()[0]
        return jsonify({"pk": np_pk})
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
        SQL = """SELECT password_hash FROM shipper_accounts
                    WHERE username=?;"""

        password_hash = cursor.execute(SQL, (username,)).fetchone()[0]
        if check_password(password, password_hash):
            SQL = """SELECT pk FROM shipper_accounts
                    WHERE username=?;"""
            shipper_pk = cursor.execute(SQL, (username,)).fetchone()[0]
            return jsonify({"pk": shipper_pk})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/np_login", methods=["POST"])
def np_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    password = bytes(password, "utf-8")
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """SELECT password_hash FROM np_accounts
                        WHERE username=?;"""
        password_hash = cursor.execute(SQL, (username,)).fetchone()[0]
        if check_password(password, password_hash):
            SQL = """SELECT pk FROM np_accounts
                    WHERE username=?;"""
            np_pk = cursor.execute(SQL, (username,)).fetchone()[0]
        return jsonify({"pk": np_pk})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/shipper_new_route", methods=["POST"])
def shipper_new_route():
    data = request.get_json()
    arrival_location = data.get("arrivalLocation")
    arrival_date = data.get("arrivalDate")
    departure_location = data.get("departureLocation")
    departure_date = data.get("departureDate")
    available_containers = data.get("availableContainers")
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO routes (
                departure_location, departure_date,
                arrival_location, arrival_date,
                available_containers )
                VALUES (?, ?, ?, ?, ?); """
        values = (
            arrival_location,
            arrival_date,
            departure_location,
            departure_date,
            departure_location,
            available_containers,
        )
        cursor.execute(SQL, values)
        return jsonify({"SQL": "Success"})
    return jsonify({"SQL": "Error"})


@app.route("api/open_routes", methods=["POST"])
def open_routes():
    pass

@app.route("/api/shipper_previous_routes", methods=["POST"])
def shipper_previous_routes():
    pass


@app.route("/api/np_previous_routes", methods=["POST"])
def np_previous_routes():
    pass


if __name__ == "__main__":
    app.run(debug=True)
