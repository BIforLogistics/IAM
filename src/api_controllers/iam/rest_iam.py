import logging
from flask import Blueprint, Flask, Response, jsonify, request
from libs.models import db
from configs.flask_config import APP

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
def add_emp():
    '''method to add user in our database'''
    try:
        from libs.models import User_Model
        request_data = request.get_json()
        User_Model.add_usr(request_data["fname"], request_data["lname"], request_data["ph_no"], request_data["email"], request_data["passed"], request_data["re_passwd"])
        response = Response("User Added", 201, mimetype='application/json')
        logging.info(" * User Added")
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
        User_Model.update_user(id, request_data['fname'], request_data['lname'], request_data["ph_no"], request_data["email"], request_data["passed"], request_data["re_passwd"])
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