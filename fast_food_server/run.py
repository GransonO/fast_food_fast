import app
from flask import Flask
from flask_restplus import Resource, Api, fields
from dataset.data_handler import savedData

my_app = app.create_app('TESTING')
api = Api(my_app)

class Home(Resource):
    def get(self):
        return {'data':'This is home'}
        
class GeneralRequests(Resource):
    ''' Processes the get all and post requests'''
    
    def get(self):
        '''Retrieves all items and pass them back to user'''
        result = savedData.allOrders(self)
        return {'data': result}
   

api.add_resource(Home,'/home')
api.add_resource(GeneralRequests,'/v1/orders')

if __name__ == '__main__':
    my_app.run()