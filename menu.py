'''
Created on Apr 24, 2015

@author: Ross
'''
from pygame import Rect
from pygame.surface import Surface

class Menu(object):
    '''
    classdocs
    '''

    def __init__(self, rect, width):
        self.width = width
        self.mainDisplayRect = rect
        self.menuRect = Rect(rect.right - self.width, 0, self.width, rect.height)
        self.surface = Surface((self.menuRect.width, self.menuRect.height))
        self.surface.fill((100,100,250))
        '''
        Constructor
        '''
        
    def getSurface(self):
        return self.surface
        