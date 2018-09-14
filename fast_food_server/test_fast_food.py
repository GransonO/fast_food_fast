'''For the testing, I have employed the use of vanilla flask in
place of the restplus due to difficulties found in testing apis'''

TEST_DATA = {"name":"Mango", "amount":200, "quantity":20}
PUT_DATA = {"name":"Guava", "amount":250, "quantity":25}

def test_home(app_test):
    '''Test for home return'''
    response = app_test.get('/home')
    assert response.status_code == 200

def test_development(app_test):
    '''Test for returned get value from home'''
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
    response = app_test.post('/v1/orders', json=TEST_DATA)
    assert response.status_code == 201

def test_post_i(app_test):
    '''Test for posting a new order'''
    response = app_test.post('/v1/orders', json=TEST_DATA)
    assert b"Mango" in response.data
    assert b"200" in response.data
    assert b"20" in response.data

#Updating orders
def test_update(app_test):
    '''Test for updating an order'''
    response = app_test.get('/v1/orders/2')
    assert response.status_code == 200

def test_update_i(app_test):
    '''Test for updating an order'''
    response = app_test.put('/v1/orders/1', json=PUT_DATA)
    assert b"Guava" in response.data
