import pygame
import random
import time


def show_time(x, y, timer_text):
    score = font.render("Time:" + str(timer_text) + "s", True, (255, 255, 255))

    win.blit(score, (x, y))


def game_over():
    game_over_text = font.render(f"Game Over!", True, (255, 184, 76))
    win.blit(game_over_text, (300, 240))


pygame.init()

win = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Dodge")
background_img = pygame.image.load('space_dodge_bg.png')
background_img = pygame.transform.scale(background_img, (800, 600))
start_time = time.time()

x, y, width, height = 250, 500, 30, 40
vel = 10
player = pygame.Rect(x, y, width, height)

font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

x_projectile, y_projectile, width_projectile, height_projectile = 200, -20, 10, 20
total_projectiles = 0
projectiles = []
projectile_vel = 5
projectile_increase_interval = 2000  # 10 seconds in milliseconds
speed_increase_interval = 2000  # 10 seconds in milliseconds
a, b = 1, 5
count = 0

clock = pygame.time.Clock()
time_elapsed = 0
running = True
is_game_over = False

while running:

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time_elapsed = time_elapsed + clock.get_time()
    seconds = int(time.time() - start_time)

    win.blit(background_img, (0, 0))
    pygame.display.flip()
    show_time(textX, textY, seconds)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x = player.x - vel
    if keys[pygame.K_RIGHT]:
        player.x = player.x + vel
    if player.x >= 800 - width:
        player.x = 800 - width
    if player.x <= 0:
        player.x = 0

    if time_elapsed >= projectile_increase_interval:
        x = random.randint(a, b)
        a = a + 1
        b = b + 1

        count = count + 1

        if count == 20:

            count = 0
            a = 1
            b = 5

        for _ in range(x):
            projectile = pygame.Rect(random.randint(0, 800), y_projectile, width_projectile, height_projectile)
            projectiles.append(projectile)

        total_projectiles = total_projectiles + x

        time_elapsed = 0

    if time_elapsed >= speed_increase_interval:
        projectile_vel = projectile_vel + total_projectiles
        time_elapsed = 0

    pygame.draw.rect(win, (255, 0, 0), player)
    for i in range(total_projectiles):
        projectiles[i].y = projectiles[i].y + random.randint(5, 15)
        pygame.draw.rect(win, (255, 255, 255), projectiles[i])

        if player.colliderect(projectiles[i]):
            is_game_over = True
            game_over()
            running = False

    clock.tick(60)

    pygame.display.update()

    if is_game_over:
        pygame.time.wait(5000)

pygame.quit()
