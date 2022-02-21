from flask import Blueprint
from flask_responses import json_response

ROOT_ROUTE = Blueprint('root',__name__)

@ROOT_ROUTE.route('/')
def root():
    '''Return Simple Health Status'''
    dictionary = {'Service':'IAM', 'Status':'Healthy'}
    return json_response(data=dictionary, status_code=200)