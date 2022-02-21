from flask import Blueprint
from flask_responses import json_response
import socket

ABOUT_ROUTE = Blueprint('about',__name__)

@ABOUT_ROUTE.route('/healthz')
def about():
    '''Return Simple Health Status'''
    dictionary = {'Service':'IAM', 'Host':socket.gethostname()}
    return json_response(data=dictionary, status_code=200)
