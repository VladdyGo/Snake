import pygame
import time

class Snake:
    def __init__(self,display,head_location,head_location_change = [0,0],color=(0,0,255),widght=10):
        self.display = display
        self.size = 0
        self.head_location = head_location
        self.snake = [head_location]
        self.color = color
        self.head_location_change = head_location_change
        self.widght = widght
        self.body_segments = [[self.size,0]]
        self.eaten = False
        self.snake_dead = False

        self.current_time = time.time()
        self.last_move_time = self.current_time
        self.min_time_between_moves = 0.08

    def movement_restrictions_loops(self):
        if(self.head_location[0] >= self.display.get_size()[0]):
                self.head_location[0] = 0

        if(self.head_location[0] < 0):
            self.head_location[0] = self.display.get_size()[0]

        if(self.head_location[1] >= self.display.get_size()[1]):
                self.head_location[1] = 0

        if(self.head_location[1] < 0):
            self.head_location[1] = self.display.get_size()[1]

    def movement_restrictions(self):
        if(self.head_location[0] > self.display.get_size()[0] or self.head_location[0] < 0 
           or self.head_location[1] > self.display.get_size()[1] or self.head_location[1] < 0):
                self.snake_dead = True
        
        if self.size >3 and self.head_location in self.snake[3:]:
             self.snake_dead = True
             pygame.time.delay(1000)

    def movement(self):
            self.head_location = [a + b for a, b in zip(self.head_location,self.head_location_change)]
            self.snake.insert(0,self.head_location)

            if self.eaten == False:
                 self.snake.pop()

            # self.movement_restrictions_loops()
            self.movement_restrictions()

    def change_direction(self,event):
        self.current_time = time.time()
        if self.current_time - self.last_move_time >= self.min_time_between_moves:
            if event.key == pygame.K_a and self.head_location_change != [1 * self.widght,0]:
                self.head_location_change = [-1 * self.widght,0]
                self.last_move_time = self.current_time
            elif event.key == pygame.K_d and self.head_location_change != [-1 * self.widght,0]:
                self.head_location_change = [1 * self.widght,0]
                self.last_move_time = self.current_time
            elif event.key == pygame.K_w and self.head_location_change != [0,1 * self.widght]:
                self.head_location_change = [0,-1 * self.widght]
                self.last_move_time = self.current_time
            elif event.key == pygame.K_s and self.head_location_change != [0,-1 * self.widght]:
                self.head_location_change = [0,1 * self.widght]
                self.last_move_time = self.current_time

    
    def snake_food_consumption(self):
        self.size += 1

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.display,self.color,[segment[0],segment[1],self.widght,self.widght])
