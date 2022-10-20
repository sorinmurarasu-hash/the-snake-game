import  pygame
from    ast     import FloorDiv
from    turtle  import speed
from    game    import Game
from    vardata import *

game  = Game()
       
if __name__ == "__main__":
    game.draw_header()
    game.draw_grid()
    game.insert_food()

    while not game.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not game.direction == 'R':
                    game.direction = 'L'
                elif event.key == pygame.K_RIGHT and not game.direction == 'L':
                    game.direction = 'R'
                elif event.key == pygame.K_UP and not game.direction == 'D':
                    game.direction = 'U'
                elif event.key == pygame.K_DOWN and not game.direction == 'U':
                    game.direction = 'D' 
                elif game.snake_dead and event.key == pygame.K_RETURN:
                    game.direction = '0'
                    game.snake_dead = False  

        if not game.snake_dead:
            game.current_head_pos = game.move( game.current_head_pos )
            pygame.draw.rect(dis, white, [game.current_head_pos[0], game.current_head_pos[1], sizex, sizey])

        else:
            pygame.draw.rect(dis, red, [game.current_head_pos[0], game.current_head_pos[1], sizex, sizey])
            game.direction = 0
    
        game.draw_header()
        game.draw_grid()
        clock.tick(speed)
        pygame.display.update()
    
    pygame.quit()
    quit()