'''
Created on Apr 24, 2015

@author: Ross
'''
from pygame import Rect
from pygame.surface import Surface
import button

class Menu(object):
    '''
    classdocs
    '''

    def __init__(self, rect, width):
#         self.width = width
#         self.mainDisplayRect = rect
#         self.menuRect = Rect(rect.right - self.width, 0, self.width, rect.height)
#         self.menuRect = Rect(0, 0, self.width, rect.height)
        self.surface = Surface((width, rect.height))
        self.surface.fill((100,100,250))
        self.buttonDict = dict()
        self.addButton(10, 10, 40, 40, "House")
        self.updateAll()
        '''
        Constructor
        '''
        
    def addButton(self, x, y, width, height, text):
        self.buttonDict[(x, y, width, height)] = (button.Button(width, height, text))
        
    def getButton(self, x, y):
        for myRect in self.buttonDict.keys():
            if Rect(myRect[0], myRect[1], myRect[2], myRect[3]).collidepoint(x, y):
                return self.buttonDict[(myRect[0], myRect[1], myRect[2], myRect[3])].text
        return None
            
    def updateAll(self):
        for myRect, button in self.buttonDict.items():
            self.surface.blit(button.surface, (myRect[0], myRect[1]))
    
    def getSurface(self):
        return self.surface
        