import pygame
import time
from enum import Enum

#TODO : fix duck

class Duck:
    position = pygame.Vector2()
    position.xy
    default_duck_img = pygame.image.load("data/gfx/waddle_front_0.png")
    width = default_duck_img.get_width()*5
    height = default_duck_img.get_height()*5

    def __init__(self):
        
        self.images_right = []
        self.images_left = []
        self.images_front = []
        self.images_back = []
        self.images_idle = []
        
        self.images_right.append(pygame.image.load('data/gfx/waddle_right_0.png'))
        self.images_right.append(pygame.image.load('data/gfx/waddle_right_1.png'))
        
        self.images_left.append(pygame.image.load('data/gfx/waddle_left_0.png'))
        self.images_left.append(pygame.image.load('data/gfx/waddle_left_1.png'))
        
        self.images_front.append(pygame.image.load('data/gfx/waddle_front_0.png'))
        self.images_front.append(pygame.image.load('data/gfx/waddle_front_1.png'))
        
        self.images_back.append(pygame.image.load('data/gfx/waddle_back_0.png'))
        self.images_back.append(pygame.image.load('data/gfx/waddle_back_1.png'))
        
        self.images_idle.append(pygame.image.load('data/gfx/waddle_idle_0.png'))
        self.images_idle.append(pygame.image.load('data/gfx/waddle_idle_1.png'))
        
        self.index = 0
        
     
    def display_duck(self, mouse, screen, movement):
        if movement =='shop':
            pygame.display.update()
            pygame.time.delay(100)
        else:
            img = movement[self.index]
            img = pygame.Surface.convert_alpha(img)
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
            return self.images_right
        elif (position_x < previous_position_x  and (previous_position_x - position_x)>10):
            return self.images_left
        elif (position_y > previous_position_y and (position_y - previous_position_y)>10):
            return self.images_front
        elif (position_y < previous_position_y and (previous_position_y - position_y)>10):
            return self.images_back  
        else:
            return self.images_idle # TODO : idle
        
    def update(self, image_type):
        self.index += 1
        #if the index is larger than the total images
        if self.index >= len(image_type):
            #we will make the index to 0 again
            self.index = 0

        return image_type[self.index]