import pygame
from pygame import time
from menuView import menuView

pygame.init() 
V = menuView()
clock = time.Clock()
oldTime = time.get_ticks()


mainLoop = True
while(mainLoop):
    clock.tick(24) 
    V = V.processEvents()
    pygame.event.pump()
    V.blitAll()
    V.flip()

        