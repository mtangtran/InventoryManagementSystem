class InventoryPrediction:
    def __init__(self):
        self.predictions = []
        self.past = []
        self.totalItems = 0

    def createPrediction(self):
        self.predictions = []
    def getPrediction(self):
        return self.predictions

    def getTotalItems(self):
        return self.totalItems