import pygame
import menu
import angband

class View(object):
    
    MENU_WIDTH = 200
    DISPLAY_SIZE = (640,640)
    
    def __init__(self):
        pygame.display.init()
        
        pygame.display.set_mode(View.DISPLAY_SIZE)
        self.display = pygame.display.get_surface()
        self.displayRect = self.display.get_rect()
        
        self.tileSet = angband.Angband()

        self.M = menu.Menu(self.displayRect, View.MENU_WIDTH)
        self.menuX = self.displayRect.width - View.MENU_WIDTH
        self.menuRect = pygame.Rect(self.menuX, 0, View.MENU_WIDTH, self.displayRect.height)
             
        self.background = pygame.Surface((1024,1024))
        for (x,y) in [(x,y) for x in range(1024) for y in range(1024) if x%32 == 0 and y%32 == 0]:
            self.background.blit(self.tileSet.getTile(0,0), (x,y))
        self.background.blit(self.tileSet.getTile(1,1), (64,64))
        
        self.camPos = [0,0]
        pygame.display.flip()
        
    def blitBackground(self):
        self.display.blit(self.background, (0,0), (self.camPos[0], self.camPos[1], View.DISPLAY_SIZE[0], View.DISPLAY_SIZE[1]))

    def clear(self):
        self.display.fill((0,0,0))

    def blitMenu(self):
        self.display.blit(self.M.getSurface(), (self.displayRect.width - View.MENU_WIDTH, 0))
        
    def blitCursor(self):
        pass
    
    def changeCursor(self, object):
        pass
        
    def blitAll(self):
        self.clear()
        self.blitBackground()
        self.blitMenu()
        self.blitCursor()
                
    def flip(self):
        pygame.display.flip()   

        