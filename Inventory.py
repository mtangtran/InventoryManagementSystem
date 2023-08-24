class Inventory:

    def __init__(self, name):
        self.inventory = {}
        self.storageSpaceName = name
        self.item_id = 1
        self.totalCost = 0
        self.temp=0
        self.expectedLosses = 0
    def addInventory(self, item, quantity, cost):
        if item in self.inventory:
            self.inventory[item] = (self.item_id, quantity)
        else:
            self.inventory[item] = (self.item_id, quantity)

        self.item_id +=1
        self.totalCost = self.totalCost + quantity*cost
    def deleteInventory(self, item, cost):

        if item in self.inventory:
            self.totalCost = self.totalCost - self.inventory[item] * cost
            self.inventory.pop(item)

    def getInventoryItem(self, item):
        if item in self.inventory:
            return self.inventory[item]
        else:
            return None

    def updateInventory(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] = quantity

        else:
            self.inventory[item] = quantity

    def getTotalCost(self):
        return self.totalCost

    def getRecentItemID(self):
        return self.item_id

    def setTemp(self, temp):
        self.temp = temp

    def getTemp(self):
        return self.temp

    def setExpectedLosses(self, loss):
        self.expectedLosses += loss


    def getExpectedLoss(self):
        return self.expectedLosses