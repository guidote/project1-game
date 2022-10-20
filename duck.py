import pygame
import time

class Duck:
    
    '''
    duck_right_imgs = ["waddle_right_0.png","waddle_right_1.png"]
    duck_left_imgs = ["waddle_left_0.png","waddle_left_1.png"]
    duck_front_imgs = ["waddle_front_0.png","waddle_front_1.png"]
    duck_back_imgs = ["waddle_back_0.png","waddle_back_1.png"]
    '''
        
    def display_duck(movement_state, mouse, screen):
        indices = [0,1]
        
        if movement_state == pygame.MOUSEMOTION:
            for i in indices:
                img = pygame.image.load("data/gfx/waddle_right_{}.png".format(i))
                duck = pygame.transform.scale(img, (img.get_width()/7, img.get_height()/7))
                screen.blit(duck, (mouse[0] - (duck.get_width()/2) ,mouse[1] - (duck.get_width()/2)))
                pygame.display.update()
                pygame.time.delay(100)
            
        
        
        
