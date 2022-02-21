import logging
from flask import Blueprint, Flask, Response, jsonify, request

ROUTE = Blueprint('ROUTE',__name__)

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)