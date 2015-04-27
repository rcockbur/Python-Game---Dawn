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
        self.month = 0
        self.schedule = dict()
        
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