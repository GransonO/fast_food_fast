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
        item = "Couldn't find what you were looking for"
        num = order_id - 1
        if len(SavedData.Orders) >= 1:
            item = SavedData.Orders[num]

        return item


    def update_order(self, num, name, amount, quantity):#pylint: disable=no-self-use
        '''Updates an order in the list'''
        results = "Couldn't find what you were looking for"
        num = num - 1
        if len(SavedData.Orders) >= num:
            item = SavedData.Orders[num]

            item['name'] = name
            item['amount'] = amount
            item['quantity'] = quantity

            results = SavedData.Orders

        return results
