class savedData():
    '''Class for processing data from requests'''
    
    Orders = [{'id': 1, 'name':'Default item' , 'amount':10 , 'quantity': 2}]

    def allOrders(self):
        '''Passes the list items back to user'''
        return savedData.Orders
