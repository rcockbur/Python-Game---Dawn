from pygame.surface import Surface

class Button(object):
    def __init__(self, width, height, text):
        '''
        Constructor
        '''
        self.surface = Surface((width, height))
        self.surface.fill((120,20,20))
        self.text = text