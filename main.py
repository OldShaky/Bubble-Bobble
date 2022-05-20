import pygame
from spriteHandler import spritesheet
import moveableObjects

pygame.init()

screenWidth = 1900
screenHeight = 1000
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Bubblez")


spriteSheet = spritesheet("spriteSheet645x1746.png")
testSprite = spriteSheet.image_at((4, 14, 20, 20))
moveRight = spriteSheet.load_strip((4, 14, 20, 20), 7)

clock = pygame.time.Clock()
player1 = moveableObjects.Player(200, 500, 20, 20, moveRight, moveRight)

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
    if keys[pygame.K_LEFT]:
        player1.x -= player1.vel
        player1.left = True
    if keys[pygame.K_RIGHT]:
        player1.x += player1.vel
        player1.right = True
    RedrawGameWindow()

pygame.quit()
