from Inventory import Inventory

class SpecialInventory(Inventory):

    def __init__(self, name, reaction):
        self.inventory = Inventory.__init__(name)
        self.temp = reaction

    def getReaction(self):
        return self.temp

    def setReaction(self, reaction):
        self.temp = reaction

