class savedData():
    '''Class for processing data from requests'''
    
    Orders = [{'id': 1, 'name':'Default item' , 'amount':10 , 'quantity': 2}]

    def allOrders(self):
        '''Passes the list items back to user'''
        return savedData.Orders

    def addOrders(self,name,amount,quantity):
        '''Adds an order to the orders list'''
        id = len(savedData.Orders) + 1
        passed_order = {'id': id, 'name': name, 'amount' : amount, 'quantity' : quantity}
        savedData.Orders.append(passed_order)

        return savedData.Orders