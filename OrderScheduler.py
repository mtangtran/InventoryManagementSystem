class OrderScheduler:

    def __init__(self):
        self.orders = {}
        self.NumberedOrdered=0
        self.warehouseFlow = {}
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

    def addIntakeOutake(self, date, intake, outTake):
        self.warehouseFlow[date] = (intake, outTake)

    def getWarehouseNumbers(self):
        return self.warehouseFlow

    def getSpecificDate(self, date):
        if date in self.warehouseFlow:
            return self.warehouseFlow
        else:
            return None