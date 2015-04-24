'''
Created on Apr 18, 2015

@author: Ross
'''

class Calendar(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.today = 1
        self.schedule = dict()
        
    def addPlan(self, plan):
        day = plan[0]
        event = plan[1]
        if (day in self.schedule):
            self.schedule[day].append(event)
        else:
            self.schedule[day] = list()
            self.schedule[day].append(event)
            
    def addPlans(self, plans):
        pass
            
    def getTodaysEvents(self):
        if(self.today in self.schedule):
            events = self.schedule[self.today]
            del self.schedule[self.today]
            return events
        else:
            return list()
        
    def nextDay(self):
        self.today += 1