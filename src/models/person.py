class Person(object):

    def __init__(self, ID, day, dad, mom, gender, name):
        self.ID = ID
        self.dad = dad
        self.mom = mom
        self.name = name
        self.gender = gender
        self.birthday = day
        self.deathday = None
        self.spouse = None
        self.pregnant = None    #pID of the father
        self.kids = list()
        
    def getID(self, ID):
        return self.ID
    def getSpouse(self):
        return self.spouse
    def setSpouse(self, spouse):
        self.spouse = spouse
    def getGender(self):
        return self.gender
    def setGender(self, gender):
        self.gender = gender
    def addKid(self, pID):
        self.kids.append(pID) 
    def numKids(self):
        return len(self.kids)
    def death(self, day):
        self.deathday = day