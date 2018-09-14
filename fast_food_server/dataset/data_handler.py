'''Class for processing data from requests'''
class SavedData():
    '''Called from the run function'''

    Orders = [{'id': 1, 'name':'Default item', 'amount':10, 'quantity': 2}]

    def all_orders(self):#pylint: disable=no-self-use
        '''Passes the list items back to user'''
        return SavedData.Orders

    def add_orders(self, name, amount, quantity):#pylint: disable=no-self-use
        '''Adds an order to the orders list'''
        order_id = len(SavedData.Orders) + 1
        passed_order = {'id': order_id, 'name': name, 'amount' : amount, 'quantity' : quantity}
        SavedData.Orders.append(passed_order)

        return SavedData.Orders

    def get_specific_order(self, order_id):#pylint: disable=no-self-use
        '''Retrieves a specific item and sends back to user '''
<<<<<<< HEAD
        item = "Couldn't find what you were looking for"
        num = order_id - 1
        if len(SavedData.Orders) >= 1:
            item = SavedData.Orders[num]

        return item
=======
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
          
>>>>>>> 187e27618cf67ded9c1df1b4a08bb5b1cde6be34
