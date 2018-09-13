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

    def getSpecificOrder(self,id):
        '''Retrieves a specific item and sends back to user '''
        num = id - 1
        if len(savedData.Orders) >= num:
            item = savedData.Orders[num]
            return item
        else:
            return "Couldn't find what you were looking for"

    def updateOrder(self,id,name,amount,quantity):
        '''Updates an order in the list'''
        num = id - 1
        if len(savedData.Orders) >= num:
            item = savedData.Orders[num]
            '''Edit all entries'''
            item['name'] = name
            item['amount'] = amount
            item['quantity'] = quantity

            return savedData.Orders
        else:
            return "Couldn't find what you were looking for"
