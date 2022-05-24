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
        self.jumping = False
        self.jumpCountMax = 8
        self.jumpCount = self.jumpCountMax
        self.spriteSheetMoveLeft = spriteSheetMoveLeft
        self.spriteSheetMoveRight = spriteSheetMoveRight
        self.scaleFactor = 40
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.collideFloor = False
        self.rayCollide = False
        self.collisionRect = pygame.Rect(1, 1, 1, 1)
        self.raycast = pygame.Rect(self.x + 5 if self.right else self.x - 5,
                                   self.y + 5, 5, self.height - 2 * 5)

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
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.raycast = pygame.Rect(self.x + self.width if self.right else self.x - 5, self.y + 5, 5, self.height - 2 * 10)


class Bubble(object):
    def __init__(self, Player, width, height, spriteSheetShootLeft, spriteSheetShootRight):
        self.Player = Player
        self.x = Player.x
        self.y = Player.y - 5
        self.width = width
        self.height = height
        self.left = Player.left
        self.spriteSheetShootLeft = spriteSheetShootLeft
        self.spriteSheetShootRight = spriteSheetShootRight
        self.scaleFactor = 35
        self.shootCounter = 0
        self.hitBox = pygame.Rect(self.x, self.y - 5, self.width, self.height)
        self.bubbleCollide = False

    def draw(self, win):
        if self.shootCounter >= 7:
            win.blit(pygame.transform.scale(self.spriteSheetShootLeft[6],
                                            (self.scaleFactor, self.scaleFactor)), (self.x, self.y))
            if self.left:
                self.x -= 15
            else:
                self.x += 8
        elif self.left and self.shootCounter < 7:
            win.blit(pygame.transform.scale(self.spriteSheetShootLeft[self.shootCounter],
                                            (self.scaleFactor, self.scaleFactor)), (self.x, self.y))
            self.x -= 8
        elif not self.left and self.shootCounter < 7:
            win.blit(pygame.transform.scale(self.spriteSheetShootLeft[self.shootCounter],
                                            (self.scaleFactor, self.scaleFactor)), (self.x + self.Player.width, self.y))
        self.shootCounter += 1
        if self.left:
            self.hitBox = pygame.Rect(self.x, self.y - 5, self.width, self.height)
        else:
            self.hitBox = pygame.Rect(self.x + self.Player.width, self.y - 5, self.width, self.height)
