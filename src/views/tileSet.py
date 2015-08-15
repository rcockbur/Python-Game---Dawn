import pygame

# make class Background

class tileSet(object):
    
    def __init__(self, fileName, columns, rows):
        self.sheet = pygame.image.load(fileName)
        self.columns = columns
        self.rows = rows
        self.width = self.sheet.get_width()
        self.height = self.sheet.get_height()
        self.tw = self.width / self.columns
        self.th = self.height / self.rows
        self.tiles = list()
        for x in range(self.columns):
            self.tiles.append(list())
            for y in range(self.rows):
                tile = pygame.Surface((self.tw, self.th))
                tile.blit(self.sheet.subsurface(x*self.tw,y*self.th,self.tw,self.th), (0,0))
                self.tiles[x].append(tile)
    
    def getTile(self, x, y):
        return self.tiles[x][y]
