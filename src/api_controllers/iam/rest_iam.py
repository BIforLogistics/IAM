import logging
from flask import Blueprint, Flask, Response, jsonify, request
from lib.models import db
from configs.flask_config import APP

ROUTE = Blueprint('ROUTE',__name__)

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

@APP.before_first_request
def create_table():
    db.create_all()