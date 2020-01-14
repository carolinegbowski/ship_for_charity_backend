from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlite3 import connect

app = Flask(__name__)
CORS(app)
DBPATH = "final_project.db"


@app.route("/api/create_account", methods=["POST"])
def create_account():
    pass


@app.route("/api/shipper_login", methods=["POST"])
def shipper_login():
    pass


@app.route("/api/np_login", methods=["POST"])
def np_login():
    pass


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
