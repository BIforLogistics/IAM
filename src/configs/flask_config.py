import sys
import logging
from flask_swagger import swagger
from flask import Flask, request, g, jsonify
import json_logging

# instance of flask APP
APP = Flask(__name__)

json_logging.init_flask(enable_json=True)
json_logging.init_request_instrument(APP)

logger = logging.getLogger("IAM")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

@APP.route("/spec")
def spec():
    swag = swagger(APP)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "IAM"
    swag['schemes'] = ["http"]
    swag['host'] = request.host
    return jsonify(swag)

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:iam123@localhost:3306/IAM"
APP.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:iam123@localhost:3306/IAM"
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def register_blueprints():
    """We will register flask blueprints here"""
    from api_controllers.iam.rest_iam import ROUTE
    from api_controllers.root import ROOT_ROUTE
    from api_controllers.about.about import ABOUT_ROUTE
    APP.register_blueprint(ROOT_ROUTE)
    APP.register_blueprint(ABOUT_ROUTE)
    APP.register_blueprint(ROUTE)
    
register_blueprints()