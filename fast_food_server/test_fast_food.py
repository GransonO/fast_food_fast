'''For the testing, I have employed the use of vanilla flask in 
place of the restplus due to difficulties found in testing apis'''

test_data = {"name":"Mango","amount":200,"quantity":20}
put_data = {"name":"Guava","amount":250,"quantity":25}

'''Test for home return'''
def test_home(app_test):
    response = app_test.get('/home')
    assert response.status_code == 200

'''Test for returned get value from home'''
def test_development(app_test):
    response = app_test.get('/home')
    assert b"this is home" in response.data

#Get all orders
def test_get_all(app_test):
    '''Test for get call orders'''
    response = app_test.get('/v1/orders')
    assert response.status_code == 202

def test_get_all_i(app_test):
    '''Test for get call orders'''
    response = app_test.get('/v1/orders')
    assert b"Cake" in response.data
    assert b"quantity" in response.data
    assert b"Pizza" in response.data

#Get specific order
def test_get_specific(app_test):
    '''Test for getting a specific order'''
    response = app_test.get('/v1/orders/1')
    assert b"Pizza" in response.data
    assert b"1500" in response.data

def test_get_specific_i(app_test):
    '''Test for getting a specific order'''
    response = app_test.get('/v1/orders/1')
    assert response.status_code == 200

#Posting orders
def test_post(app_test):
    '''Test for posting a new order'''
    response = app_test.post('/v1/orders', json=test_data)
    assert response.status_code == 201

def test_post_i(app_test):
    '''Test for posting a new order'''
    response = app_test.post('/v1/orders',json=test_data)
    assert b"Mango" in response.data
    assert b"200" in response.data
    assert b"20" in response.data    