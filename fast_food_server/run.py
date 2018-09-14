''' The main starter for the application'''
from flask_restplus import Resource, Api
import app
from dataset.data_handler import savedData

my_app = app.create_app('TESTING')
api = Api(my_app)

class Home(Resource):
    '''Redirects to home page'''

    def get(self): #pylint: disable=no-self-use
        '''Redirects to home page'''
        return {'data':'This is home'}

class GeneralRequests(Resource):
    ''' Processes the get all and post requests'''

    def get(self):
        '''Retrieves all items and pass them back to user'''
        result = savedData.allOrders(self)
        return {'data': result}, 200

api.add_resource(Home, '/home')
api.add_resource(GeneralRequests, '/v1/orders')

if __name__ == '__main__':
    my_app.run()
