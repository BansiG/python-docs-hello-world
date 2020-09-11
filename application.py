import flask
from flask import request, jsonify

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

@app.errorhandler(404) 
def not_found(e): 
  return "404 Not Found"


if __name__ == "__main__":
    app.run() 