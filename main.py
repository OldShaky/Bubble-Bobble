import pygame
from spriteHandler import spritesheet
import moveableObjects

pygame.init()

screenWidth = 1900
screenHeight = 1000
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Bubblez")

spriteSheet = spritesheet("spriteSheet645x1746.png")
moveLeft = spriteSheet.images_at([(4, 15, 20, 20), (25, 15, 20, 20), (46, 15, 20, 20), (67, 15, 20, 20), (88, 15, 20, 20), (109, 15, 20, 20), (128, 15, 20, 20)], colorkey=(15, 79, 174))
moveRight = spriteSheet.flip_strip(moveLeft)

clock = pygame.time.Clock()
player1 = moveableObjects.Player(200, 500, 40, 40, moveLeft, moveRight)

def RedrawGameWindow():
    win.fill((0, 0, 0))
    player1.draw(win)
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

    if not player1.jumping:  # if not jumping
        if keys[pygame.K_UP]:
            player1.jumping = True
            player1.walkCount = 0
    else:   # if jumping
        if player1.jumpCount >= -4:    # jump happens when jumpCount > -10
            neg = 1
            if player1.jumpCount < 0:
                neg = -1
            player1.y -= (player1.jumpCount ** 2) * 4 * neg
            player1.jumpCount -= 1
        else:
            player1.jumping = False
            player1.jumpCount = 4

    RedrawGameWindow()

pygame.quit()
