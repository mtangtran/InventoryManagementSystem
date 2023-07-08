class Inventory:

    def __init__(self, name):
        self.inventory = {}
        self.storageSpaceName = name
        self.item_id = 0
        self.totalCost = 0
    def addInventory(self, item, quantity, cost):
        if item in self.item_id:
            self.inventory[item] = quantity
        else:
            self.inventory[item] = quantity

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