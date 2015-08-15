from house import house

class houseController(object):
    def __init__(self):
        self.houses = dict()
        
    def addHouse(self, hID):
        self.houses[hID] = house(hID)