from pygame.surface import Surface

class button(object):
    def __init__(self, width, height, text):
        self.surface = Surface((width, height))
        self.surface.fill((120,20,20))
        self.text = text