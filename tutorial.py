import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First game")

x = 50
y = 50
width = 40
height = 60
vel = 5

player = pygame.Rect(x, y, width, height)

running = True
while running:

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x = player.x - vel
    if keys[pygame.K_RIGHT]:
        player.x = player.x + vel
    if keys[pygame.K_UP]:
        player.y = player.y - vel
    if keys[pygame.K_DOWN]:
        player.y = player.y + vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), player)
    pygame.display.update()

pygame.quit()