import pygame
from pygame import time
from views.menuView import menuView
from userEventHandler import UserEventHandler

pygame.init() 
V = menuView()
UEH = UserEventHandler()
clock = time.Clock()
oldTime = time.get_ticks()
tics = 0


mainLoop = True
while(mainLoop):
    tics += 1
    clock.tick(24) 
    V = V.processEvents()
    if (tics%5 == 0):
        UEH.handleEvents()
    pygame.event.pump()
    V.blitAll()
    V.flip()

        