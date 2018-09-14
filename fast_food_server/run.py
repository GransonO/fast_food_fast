''' The main starter for the application'''
from flask_restplus import Resource, Api
import app
from dataset.data_handler import savedData

MY_APP = app.create_app('TESTING')
API = Api(MY_APP)

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

API.add_resource(Home, '/home')
API.add_resource(GeneralRequests, '/v1/orders')

if __name__ == '__main__':
    MY_APP.run()
