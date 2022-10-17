from ast import FloorDiv
from turtle import speed
import pygame
import random
import math

resolution_X        = 640
resolution_Y        = 480
header_height       = 50

dis = pygame.display.set_mode((resolution_X, resolution_Y + header_height ))
 
pygame.display.set_caption('Snake')
 
blue                = ( 0, 0, 255 )
red                 = ( 255, 0, 0 )
black               = ( 0, 0, 0 )
header_color        = ( 100, 100, 100 )
fonts = {}

clock = pygame.time.Clock()

sizex, sizey        = 10, 10
direction           = 0
step                = 10
speed               = 20
current_head_pos    = (200, 150)
snake               = [current_head_pos]
food                = ()

game_over       = False
snake_dead      = False
snake_length    = 1

def move(fromxy: tuple, direction: str):
    new_head_pos = ()
    global snake_dead, snake_length

    if direction == 'L':
        new_head_pos = (fromxy[0] - step, fromxy[1])
    elif direction == 'R':
        new_head_pos = (fromxy[0] + step, fromxy[1])
    elif direction == 'U':
        new_head_pos = (fromxy[0], fromxy[1] - step)
    elif direction == 'D':
        new_head_pos = (fromxy[0], fromxy[1] + step)
    else:
        new_head_pos = fromxy

    snake_dead = check_stepped_outside(new_head_pos)
    check_snake_eat(new_head_pos)

    if snake_dead:
        #return previous point
        return fromxy
    else:
        update_snake_cut_tail(fromxy)

    return new_head_pos

def update_snake_cut_tail(tailxy: tuple):
    #cut tail
    pygame.draw.rect(dis, black, [tailxy[0], tailxy[1], sizex, sizey])

    return

def check_snake_eat(pos: tuple) -> bool:
    if pos == food:
        insert_food()
        return True
    else:
        return False

def check_stepped_outside(fromxy: tuple) -> bool:
    if  fromxy[0] < 0 or \
        fromxy[1] < header_height or \
        fromxy[0] > resolution_X - sizex or \
        fromxy[1] > resolution_Y + header_height - sizey:
        return True
    return False

def draw_text(surface, fontFace, size, x, y, text, colour):
    if size in fonts:
        font = fonts[size]
    else:
        font = pygame.font.Font(fontFace, size)
        fonts[size] = font

    text = font.render(text, 1, colour)
    surface.blit(text, (x, y))

def draw_header():
    pygame.draw.rect(dis, header_color, [0, 0, resolution_X, header_height])
    # dis.fill((255, 255, 255))
    draw_text(dis, 'arial.ttf', 32, 5, 5, str(snake_length), (0, 0, 0))

def draw_food(old_food: tuple, new_food: tuple):
    pygame.draw.rect(dis, red, [new_food[0], new_food[1], sizex, sizey])
    if old_food is None:
        pygame.draw.rect(dis, black, [old_food[0], old_food[1], sizex, sizey])

def insert_food():
    global food
    old_food = food
    rx = random.randint(0 , resolution_X - step)
    ry = random.randint(0 , resolution_Y - step)
    rx = math.ceil(rx) - rx % 10
    ry = math.ceil(ry) - ry % 10
    food = (rx, ry)
    draw_food(old_food, food)



pygame.init()
draw_header()
insert_food()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'L'
            elif event.key == pygame.K_RIGHT:
                direction = 'R'
            elif event.key == pygame.K_UP:
                direction = 'U'
            elif event.key == pygame.K_DOWN:
                direction = 'D'  

    if not snake_dead:
        current_head_pos = move(current_head_pos, direction)
        pygame.draw.rect(dis, blue, [current_head_pos[0], current_head_pos[1], sizex, sizey])
    else:
        pygame.draw.rect(dis, red, [current_head_pos[0], current_head_pos[1], sizex, sizey])
        direction = 0
    
    #draw_food()
    draw_header()
    clock.tick(speed)
    pygame.display.update()
    
    
pygame.quit()
quit()

