import pygame

class house(object):
    
    def __init__(self, hID):
        self.hID = hID
        self.sprite = pygame.Surface((64,64))
        self.sprite.fill((50,50,50), rect=None, special_flags=0)
        self.owner = None
        self.occupants = list()