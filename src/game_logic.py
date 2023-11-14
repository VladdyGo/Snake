import pygame;
from snake_logic import Snake
from food_logic import Food

class Snake_Game:
    def __init__(self,window_size,FPS,snake_loc):
        self.window_size = window_size
        self.FPS = FPS
        self.snake_loc = snake_loc
        self.game_over = False
        self.background_color = (255,255,255)


    def run(self):

        pygame.init()
        display = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption('Snake game by Vladislav')

        font = pygame.font.Font(None,36)

        snake = Snake(display,self.snake_loc,(0,0,0))
        snake.draw_snake()
        food_piece = Food(display,self.window_size)


        clock = pygame.time.Clock()

        # while not self.game_over:
        while True:
            display.fill(self.background_color)
            score_txt = "SCORE: {}".format(snake.size)
            score_txt_render = font.render(score_txt,True,(0,0,0))
            display.blit(score_txt_render,(20,20))
            for event in pygame.event.get(): 
                if event.type==pygame.QUIT:
                    # self.game_over=True
                    pygame.quit()
                    quit()
                    
                if event.type == pygame.KEYDOWN:
                    snake.change_direction(event)

            snake.movement()
            if snake.snake_dead:
                break
            food_piece.draw_food()
            food_piece.is_food_eaten(snake.head_location)
            if(food_piece.eaten == True):
                snake.snake_food_consumption()
                snake.eaten = True
                food_piece.gen_new_position()
            else:
                snake.eaten = False
            snake.draw_snake()
        
            pygame.display.update()
            clock.tick(self.FPS)

        score_txt = "YOUR SCORE IS: {}".format(snake.size)
        score_txt_render = font.render(score_txt,True,(0,0,0))
        display.blit(score_txt_render,(((self.window_size[0] - score_txt_render.get_width()) // 2)
                                       ,((self.window_size[1] - score_txt_render.get_height()) // 2)))
        pygame.display.update()
        
        while True:
            for event in pygame.event.get(): 
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    break
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.run()
                        break

        