from models.person import Person 
import random

class personController(object):
    
    FEMALE_NAMES = ("Joan", "Elizabeth", "Matilda", "Mary", "Emily", "Arianna", "Brianne", "Claire", "Heather", "Leah", "Laura", "Irene", "Stephanie", "Constance", "Catelyn", "Lisa",
             "Alaina", "Bethany", "Dana", "Chantelle", "Elsa", "Gina", "Gabrielle", "Gwen", "Hailey", "Lisa", "Rose", "Samantha")
    MALE_NAMES = ("Adam", "Brian", "John", "Christopher", "Richard", "Henry", "William", "Edward", "David", "Patrcick", "Stephen", "Andrew", "Daniel", "Michael", "Mathew", "Alexander",
              "Edmond", "Ross", "Timothy", "Nickolas", "Jordan", "Jeffery", "Zachary", "Benjaman", "Thomas", "Darren", "Marcus", "Robbert")
    MAX_KIDS = 6

    def __init__(self):
        self.everyone = dict()  #all people, living and dead
        self.living = set()     #all living people
        self.adults = set()     #all adults, living and dead
        self.unmarried = set()  #all unmarried, living people
        self.count = 0          #number of people, living and dead
        random.seed()
        
    def __getitem__(self, i):
        return self.everyone[i]
        
    def birth(self, day, mID, fID, gender=None, name = None):
        if (gender == None):
            gender = self.randomGender()
        if (name == None):
            name = self.randomName(gender)
        self.everyone[self.count] = Person(self.count, day, mID, fID, gender, name)
        self.living.add(self.count)
        if (mID != None):
            self.everyone[mID].addKid(self.count)
            self.everyone[fID].addKid(self.count)
        self.count += 1
        if (gender == "male"): title = "boy"
        else: title = "girl"            
        if (mID == None): print("A " + title + " named " + name + " was born"),
        else: print(self.everyone[mID].name + " and " + self.everyone[fID].name + " had a " + title + " named " + name),
        print(" Population=" + str(len(self.living)))
        return (self.count - 1)
            
    def pregnant(self, fID, mID):
        if (self.everyone[fID].numKids() < self.MAX_KIDS):
            self.everyone[fID].pregnant = mID
            return True
        return False
    
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
    
    def findSpouse(self, pID):
        for spouse in self.unmarried:
            if (self.everyone[spouse].gender != self.everyone[pID].gender and spouse != pID):
                return spouse
        return None
        
    def death(self, pID, day):
        self.everyone[pID].death(day)
        spouse = self.everyone[pID].getSpouse()
        if (spouse != None):
            self.everyone[spouse].setSpouse(None)
            self.unmarried.add(spouse)
        else:
            if (pID in self.unmarried):  #self.adult would work also
                self.unmarried.remove(pID)
            
        self.living.remove(pID)
        print(self.everyone[pID].name + " has died"), 
        print(" Population=" + str(len(self.living)))
        return spouse
            
    
    def randomGender(self):
        return random.choice(("female", "male"))
    
    def randomName(self, gender):
        if (gender == "male"):
            return random.choice(self.MALE_NAMES)
        else:
            return random.choice(self.FEMALE_NAMES)
        