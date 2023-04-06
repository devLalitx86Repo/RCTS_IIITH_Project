'''
Author: Lalit Gupta
Discription: Rest API for the application
Endpoint: /custom, /health, 
'''
from flask import Flask, Response, jsonify, request

#Local imports
from .errors import errors
# from db_connection import Database
from .db_helper import DbHelper

app = Flask(__name__)
app.register_blueprint(errors)

DbHelper = DbHelper()

@app.route("/")
def index():
    return Response("Hello, world!", status=200)


@app.route("/custom", methods=["POST"])
def custom():
    payload = request.get_json()

    if payload.get("say_hello") is True:
        output = jsonify({"message": "Hello!"})
    else:
        output = jsonify({"message": "..."})

    return output


@app.route("/health")
def health():
    return Response("OK", status=200)

@app.route("/records", methods=["GET", "POST"])
def record_action():
    if request.method == "GET":
        return DbHelper.list_docs()
    # elif request.method == "POST":
    #     return DbHelper.create_doc()
