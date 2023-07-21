class Management:

    def __init__(self):
        self.managers = []
        self.storageSpaces = {}


    def addManagers(self, manager):
        self.managers.append(manager)

    def getManagers(self):
        self.managers = []

    def removeManager(self, manager):
        for i in range(len(self.managers)):
            if self.managers[i]==manager:
                self.managers.remove(manager)

    def updateManager(self, manager, change):
        for i in range(len(self.managers)):
            if self.managers[i]== manager:
                self.managers[i] = change
    def getStorageSpace(self):
        return self.storageSpaces

    def removeStorageSpace(self, storageName):
        if storageName in self.storageSpaces:
            self.storageSpaces.pop(storageName)

    def getStorageSpace(self):
        return self.storageSpaces

    def addStorage(self, storage):
        self.storageSpaces[storage]=[]

