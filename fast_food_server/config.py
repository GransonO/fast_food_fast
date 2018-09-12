import os

class TestingConfiguration():
    '''Configuration during testing'''
    DEBUG = True
    TESTING = True

class ProductionConfiguration():
    '''Configuration during production'''
    DEBUG = False
    TESTING = False

config_status = {"TESTING":TestingConfiguration,"Production": ProductionConfiguration}