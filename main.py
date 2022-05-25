import pygame
from spriteHandler import spritesheet
import moveableObjects
import levelGenerator


pygame.init()

# generate window
screenWidth = 1200
screenHeight = 900
print(screenWidth)
print(screenHeight)
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Bubblez")

# Generete lvl tile
tileSpriteSheet = spritesheet('tileSpriteSheet.png')
tile1Sprite = tileSpriteSheet.image_at((52, 4, 15, 15)) #colorkey=(0, 64, 64)
tile1 = levelGenerator.Tile(40, 40, tile1Sprite)


# generate player animations
spriteSheet = spritesheet("spriteSheet645x1746.png")
moveLeft = spriteSheet.images_at([(4, 15, 20, 20), (25, 15, 20, 20), (46, 15, 20, 20), (67, 15, 20, 20), (88, 15, 20, 20), (109, 15, 20, 20), (128, 15, 20, 20)], colorkey=(15, 79, 174))
moveRight = spriteSheet.flip_strip(moveLeft)

# generate bubble animations
bubbleLeft = spriteSheet.images_at([(5, 1050, 18, 18), (22, 1050, 18, 18), (39, 1050, 18, 18), (58, 1050, 20, 20), (76, 1050, 20, 20), (94, 1050, 20, 20)], colorkey=(15, 79, 174))
bubbleLeft.append(spriteSheet.image_at((5, 1070, 18, 18), colorkey=(15, 79, 174)))
bubbleLeft.append(spriteSheet.image_at((22, 1070, 18, 18), colorkey=(15, 79, 174)))
bubbleList = []

clock = pygame.time.Clock()
player1 = moveableObjects.Player(900, 550, 35, 35, moveLeft, moveRight)


def RedrawGameWindow():
    win.fill((0, 0, 0))
    player1.draw(win)
#    for (b, i) in zip(bubbleLeft, range(len(bubbleLeft))):     # drawing example
#        win.blit(b, (300 + 50 * i, 400))
    if not len(bubbleList) == 0:  # if there are any bubbles
        for bubz in bubbleList:
            if bubz.shootCounter >= 70:
                bubbleList.remove(bubz)
            else:
                bubz.draw(win)
    # draw lvl 1
    levelGenerator.drawLvl(levelGenerator.lvl1, win, tile1)
    # update display
    pygame.display.update()


running = True
while running:
    clock.tick(30)
    player1.collideFloor = False
    for rect in levelGenerator.lvlHitboxes:     # check player collide
        player1.collideFloor = pygame.Rect.colliderect(player1.hitbox, rect)
        if player1.collideFloor:
            player1.collisionRect = rect
            break
    if not len(bubbleList) == 0:
        for rect in levelGenerator.lvlHitboxes:     # check last bubble collide
            for bubz in bubbleList:
                if pygame.Rect.colliderect(bubz.hitBox, rect):
                    bubbleList.remove(bubz)
    if not player1.collideFloor and not player1.jumping:  # freefall
        player1.y += 7
    elif player1.collideFloor and player1.jumping:        # jumping + collision
        player1.y += 7
    elif player1.collideFloor and not player1.jumping:    # landing on collisionRect
        player1.y = player1.collisionRect.y - player1.height + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_LEFT] and not player1.jumping:
        player1.left = True
        player1.right = False
        player1.standing = False
        for rect in levelGenerator.lvlHitboxes:
            player1.rayCollide = pygame.Rect.colliderect(player1.raycast, rect)
            if player1.rayCollide:
                break
        if player1.rayCollide:
            player1.x += 1
        else:
            player1.x -= player1.vel
    elif keys[pygame.K_RIGHT] and not player1.jumping:
        player1.left = False
        player1.right = True
        player1.standing = False
        for rect in levelGenerator.lvlHitboxes:
            player1.rayCollide = pygame.Rect.colliderect(player1.raycast, rect)
            if player1.rayCollide:
                break
        if player1.rayCollide:
            player1.x -= 1
        else:
            player1.x += player1.vel
    if keys[pygame.K_LCTRL]:
        if not len(bubbleList) == 0:    # if there are bubbles fired
            if bubbleList[-1].shootCounter > 6:     # previous bub happened at least 5 ticks ago
                bubble = moveableObjects.Bubble(player1, player1.width, player1.height - 10, bubbleLeft, bubbleLeft)
                bubbleList.append(bubble)
        else:
            bubble = moveableObjects.Bubble(player1, 30, 30, bubbleLeft, bubbleLeft)
            bubbleList.append(bubble)
    else:
        player1.standing = True

    if not player1.jumping:  # if not jumping
        if keys[pygame.K_UP] and player1.collideFloor:
            player1.jumping = True
            player1.walkCount = 0
    else:   # if jumping
        if player1.jumpCount > 0:    # jump active
            player1.y -= (player1.jumpCount ** 2) * 0.8
            player1.jumpCount -= 1
        else:
            if player1.collideFloor:
                player1.jumping = True
            else:
                player1.jumping = False
                player1.jumpCount = player1.jumpCountMax

    RedrawGameWindow()

pygame.quit()
