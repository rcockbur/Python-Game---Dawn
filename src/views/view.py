import pygame
import menu
import angband

class view(object):
    
    MENU_WIDTH = 200
    DISPLAY_SIZE = (640,640)
    
    def __init__(self):
        pygame.display.init()
        
        pygame.display.set_mode(self.DISPLAY_SIZE)
        self.display = pygame.display.get_surface()
        self.displayRect = self.display.get_rect()
        
        self.tileSet = angband.angband()

        self.M = menu.menu(self.displayRect, self.MENU_WIDTH)
        self.menuX = self.displayRect.width - self.MENU_WIDTH
        self.menuRect = pygame.Rect(self.menuX, 0, self.MENU_WIDTH, self.displayRect.height)
             
        self.background = pygame.Surface((1024,1024))
        for (x,y) in [(x,y) for x in range(1024) for y in range(1024) if x%32 == 0 and y%32 == 0]:
            self.background.blit(self.tileSet.getTile(0,0), (x,y))
        self.background.blit(self.tileSet.getTile(1,1), (64,64))
        
        self.camPos = [0,0]
        pygame.display.flip()
        
    def blitBackground(self):
        self.display.blit(self.background, (0,0), (self.camPos[0], self.camPos[1], self.DISPLAY_SIZE[0], self.DISPLAY_SIZE[1]))

    def clear(self):
        self.display.fill((0,0,0))

    def blitMenu(self):
        self.display.blit(self.M.getSurface(), (self.displayRect.width - self.MENU_WIDTH, 0))
        
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
    
    def moveCameraRelative(self, dx, dy):
        self.camPos[0] = self.camPos[0] + dx
        self.camPos[1] = self.camPos[1] + dy
        
    def processPygameEvents(self):
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        left_held = pressed[pygame.K_LEFT]
        right_held = pressed[pygame.K_RIGHT]
        up_held = pressed[pygame.K_UP]
        down_held = pressed[pygame.K_DOWN]
        
        if left_held:
            self.moveCameraRelative(-5, 0)
        if right_held:
            self.moveCameraRelative(5, 0)  
        if up_held:
            self.moveCameraRelative(0, -5)  
        if down_held:
            self.moveCameraRelative(0, 5)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()                       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and ctrl_held:
                    pygame.quit()
                    quit()      
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menuRect.collidepoint(event.pos):
                    print("menu")
                    buttonText = self.M.getButton(event.pos[0] - self.menuX, event.pos[1])
                    if buttonText != None:
                        print(buttonText)   

        