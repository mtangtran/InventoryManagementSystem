from Inventory import Inventory


class SpecialInventory(Inventory):

    def __init__(self, name, reaction):
        self.inventory = Inventory.__init__(name)
        self.temp = reaction
        self.sensitive = False
        self.whmis = False

    def getReaction(self):
        return self.temp

    def setReaction(self, reaction):
        self.temp = reaction


    def getWHMIS(self):
        return self.whmis

    def setWHMIS(self):
        self.whmis = True