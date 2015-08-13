import pygame
from pygame import key, time
from userEventHandler import UserEventHandler
import view

pygame.init() 
clock = time.Clock()
V = view.View()
UEH = UserEventHandler()
# UEH.C.createAdamEve()

month = {0: "Jan", 1: "Feb", 2: "Mar", 3: "Apr", 4: "May", 5: "June", 6: "July", 7: "Aug", 8: "Sept", 9: "Oct", 10: "Nov", 11: "Dec"}


oldTime = time.get_ticks()
mainLoop = True
while(mainLoop):
    clock.tick(24)
    
    pressed = key.get_pressed()
    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    left_held = pressed[pygame.K_LEFT]
    right_held = pressed[pygame.K_RIGHT]
    up_held = pressed[pygame.K_UP]
    down_held = pressed[pygame.K_DOWN]
    
    if left_held:
        V.camPos[0] = V.camPos[0] - 5  
    if right_held:
        V.camPos[0] = V.camPos[0] + 5  
    if up_held:
        V.camPos[1] = V.camPos[1] - 5  
    if down_held:
        V.camPos[1] = V.camPos[1] + 5
            
    #pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()                       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c and ctrl_held:
                pygame.quit()
                quit()      
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if V.menuRect.collidepoint(event.pos):
                print("menu")
                buttonText = V.M.getButton(event.pos[0] - V.menuX, event.pos[1])
                if buttonText != None:
                    print(buttonText)                            
    pygame.event.pump()
    
    V.blitAll()
    V.flip()
    
    #user events
    if(time.get_ticks()-oldTime >= 2000):
        oldTime = time.get_ticks()
        UEH.handleEvents()
        