# from pygame import USEREVENT
from controllers.eventController import eventController
from controllers.personController import personController

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
        self.EC = eventController()
        self.PC = personController()
    
    def handleEvents(self):
        print(self.EC.month)
        for event in self.EC.getTodaysEvents():
            if event[0] == CREATE:
                pID = self.PC.birth(self.EC.month, event[1]['mID'], event[1]['fID'], event[1]['gender'], event[1]['name'])
                self.EC.planAdulthood(pID)
                self.EC.planDeath(pID, True)   
            
            elif event[0] == BIRTH:
                if (event[1]['fID'] not in self.PC.living):
                    continue
                pID = self.PC.birth(self.EC.month, event[1]['mID'], event[1]['fID'], event[1]['gender'], event[1]['name'])
                self.EC.planAdulthood(pID)
                if (event[1]['mID'] not in self.PC.living):
                    continue
                self.EC.planPregnancy(event[1]['mID'], event[1]['fID'])
                self.EC.planDeath(pID, False)
                
            elif event[0] == ADULTHOOD:
                if (event[1]['pID'] not in self.PC.living):
                    continue
                self.PC.adulthood(event[1]['pID'])
                spouse = self.PC.findSpouse(event[1]['pID'])
                if (spouse != None):
                    if (self.PC[event[1]['pID']].getGender() == "male"):
                        self.PC.marriage(event[1]['pID'], spouse)
                        self.EC.planPregnancy(event[1]['pID'], spouse)
                    else:
                        self.PC.marriage(spouse, event[1]['pID'])
                        self.EC.planPregnancy(spouse, event[1]['pID'])
                      
            elif event[0] == PREGNANT:
                if (event[1]['mID'] not in self.PC.living):
                    continue
                if (self.PC.pregnant(event[1]['mID'], event[1]['fID'])):
                    self.EC.planBirth(event[1]['mID'], event[1]['fID'])            
                
            elif event[0] == DEATH:
                if (event[1]['pID'] not in self.PC.living):
                    continue
                pID = self.PC.death(event[1]['pID'], self.EC.month)
                if (pID != None):
                    spouse = self.PC.findSpouse(pID)
                    if (spouse != None):
                        if (self.PC[pID].getGender() == "male"):
                            self.PC.marriage(pID, spouse)
                            self.EC.planPregnancy(pID, spouse)
                        else:
                            self.PC.marriage(spouse, pID)
                            self.EC.planPregnancy(spouse, pID)
                            
        self.EC.nextMonth()
        
        