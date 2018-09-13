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