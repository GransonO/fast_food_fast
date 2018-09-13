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