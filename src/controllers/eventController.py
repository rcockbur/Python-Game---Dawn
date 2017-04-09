import random

class eventController(object):
    
    MARRIAGE = 1
    BIRTHDAY = 2
    DEATH = 3
    BIRTH = 4
    ADULTHOOD = 5
    PREGNANT = 6
    CREATE = 7
    
    MONTHS_AS_CHILD = 12 * 16
    MONTHS_PREGNANT = 9
    MAXLIFE = 12 * 80
    MAXCONCEIVE = 12*5

    def __init__(self):
        self.month = 0
        self.schedule = dict()
        self.createAdamEve()
        
    def addPlan(self, plan):
        month = plan[0]
        event = plan[1]
        if (month in self.schedule):
            self.schedule[month].append(event)
        else:
            self.schedule[month] = list()
            self.schedule[month].append(event)
            
    def addPlans(self, plans):
        pass
            
    def getTodaysEvents(self):
        if(self.month in self.schedule):
            events = self.schedule[self.month]
            del self.schedule[self.month]
            return events
        else:
            return list()
        
    def nextMonth(self):
        self.month += 1
        
    def lifeSpan(self):
        return random.randint(1, self.MAXLIFE)

    def monthsToConveive(self):
        return random.randint(1, 12*5)

    def createAdamEve(self):
        event = (self.CREATE, {"fID": None, "mID": None, "gender": "male", "name": "Adam"})    
        self.addPlan((0, event))
        event = (self.CREATE, {"fID": None, "mID": None, "gender": "female", "name": "Eve"})
        self.addPlan((0, event))
        
    def planAdulthood(self, pID):
        event = (self.ADULTHOOD, {"pID": pID})
        self.addPlan((self.month + self.MONTHS_AS_CHILD, event))
        
    def planBirth(self, fID, mID):
        event = (self.BIRTH, {"mID": mID, "fID": fID, "gender": None, "name": None})
        self.addPlan((self.month + self.MONTHS_PREGNANT, event))
        
    def planPregnancy(self, fID, mID):
        event = (self.PREGNANT, {"mID": mID, "fID": fID})
        self.addPlan((self.month + self.monthsToConveive(), event))
        
    def planDeath(self, pID, maxLife):
        event = (self.DEATH, {"pID": pID})
        if (maxLife == True):
            self.addPlan((self.month + self.MAXLIFE, event))
        else:
            self.addPlan((self.month + self.lifeSpan(), event))