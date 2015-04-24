'''
Created on Apr 18, 2015

@author: Ross
'''

class Person(object):
    '''
    classdocs
    '''


    def __init__(self, birthday, dad, mom, gender, name):
        '''
        Constructor
        '''
        self.dad = dad
        self.mom = mom
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.spouse = None
        self.pregnant = None
        
    def setSpouse(self, spouse):
        self.spouse = spouse