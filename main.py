import every as every
import pygame
from random import randrange

from pygame import surface

##main code##

RES = 800
size = 50

x, y = randrange(size, RES - size, RES), randrange(size, RES - size, RES)
apple = randrange(size, RES - size, RES), randrange(size, RES - size, RES)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 30


## controler ##
dirs = {'W': True, 'S': True, 'A': True, 'D': True}

score = 0
speed_count, snake_speed = 0, 10

pygame.init()
Surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Times New Roman', 26, bold=True)
font_end = pygame.font.SysFont('Times New Roman', 38, bold=True)
img = pygame.image.load('BackGround.png').convert()


#death#
def close_game():
    for event in pygame.event.get():
        if every.type == pygame.QUIT:
            exit()

##game itself##
while True:
    [pygame.draw.rect(surface, pygame.Color('green'), (i, j, size - 3, size - 3)) for i, j in snake]
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, size, size))


    ##points
    render_score = font_score.render(f'score:{score}', 1, pygame.color('orange'))
    surface.blit(render_score, (5, 5))

    ##finally movement
    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * size
        y += dy * size
        snake.append((x, y))
        snake = snake[-length]

    #food 6:27#

    if snake[-1] == apple:
        apple = randrange(size, RES - size, size), randrange(size, RES - size, size)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)

    #death

    if x < 0 or x > RES - size or y < 0 or y > RES - size or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('Game Over', 1, pygame.color('pink'))
            surface.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            close_game()

    #movement
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, -1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': False}
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': False, 'D': True}