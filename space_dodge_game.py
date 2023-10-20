import pygame
import random
import time
import math


def show_time(x, y, timer_text):
    score = font.render("Time:" + str(timer_text) + "s", True, (255, 255, 255))
    win.blit(score, (x, y))


def game_over():
    game_over_text = font.render("Game Over!!!", True, (255, 255, 255))
    win.blit(game_over_text, (300, 240))


def draw():
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    for k in range(total_projectiles):
        pygame.draw.rect(win, (255, 255, 255), (x_projectile[k], y_projectile[k],
                                                projectile_width, projectile_height))

    pygame.display.update()


def collision(x, x_projectile, y, y_projectile):

    for i in range(total_projectiles):

        distance = math.sqrt(math.pow((x - x_projectile[i]), 2) + math.pow((y - y_projectile[i]), 2))
        if distance < 27:
            game_over()
            return True
    return False


pygame.init()

win = pygame.display.set_mode((800, 600))
is_game_over = False

pygame.display.set_caption("Space Dodge")
background_img = pygame.image.load('space_dodge_bg.png')
background_img = pygame.transform.scale(background_img, (800, 600))

start_time = time.time()


x = 250
y = 500
width = 30
height = 40
vel = 10


total_projectiles = 6
x_projectile = []
y_projectile = [0]*total_projectiles
projectile_width = 10
projectile_height = 20


for projectile in range(total_projectiles):
    x_projectile.append(random.randint(100, 800))

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

clock = pygame.time.Clock()


running = True

while running:

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    elapsed_time = time.time() - start_time
    seconds = int(elapsed_time)

    win.blit(background_img, (0, 0))
    pygame.display.flip()




    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x = x - vel
    if keys[pygame.K_RIGHT]:
        x = x + vel

    for i in range(total_projectiles):
        random_speed = random.uniform(5, 15)
        y_projectile[i] = y_projectile[i] + random_speed



    if collision(x, x_projectile, y, y_projectile):
        is_game_over = True
        game_over()
        running = False

    draw()

    clock.tick(60)

    if is_game_over:
        pygame.time.wait(5000)

pygame.quit()
