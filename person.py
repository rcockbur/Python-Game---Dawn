'''
Created on Apr 18, 2015

@author: Ross
'''

class Person(object):
    '''
    classdocs
    '''


    def __init__(self, day, dad, mom, gender, name):
        '''
        Constructor
        '''
        self.dad = dad
        self.mom = mom
        self.name = name
        self.gender = gender
        self.birthday = day
        self.deathday = None
        self.spouse = None
        self.pregnant = None    #pID of father
        self.kids = list()
        
    def setSpouse(self, spouse):
        self.spouse = spouse
        
    def getSpouse(self):
        return self.spouse
    
    def addKid(self, pID):
        self.kids.append(pID)
        
    def numKids(self):
        return len(self.kids)
        
    def death(self, day):
        self.deathday = day