import rsa
import logging
import traceback
from flask import Blueprint, Flask, Response, jsonify, request
from libs.models import db
from configs.flask_config import APP

ROUTE = Blueprint('ROUTE',__name__)

publicKey, privateKey = rsa.newkeys(512)

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
        traceback.print_exc()
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
        traceback.print_exc()
        resp = jsonify({"message": "Internal server error"})
        resp.status_code = 500   
        return resp
@ROUTE.route('/userlogin', methods=['POST'])
def user_login():
    try:
        request_data = request.get_json()
        user_name = request_data["id"]
        password = request_data["passwd"]
        from libs.models import User_Model
        return_value = User_Model.get_user_by_id(user_name)
        if password == return_value["passwd"]:
            resp = jsonify({"message": "Successfully logged in"})
            resp.status_code = 200   
            return resp
        else:
            resp = jsonify({"message": "Incorrect password"})
            resp.status_code = 400   
            return resp
    
    except Exception as e:
        logging.info(f"{e}")
        resp = jsonify({"message": "Internal server error"})
        resp.status_code = 500   
        return resp

@ROUTE.route('/user', methods=['POST'])
def add_user():
    '''method to add user in our database'''
    try:
        from libs.models import User_Model
        request_data = request.get_json()
        user_name = request_data["id"]
        return_value = User_Model.get_user_by_id(user_name)
        if return_value:
            resp = jsonify({"message": "Id already there"})
            resp.status_code = 400
            return resp
        logging.info(request_data["passwd"])
        password = request_data["passwd"]
        password = str(rsa.encrypt(password.encode(),publicKey))
        logging.info(password)
        re_password = request_data["re_passwd"]
        re_password = rsa.encrypt(password.encode(),publicKey)
        logging.info(re_password)
        User_Model.add_usr(request_data["fname"], request_data["lname"], request_data["ph_no"], request_data["email"], password, re_password, request_data["role"])
        response = Response("User Added", 201, mimetype='application/json')
        logging.info(" * User Added")
        return response
    except:
        traceback.print_exc()
        resp = jsonify({"message": "Internal server error"})
        resp.status_code = 500   
        return resp

@ROUTE.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    '''method to update existing user'''
    try:
        from libs.models import User_Model
        request_data = request.get_json()
        User_Model.update_user(id, request_data['fname'], request_data['lname'], request_data["ph_no"], request_data["email"], request_data["passwd"], request_data["re_passwd"], request_data["role"])
        response = Response("User Updated", 201, mimetype='application/json')
        logging.info(" * User Updated")
        return response
    except:
        traceback.print_exc()
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
        traceback.print_exc()
        resp = jsonify({"message": "Internal server error"})
        resp.status_code = 500   
        return resp