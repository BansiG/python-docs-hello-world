import flask
from flask import request, jsonify
# import database
import datetime

app = flask.Flask(__name__)
# app.config["DEBUG"] = False

@app.route("/")
def index():
    return "Hello !!!"

@app.route("/api", methods=['GET'])
def initialize():
    CompanyID = int(request.args.get('companyID'))
    BranchID = int(request.args.get('branchID'))
    return "sucessssssss"

# @app.route("/api/initialize", methods=['POST'])
# def initialize():
#     data = request.get_json()
#     companyID = int(data['companyID'])
#     branchID = int(data['branchID'])
#     try:
#         sqltable_creator.create_sql_table(companyID, branchID)
#     except:
#         return "Table already initialized"
#     return "Table created"

# @app.route("/api/getModel", methods=['GET'])
# def getModel():
    
#     companyID = int(request.args.get('companyID'))
#     branchID = int(request.args.get('branchID'))
#     result = database.getModel(companyID, branchID)
#     return jsonify(result)


# @app.route("/api/saveModel", methods=['GET'])
# def saveModel():
    
#     companyID = int(request.args.get('companyID'))
#     branchID = int(request.args.get('branchID'))
#     version = str(request.args.get('Version'))
#     result = database.insert_row(companyID, branchID, datetime.datetime.now(), version)
#     return jsonify(result)


@app.errorhandler(404) 
def not_found(e): 
  return "404 Not Found"


if __name__ == "__main__":
    app.run() 