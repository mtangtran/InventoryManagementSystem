class OrderScheduler:

    def __init__(self):
        self.orders = {}
        self.NumberedOrdered=0
    def getOrders(self):
        return self.NumberedOrdered

    def addOrders(self, order, quantity):
        self.NumberedOrdered +=1
        self.orders[order] = quantity

    def deleteOrder(self, order):
        if order in self.orders:
            self.orders.pop(order)

    def updateOrderQuantity(self, order, quantity):
        self.orders[order]=quantity

    def getAllOrders(self):
        return self.orders

    def deleteAllOrders(self):
        self.orders = {}