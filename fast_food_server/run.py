''' The main starter for the application'''
from os import environ
from flask_restplus import Resource, Api, fields
import app
from dataset.data_handler import SavedData

MY_APP = app.create_app(None)
API = Api(MY_APP)


PROP_ORDER = API.model('order', {'name' : fields.String('Name of what to order'), 'amount' : fields.Integer('Price of order'), 'quantity' : fields.Integer('Quantity of items')}) #pylint: disable=line-too-long

class Home(Resource):
    '''Redirects to home page'''

    def get(self):#pylint: disable=no-self-use
        '''Redirects to home page'''
        return {'data':'This is home'}

class GeneralRequests(Resource):
    ''' Processes the get all and post requests'''

    def get(self):
        '''Retrieves all items and pass them back to user'''
        result = SavedData.all_orders(self)
        return {'data': result}, 200

    @API.expect(PROP_ORDER)
    def post(self):
        '''Adds an order to the items list'''
        my_order = API.payload
        name = my_order['name']
        amount = my_order['amount']
        quantity = my_order['quantity']
        results = SavedData.add_orders(self, name, amount, quantity)

        return {'data':results}, 201

class SpecificRequests(Resource):
    '''Processes specific put and get requests'''
    def get(self, num):
        '''Retrieves a specific order'''
        results = SavedData.get_specific_order(self, num)

        return {'data' : results}, 202

    @API.expect(PROP_ORDER)
    def put(self, num):
        '''Edits content of a specified order'''
        update_data = API.payload

        name = update_data['name']
        amount = update_data['amount']
        quantity = update_data['quantity']
        results = SavedData.update_order(self, num, name, amount, quantity)

        return {'data': results}

API.add_resource(Home, '/home')
API.add_resource(GeneralRequests, '/v1/orders')
API.add_resource(SpecificRequests, '/v1/orders/<int:num>')

if __name__ == '__main__':
    MY_APP.run(host='0.0.0.0',port=environ.get("PORT", 5000))
