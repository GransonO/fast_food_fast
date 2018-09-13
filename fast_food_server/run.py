import app
from flask import Flask
from flask_restplus import Resource, Api, fields
from dataset.data_handler import savedData

my_app = app.create_app('TESTING')
api = Api(my_app)


properties_order = api.model('order',{'name' : fields.String('Name of what to order'),
'amount' : fields.Integer('Price of order'),'quantity' : fields.Integer('Quantity of items')})

class Home(Resource):
    def get(self):
        return {'data':'This is home'}
        
class GeneralRequests(Resource):
    ''' Processes the get all and post requests'''
    
    def get(self):
        '''Retrieves all items and pass them back to user'''
        result = savedData.allOrders(self)
        return {'data': result}, 200

    @api.expect(properties_order)
    def post(self):
        '''Adds an order to the items list'''
        my_order = api.payload
        name = my_order['name']
        amount = my_order['amount']
        quantity = my_order['quantity']
        results = savedData.addOrders(self,name, amount, quantity)

        return {'data':results}, 201

   

api.add_resource(Home,'/home')
api.add_resource(GeneralRequests,'/v1/orders')

if __name__ == '__main__':
    my_app.run()