from app import create_app
from flask import jsonify, request
import pytest

'''Creates an app instance for testing the functions '''
my_app = create_app('TESTING')

#TESTS TO PERFORM
test_orders = [{'id':1,'name':'Cake','amount':'2000','quantity':10},{'id':2,'name':'Pizza','amount':'1500','quantity':10}]

'''Test for get call on home page'''
@my_app.route('/home')
def home():
    return 'this is home'

#Test for all orders
@my_app.route('/v1/orders', methods=['GET'])
def get_all():
    '''Test for get call orders'''
    return jsonify(test_orders), 202

@my_app.route('/v1/orders/<int:num>')
def get_specified(num):
    '''Test for getting a specific order'''
    return jsonify(test_orders[num]), 200


@pytest.fixture
def app_test():
    '''Creates a fixture for the flask app
        for testing'''
    test_client = my_app.test_client()

    #Establish context
    app_context = my_app.app_context()
    app_context.push()

    yield test_client

    #Cleaning after testing
    app_context.pop()