import pygame
import random 

class Food:
    def __init__(self,display,window_dim,color=[255,0,0],x=0,y=0):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.eaten = False
        self.window_dim = window_dim
        self.food_size = 10
        self.gen_new_position()
        

    def gen_new_position(self):
        while True:
            random_x = random.randrange(0,self.window_dim[0]-self.food_size,self.food_size)
            random_y = random.randrange(0,self.window_dim[1]-self.food_size,self.food_size)
            if random_x > 170 or random_y > 60: 
                self.x = random_x
                self.y = random_y
                self.eaten = False
                break

    def is_food_eaten(self,snake_coordinates):
        if [self.x,self.y] == snake_coordinates:
            self.eaten = True
    
    def draw_food(self):
        pygame.draw.rect(self.display,self.color,[self.x,self.y,self.food_size,self.food_size])


