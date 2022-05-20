import pygame


class Player(object):
    def __init__(self, x, y, width, height, spriteSheetMoveLeft, spriteSheetMoveRight):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCounter = 0
        self.vel = 5
        self.standing = False
        self.left = False
        self.right = False
        self.spriteSheetMoveLeft = spriteSheetMoveLeft
        self.spriteSheetMoveRight = spriteSheetMoveRight
        self.scaleFactor = 40

    def draw(self, win):
        if self.walkCounter >= 21:
            self.walkCounter = 0
        if not self.standing:  # if moving
            if self.left:
                win.blit(pygame.transform.scale(self.spriteSheetMoveLeft[self.walkCounter // 3], (self.scaleFactor, self.scaleFactor)), (self.x, self.y))
                self.walkCounter += 1
            elif self.right:
                win.blit(pygame.transform.scale(self.spriteSheetMoveRight[self.walkCounter // 3], (self.scaleFactor, self.scaleFactor)), (self.x, self.y))
                self.walkCounter += 1
        else:  # if standing still
            if self.right:
                win.blit(pygame.transform.scale(self.spriteSheetMoveRight[0], (self.scaleFactor, self.scaleFactor)), (self.x, self.y))
            else:
                win.blit(pygame.transform.scale(self.spriteSheetMoveLeft[0], (self.scaleFactor, self.scaleFactor)), (self.x, self.y))
