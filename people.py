'''
Created on Apr 18, 2015

@author: Ross
'''
import person, random

FEMALE_NAMES = ("Joan", "Elizabeth", "Matilda", "Mary", "Emily", "Arianna", "Brianne", "Claire", "Heather", "Leah", "Laura", "Irene", "Stephanie", "Constance", "Catelyn", "Lisa")
MALE_NAMES = ("Adam", "Brian", "John", "Christopher", "Richard", "Henry", "William", "Edward", "David", "Patrcick", "Stephen", "Andrew", "Daniel", "Michael", "Mathew", "Alexander")
    
class People(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.everyone = dict()
        self.living = set()
        self.adults = set()
        self.unmarried = set()
        self.count = 0
        random.seed()
        
    def birth(self, birthday, mID, fID, gender=None, name = None):
        
#         if (dad == None and gender == "female"):
#             name = "Eve"
#         if (dad == None and gender == "male"):
#             name = "Adam"
            
        if (gender == None):
            gender = self.randomGender()
        if (name == None):
            name = self.randomName(gender)
            
        self.everyone[self.count] = person.Person(birthday, mID, fID, gender, name)
        self.living.add(self.count)
        self.count += 1
        
        if (gender == "male"):
            title = "boy"
        else:
            title = "girl"
            
        if (mID == None):
            print("A " + title + " named " + name + " was born")
        else:
            print(self.everyone[mID].name + " and " + self.everyone[fID].name + " had a " + title + " named " + name)
            
        return (self.count - 1)
            
    def pregnant(self, fID, mID):
        self.everyone[fID].pregnant = mID
    
    def marriage(self, mID, fID):
        self.everyone[mID].setSpouse(fID)
        self.everyone[fID].setSpouse(mID)
        self.unmarried.remove(mID)
        self.unmarried.remove(fID)
        print(self.everyone[mID].name + " and " + self.everyone[fID].name + " have gotten married")
        
    def adulthood(self, pID1):
        self.adults.add(pID1)
        self.unmarried.add(pID1)
        print(self.everyone[pID1].name + " is now an adult")
        
        for pID2 in self.unmarried:
            if (self.everyone[pID2].gender != self.everyone[pID1].gender and pID1 != pID2):
                return pID2
        return None
        
    def randomGender(self):
        return random.choice(("female", "male"))
    
    def randomName(self, gender):
        if (gender == "male"):
            return random.choice(MALE_NAMES)
        else:
            return random.choice(FEMALE_NAMES)