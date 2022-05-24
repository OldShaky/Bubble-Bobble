import pygame



class Tile(object):
    def __init__(self, width, height, sprite):
        self.width = width
        self.height = height
        self.sprite = sprite


lvlHitboxes = []

def drawLvl(lvl, win, Tile):
    rowNo = 0
    for row in lvl:
        colNo = 0
        for tile in row:
            if tile == 'X':
                win.blit(pygame.transform.scale(Tile.sprite, (Tile.width, Tile.height)), (200 + colNo * Tile.width, 100 + rowNo * Tile.height))
                lvlHitboxes.append(pygame.Rect(200 + colNo * Tile.width, 100 + rowNo * Tile.height, Tile.width, Tile.height))
                # pygame.draw.rect(win, (255, 0, 0), lvlHitboxes[-1])
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
    'X      XXXXXX      X',
    'X                  X',
    'X             X    X',
    'X     XXXXXXXXXXXX X',
    'X                  X',
    'X            XX    X',
    'X                  X',
    'XXXXXXXXXXXXXXXXXXXX'
]
