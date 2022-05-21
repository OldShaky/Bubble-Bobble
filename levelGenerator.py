import pygame



class Tile(object):
    def __init__(self, width, height, sprite):
        self.width = width
        self.height = height
        self.sprite = sprite


def drawLvl(lvl, win, Tile):
    rowNo = 0
    for row in lvl:
        colNo = 0
        for tile in row:
            if tile == 'X':
                win.blit(pygame.transform.scale(Tile.sprite, (Tile.width, Tile.height)), (200 + colNo * Tile.width, 100 + rowNo * Tile.height))
            colNo += 1
        rowNo += 1

lvl1 = [
    'XXXXXXXXXXXXXXXXXXXX',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'X                  X',
    'XXXXXXXXXXXXXXXXXXXX'
]
