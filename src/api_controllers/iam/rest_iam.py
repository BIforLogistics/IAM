import logging
from flask import Blueprint, Flask, Response, jsonify, request
from libs.models import db
from configs.flask_config import APP
from libs.iam_process.iam_validations import IAM_Register
ROUTE = Blueprint('ROUTE',__name__)

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

@APP.before_first_request
def create_table():
    db.create_all()

@ROUTE.route('/user', methods=['GET'])
def get_user():
    '''method to get all users in database'''
    try:
        from libs.models import User_Model
        logging.info(" * GET call")
        return jsonify({'Users': User_Model.get_all_users()})
    except:
        resp = jsonify({"message": "Internal server error"})
        resp.status_code = 500 
        return resp

@ROUTE.route('/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    try:
        from libs.models import User_Model
        return_value = User_Model.get_user_by_id(id)
        return jsonify(return_value)
    except:
        resp = jsonify({"message": "Internal server error"})
        resp.status_code = 500   
        return resp

@ROUTE.route('/user', methods=['POST'])
def add_user():
    '''method to add user in our database'''
    try:
        from libs.models import User_Model
        request_data = request.get_json()
        datatype_check = IAM_Register(fname=request_data["fname"], lname=request_data["lname"],
        ph_no=request_data["ph_no"], email=request_data["email"], passwd=request_data["passwd"],
        re_passwd=request_data["re_passwd"], role=request_data["role"]).validate_data_type()
        if datatype_check:
            User_Model.add_usr(request_data["fname"], request_data["lname"], request_data["ph_no"], request_data["email"], request_data["passwd"], request_data["re_passwd"])
            response = Response("User Added", 201, mimetype='application/json')
            logging.info(" * User Added")
            return response
        else:
            response = Response("Validation failed", 400, mimetype='application/json')
            logging.info(" * validation failed")
            return response
    except Exception:
        resp = jsonify({"message": "Internal server error"})
        resp.status_code = 500   
        return resp

@ROUTE.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    '''method to update existing user'''
    try:
        from libs.models import User_Model
        request_data = request.get_json()

        User_Model.update_user(id, request_data['fname'], request_data['lname'], request_data["ph_no"], request_data["email"], request_data["passwd"], request_data["re_passwd"])
        response = Response("User Updated", 201, mimetype='application/json')
        logging.info(" * User Updated")
        return response
    except:
        resp = jsonify({"message": "Internal server error"})
        resp.status_code = 500   
        return resp

@ROUTE.route('/user/<int:id>', methods=['DELETE'])
def remove_user(id):
    '''method to delete existing user'''
    try:
        from libs.models import User_Model
        User_Model.delete_user(id)
        response = Response("User Deleted", 200, mimetype='application/json')
        logging.info(" * User Deleted")
        return response
    except:
        resp = jsonify({"message": "Internal server error"})
        resp.status_code = 500   
        return resp