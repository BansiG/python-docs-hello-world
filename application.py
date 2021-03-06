import flask
from flask import request, jsonify
# import database
import db2
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
    # result = "SUCESSSSSSS"
    try:
        result = db2.connect(CompanyID, BranchID)
    except Exception as ex:
        result = "FAILUREEEEE"

    return jsonify(result)
"""
@app.route("/connect", methods=['GET'])
def connect():
    CompanyID = int(request.args.get('c'))
    BranchID = int(request.args.get('b'))
    result = database.connect(CompanyID, BranchID)
    return jsonify(result)
"""

@app.route("/getModel", methods=['GET'])
def getModel():
    
    companyID = int(request.args.get('companyID'))
    branchID = int(request.args.get('branchID'))
    try:
        result = db2.getModel(companyID, branchID)
    except Exception as ex:
        result = str(ex)
    return jsonify(result)


@app.route("/saveModel", methods=['GET'])
def saveModel():
    
    companyID = int(request.args.get('companyID'))
    branchID = int(request.args.get('branchID'))
    version = str(request.args.get('Version'))
    try:
        result = db2.saveModel(companyID, branchID, datetime.datetime.now(), version)
    except Exception as ex:
        result = str(ex)
    return jsonify(result)


@app.errorhandler(404) 
def not_found(e): 
  return "404 Not Found"


if __name__ == "__main__":
    app.debug = True
    app.run() 