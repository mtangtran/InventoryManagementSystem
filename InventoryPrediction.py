class InventoryPrediction:
    def __init__(self):
        self.predictions = []
        self.past = []
        self.totalItems = 0
        self.requirements = []
    def createPrediction(self):
        self.predictions = []
    def getPrediction(self):
        return self.predictions

    def getTotalItems(self):
        return self.totalItems

    def setRequirements(self, date, item, quantity):
        self.requirements.append((date, item, quantity))

    def getAllRequirements(self):
        return self.requirements

    def getSpecificRequirement(self, item, date):
        reqList=[]
        for i in range(len(self.requirements)):
            if self.requirements[i][0] == date and self.requirements[i][1] == item:
                reqList.append(self.requirements[i])

        return reqList

    def clearRequirements(self):
        self.requirements = []

    def updateRequirements(self, item, date, quantity):
        for i in range(len(self.requirements)):
            if self.requirements[i][0] == date and self.requirements[i][1] == item and self.requirements[i][2] == quantity:
                self.requirements[i] = (item, date, quantity)