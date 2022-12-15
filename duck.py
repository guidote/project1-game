import pygame
import time
from enum import Enum

class Duck:
    position = pygame.Vector2()
    position.xy
    default_duck_img = pygame.image.load("data/gfx/waddle_front_0.png")
    width = default_duck_img.get_width()/7
    height = default_duck_img.get_height()/7
    
    '''
    duck_right_imgs = ["waddle_right_0.png","waddle_right_1.png"]
    duck_left_imgs = ["waddle_left_0.png","waddle_left_1.png"]
    duck_front_imgs = ["waddle_front_0.png","waddle_front_1.png"]
    duck_back_imgs = ["waddle_back_0.png","waddle_back_1.png"]
    duck_idle_imgs = ["waddle_idle_0.png","waddle_idle_1.png"]
    
    '''
    def __init__(self):
        pass
     
    def display_duck(self, mouse, screen, movement):
        if movement =='shop':
            pygame.display.update()
            pygame.time.delay(100)
        else:
            indices = [0,1]
            for i in indices:
                img = pygame.image.load("data/gfx/waddle_{0}_{1}.png".format(movement, i))
                duck = pygame.transform.scale(img, (self.width, self.height))
                screen.blit(duck, (mouse[0] - (duck.get_width()/2) ,mouse[1] - (duck.get_height()/2)))
                pygame.display.update()
                pygame.time.delay(100)
    
    def check_pick_up(self, b_x, b_y, b_width, b_height):
        top = self.position.y + self.height/4
        bottom = self.position.y - self.height/4
        left = self.position.x - self.width/4
        right = self.position.x + self.width/4
    
        if (b_x >= left and b_x <= right):
            if (b_y <= top and b_y >= bottom):
                return True
            return False

    def check_duck_position(self, previous_position_x, previous_position_y, position_x, position_y):
        if (position_x > previous_position_x and (position_x - previous_position_x)>10):
            return "right"
        elif (position_x < previous_position_x  and (previous_position_x - position_x)>10):
            return "left"
        elif (position_y > previous_position_y and (position_y - previous_position_y)>10):
            return "front"
        elif (position_y < previous_position_y and (previous_position_y - position_y)>10):
            return "back"   
        else:
            return "idle" # TODO : idle