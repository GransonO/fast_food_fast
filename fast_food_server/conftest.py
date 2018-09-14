'''Creates an app instance for testing the functions '''
import pytest
from flask import jsonify, request
from app import create_app

MY_APP = create_app('TESTING')

#TESTS TO PERFORM
TEST_ORDERS = [{'id':1, 'name':'Cake', 'amount':'2000', 'quantity':10}, {'id':2, 'name':'Pizza', 'amount':'1500', 'quantity':10}] #pylint: disable=line-too-long

@MY_APP.route('/home')
def home():
    '''Test for get call on home page'''
    return 'this is home'

#Test for all orders
@MY_APP.route('/v1/orders', methods=['GET'])
def get_all():
    '''Test for get call orders'''
    return jsonify(TEST_ORDERS), 202

@MY_APP.route('/v1/orders/<int:num>')
def get_specified(num):
    '''Test for getting a specific order'''
    return jsonify(TEST_ORDERS[num]), 200

@MY_APP.route('/v1/orders', methods=['POST'])
def post_order():
    '''Test for posting a new order'''
    order_id = len(TEST_ORDERS) + 1

    name = request.json["name"]
    amount = request.json['amount']
    quantity = request.json['quantity']

    new_entry = {'id':order_id, 'name':name, 'amount':amount, 'quantity':quantity}

    TEST_ORDERS.append(new_entry)
    return jsonify(TEST_ORDERS), 201

@MY_APP.route('/v1/orders/<int:count>', methods=['PUT'])
def put_update_data(count):
    """call to edit an entry"""

    result = [test_order for test_order in TEST_ORDERS if test_order['id'] == count]
    result[0]['name'] = request.json['name']
    result[0]['amount'] = request.json['amount']
    result[0]['quantity'] = request.json['quantity']
    return jsonify(TEST_ORDERS), 202

@pytest.fixture
def app_test():
    '''Creates a fixture for the flask app
        for testing'''
    test_client = MY_APP.test_client()

    #Establish context
    app_context = MY_APP.app_context()
    app_context.push()

    yield test_client

    #Cleaning after testing
    app_context.pop()
