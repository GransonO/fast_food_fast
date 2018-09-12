import app
from flask import Flask
from flask_restplus import Resource, Api

my_app = app.create_app(None)
api = Api(my_app)

class Home(Resource):
    def get(self):
        return {'data':'This is a test'}

api.add_resource(Home,'/home')

if __name__ == '__main__':
    my_app.run(debug=True) 