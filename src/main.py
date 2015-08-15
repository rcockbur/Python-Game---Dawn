import pygame
from pygame import key, time
from userEventHandler import UserEventHandler
import view

pygame.init() 
V = view.view()
UEH = UserEventHandler()
clock = time.Clock()
oldTime = time.get_ticks()

mainLoop = True
while(mainLoop):
    clock.tick(24)
    V.processPygameEvents()
    pygame.event.pump()
    V.blitAll()
    V.flip()
    if(time.get_ticks()-oldTime >= 2000):
        oldTime = time.get_ticks()
        UEH.handleEvents()
        