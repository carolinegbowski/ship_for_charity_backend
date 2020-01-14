from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/create_account", methods=["POST"])
def create_account():
    pass 


@app.route("/api/shipper_login", methods=["POST"])
def shipper_login():
    pass


@app.route("/api/NPlogin", methods=["POST"])
def NP_login():
    pass


@app.route("/api/shipper_previous_routes", methods=["POST"])
def shipper_previous_routes():
    pass


@app.route("/api/NP_previous_routes", methods=["POST"])
def NP_previous_routes():
    pass


@app.route("/api/shipper_open_routes", methods=["POST"])
def shipper_open_routes():
    pass


if __name__ == "__main__":
    app.run(debug=True)
