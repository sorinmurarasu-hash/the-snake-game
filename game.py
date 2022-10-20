import os
from    vardata import *
from    ast     import FloorDiv
from    turtle  import speed
import  pygame
import  random
import  math

class Game:
    def __init__(self):
        pygame.display.set_caption('Snake')

        self.direction                 = '0'
        self.current_head_pos          = (200, 150)
        self.snake                     = [self.current_head_pos]
        self.food                      = ()

        self.game_over              = False
        self.snake_dead             = False
        self.snake_dead_eat_himself = False
        self.snake_eat              = False

    def update_snake_move(self, head: tuple, tail: tuple, eat: bool):
        #cut tail
        color = blue if eat else black
        pygame.draw.rect(dis, color, [tail[0], tail[1], sizex, sizey])
        self.snake.insert(0, head)
        self.snake.pop(-1)
        return

    def check_snake_eat(self, pos: tuple) -> bool:
        os.system('cls')
        print('pos ' + str(pos[0]) + ':' + str(pos[1]) + '   food ' + str(self.food[0]) + ': ' + str(self.food[1]))

        if pos == self.food:
            self.insert_food()
            self.snake.append(pos)
            return True
        else:
            return False
    
    def check_snake_eat_himself(self, head: tuple):
        if head in self.snake:
            return True
        return False

    def check_stepped_outside(self, fromxy: tuple) -> bool:
        if  fromxy[0] < 0 or \
            fromxy[1] < header_height or \
            fromxy[0] > resolution_X - sizex or \
            fromxy[1] > resolution_Y + header_height - sizey:
            return True
        return False

    def draw_text(self, surface, fontFace, size, x, y, text, colour):
        if size in fonts:
            font = fonts[size]
        else:
            font = pygame.font.Font(fontFace, size)
            fonts[size] = font

        text = font.render(text, 1, colour)
        surface.blit(text, (x, y))

    def draw_header(self):
        pygame.draw.rect(dis, header_color, [0, 0, resolution_X, header_height])
        self.draw_text(dis, 'arial.ttf', 28, 5, 5, str(len(self.snake)), (0, 0, 0))
        pygame.draw.line(dis, red, (0, header_height), (resolution_X, header_height), 2)
    
    def draw_grid(self):
        for x in range(sizex, resolution_X, sizex):
            for y in range(header_height + sizex, resolution_Y + header_height, sizex):
                pygame.draw.line(dis, lightgray, (x, header_height + 0), (x, header_height + resolution_Y) )
                pygame.draw.line(dis, lightgray, (0, y), (resolution_X, y) )
                

    def draw_food(self, old_food: tuple, new_food: tuple):
        pygame.draw.rect(dis, red, [new_food[0], new_food[1], sizex, sizey])

    def insert_food(self):
        old_food = self.food
        rx = sizex * random.randint( 0 , (resolution_X - sizex) / sizex ) 
        ry = header_height + sizex * random.randint( 0 , round((resolution_Y - sizex - header_height) / sizex ))
        # rx = random.randint( 0 , resolution_X - sizex )
        # ry = random.randint( header_height , resolution_Y - sizex )
        # rx = math.ceil( rx ) - rx % sizex
        # ry = math.ceil( ry ) - ry % sizex
        self.food = ( rx, ry )
        
        os.system('cls')
        print(str(rx) + ' ' + str(ry))
       
        self.draw_food( old_food, self.food )
    
    def move(self, fromxy: tuple):
        new_head_pos = ()

        if self.direction == 'L':
            new_head_pos = (fromxy[0] - sizex, fromxy[1])
        elif self.direction == 'R':
            new_head_pos = (fromxy[0] + sizex, fromxy[1])
        elif self.direction == 'U':
            new_head_pos = (fromxy[0], fromxy[1] - sizex)
        elif self.direction == 'D':
            new_head_pos = (fromxy[0], fromxy[1] + sizex)
        else:
            new_head_pos = fromxy

        self.snake_dead                     = self.check_stepped_outside(new_head_pos)
        if not self.snake_dead:
            self.snake_dead_eat_himself     = self.check_snake_eat_himself(new_head_pos)
        if not self.snake_dead and not self.snake_dead_eat_himself:
            self.snake_eat                  = self.check_snake_eat(new_head_pos)

        if self.snake_dead or self.snake_dead_eat_himself:
            #return previous point
            return fromxy
        elif self.snake_eat:
            self.update_snake_move(new_head_pos, self.snake[len(self.snake) - 1], True)
        else:
            self.update_snake_move(new_head_pos, self.snake[len(self.snake) - 1], False)

        return new_head_pos