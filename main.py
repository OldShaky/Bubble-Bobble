import pygame
from spriteHandler import spritesheet
import moveableObjects

pygame.init()

screenWidth = 1900
screenHeight = 1000
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Bubblez")

spriteSheet = spritesheet("spriteSheet645x1746.png")
moveLeft = spriteSheet.load_strip((4, 15, 20, 20), 7)
moveRight = spriteSheet.flip_strip(moveLeft)

clock = pygame.time.Clock()
player1 = moveableObjects.Player(200, 500, 40, 40, moveLeft, moveRight)

def RedrawGameWindow():
    win.fill((0, 0, 0))
    player1.draw(win)
    c = 10
    for i in moveLeft:
        win.blit(pygame.transform.scale(i, (60, 60)), (c, c))
        c += 70
    pygame.display.update()

#sprites er 20x20 ish
running = True
while running:

    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_LEFT] and player1.x > 5:
        player1.x -= player1.vel
        player1.left = True
        player1.right = False
        player1.standing = False
    elif keys[pygame.K_RIGHT] and player1.x + player1.width + player1.vel < screenWidth:
        player1.x += player1.vel
        player1.left = False
        player1.right = True
        player1.standing = False
    else:
        player1.standing = True

    RedrawGameWindow()

pygame.quit()
