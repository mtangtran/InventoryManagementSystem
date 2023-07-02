class Inventory:

    def __init__(self, name):
        self.inventory = {}
        self.storageSpaceName = name
        self.item_id = 0

    def addInventory(self, item, quantity):
        if item in self.item_id:
            self.inventory[item] = quantity
        else:
            self.inventory[item] = quantity

    def deleteInventory(self, item):
        if item in self.inventory:
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

