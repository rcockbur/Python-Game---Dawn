import pygame
import constants

class menuView(object):

    DISPLAY_SIZE = constants.DISPLAY_SIZE
    
    def __init__(self):
        pygame.display.init()
        self.oldTime = pygame.time.get_ticks()
        
        pygame.display.set_mode(self.DISPLAY_SIZE)
        self.display = pygame.display.get_surface()
        self.displayRect = self.display.get_rect() 
        self.background = pygame.Surface(self.DISPLAY_SIZE)
        self.background.fill((10,90,50), rect=None, special_flags=0)
        pygame.display.flip()
        
    def blitBackground(self):
        self.display.blit(self.background, (0,0), (0, 0, self.DISPLAY_SIZE[0], self.DISPLAY_SIZE[1]))

    def clear(self):
        self.display.fill((0,0,0))
        
    def blitCursor(self):
        pass
    
    def changeCursor(self, object):
        pass
        
    def blitAll(self):
        self.clear()
        self.blitBackground()
        self.blitCursor()
                
    def flip(self):
        pygame.display.flip()
        
    def processPygameEvents(self):
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        left_held = pressed[pygame.K_LEFT]
        right_held = pressed[pygame.K_RIGHT]
        up_held = pressed[pygame.K_UP]
        down_held = pressed[pygame.K_DOWN]
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()                       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and ctrl_held:
                    pygame.quit()
                    quit()      
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("leftClick")

    def processEvents(self):
        self.processPygameEvents()
        return self
        