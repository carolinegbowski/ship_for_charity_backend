from flask import Flask, request, jsonify
from flask_cors import CORS
from util import hash_password, check_password
from sqlite3 import connect
import datetime

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
    shipper_account_id = data.get("shipperAccountID")
    departure_location = data.get("departureLocation")
    departure_date = data.get("departureDate")
    date = int(datetime.datetime.strptime(departure_date, "%m/%d/%y").strftime("%s"))
    arrival_location = data.get("arrivalLocation")
    arrival_date = data.get("arrivalDate")
    _date = int(datetime.datetime.strptime(arrival_date, "%m/%d/%y").strftime("%s"))
    available_containers = data.get("availableContainers")
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """INSERT INTO routes ( shipper_account_id,
                departure_location, departure_date,
                arrival_location, arrival_date,
                available_containers, total_containers )
                VALUES (?, ?, ?, ?, ?, ?, ?); """
        values = (
            shipper_account_id,
            departure_location,
            date,
            arrival_location,
            _date,
            available_containers,
            available_containers,
        )
        cursor.execute(SQL, values)
        return jsonify({"SQL": "Success"})
    return jsonify({"SQL": "Error"})


@app.route("/api/np_search_routes", methods=["POST"])
def open_routes():
    data = request.get_json()
    departure_location = data.get("departureLocation")
    arrival_location = data.get("arrivalLocation")
    arrival_date = data.get("arrivalDate")
    date = int(datetime.datetime.strptime(arrival_date, "%m/%d/%y").strftime("%s"))
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """ SELECT * FROM routes WHERE departure_location=?
                AND arrival_location=? AND arrival_date < ?
                AND departure_date > strftime('%s'); """
        values = (departure_location, arrival_location, date)
        np_open_routes = cursor.execute(SQL, values).fetchall()
        return jsonify({"Non-profit Open routes": np_open_routes})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/np_new_route", methods=["POST"])
def np_new_route():
    pass


@app.route("/api/shipper_previous_routes", methods=["POST"])
def shipper_previous_routes():
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """SELECT * FROM routes WHERE departure_date < strftime('%s');"""
        routes = cursor.execute(SQL,).fetchall()
        return jsonify({"Routes": routes})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/shipper_open_routes", methods=["POST"])
def shipper_open_routes():
    data = request.get_json()
    shipper_account_id = data.get("shipperAccountID")
    departure_date = data.get("departureDate")
    date = int(datetime.datetime.strptime(departure_date, "%m/%d/%y").strftime("%s"))
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """ SELECT * FROM routes WHERE shipper_account_id=?
                AND departure_date > strftime('%s')
                AND available_containers > 0;"""
        values = (shipper_account_id, departure_date, date)
        shipper_open_routes = cursor.execute(SQL, values).fetchall()
        return jsonify({"Shipper open routes": shipper_open_routes})
    return jsonify({"SQL": "ERROR"})


@app.route("/api/np_previous_routes", methods=["POST"])
def np_previous_routes():
    data = request.get_json()
    np_account_id = data.get("npAccountID")
    with connect(DBPATH) as connection:
        cursor = connection.cursor()
        SQL = """ SELECT * FROM routes JOIN partnerships ON routes.pk = partnerships.route_id
                WHERE np_account_id=?;"""
        values = (np_account_id,)
        np_previous_routes = cursor.execute(SQL, values).fetchall()
        return jsonify({"NP previous routes": np_previous_routes})
    return jsonify({"SQL": "ERROR"})


if __name__ == "__main__":
    app.run(debug=True)
