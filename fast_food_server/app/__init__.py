from flask import Flask
from config import config_status


def create_app(config_state):
    '''Creates an instance of the app with 
        necessary configurations passed in '''
    app = Flask(__name__)
    
    if(config_state == 'TESTING'):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True

    return app