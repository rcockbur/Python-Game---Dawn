# from pygame import USEREVENT
from models.calendar_ import Calendar
from models.personController import PersonController

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

class UserEventHandler(object):   
    def __init__(self):
        self.C = Calendar()
        self.P = PersonController()
    
    def handleEvents(self):
        print(self.C.month)
        for event in self.C.getTodaysEvents():

            if event[0] == CREATE:
                pID = self.P.birth(self.C.month, event[1]['mID'], event[1]['fID'], event[1]['gender'], event[1]['name'])
                self.C.planAdulthood(pID)
                self.C.planDeath(pID, True)   
            
            elif event[0] == BIRTH:
                if (event[1]['fID'] not in self.P.living):
                    continue
                pID = self.P.birth(self.C.month, event[1]['mID'], event[1]['fID'], event[1]['gender'], event[1]['name'])
                self.C.planAdulthood(pID)
                if (event[1]['mID'] not in self.P.living):
                    continue
                self.C.planPregnancy(event[1]['mID'], event[1]['fID'])
                self.C.planDeath(pID, False)
                
            elif event[0] == ADULTHOOD:
                if (event[1]['pID'] not in self.P.living):
                    continue
                self.P.adulthood(event[1]['pID'])
                spouse = self.P.findSpouse(event[1]['pID'])
                if (spouse != None):
                    if (self.P[event[1]['pID']].getGender() == "male"):
                        self.P.marriage(event[1]['pID'], spouse)
                        self.C.planPregnancy(event[1]['pID'], spouse)
                    else:
                        self.P.marriage(spouse, event[1]['pID'])
                        self.C.planPregnancy(spouse, event[1]['pID'])
                      
            elif event[0] == PREGNANT:
                if (event[1]['mID'] not in self.P.living):
                    continue
                if (self.P.pregnant(event[1]['mID'], event[1]['fID'])):
                    self.C.planBirth(event[1]['mID'], event[1]['fID'])            
                
            elif event[0] == DEATH:
                if (event[1]['pID'] not in self.P.living):
                    continue
                pID = self.P.death(event[1]['pID'], self.C.month)
                if (pID != None):
                    spouse = self.P.findSpouse(pID)
                    if (spouse != None):
                        if (self.P[pID].getGender() == "male"):
                            self.P.marriage(pID, spouse)
                            self.C.planPregnancy(pID, spouse)
                        else:
                            self.P.marriage(spouse, pID)
                            self.C.planPregnancy(spouse, pID)
                            
        self.C.nextMonth()
        
        