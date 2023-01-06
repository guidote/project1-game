# -*- coding: utf-8 -*-

import pygame
from duck import Duck
            
def duck_over_rect(rect, mouse):
    if rect.collidepoint(mouse):
        return True
    else:
        return False

class Shop:
    collide = False
    
    # weeds_button = pygame.image.load('data/gfx/weeds_button.png')
    # flowers_button = pygame.image.load('data/gfx/flowers_button.png')
    # worms_button = pygame.image.load('data/gfx/worms_button.png')

    def __init__(self, image, pos, collide = False):
        self.collide = collide
        self.image = pygame.image.load(image)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        
    
    # def hover_button_image(self):
    #     self.hovered_img = pygame.transform.scale(self.image, (self.image.get_width()*1.2, self.image.get_height()*1.2))
    #     self.hovered_rect = self.hovered_img.get_rect(center=(self.x_pos, self.y_pos))
    #     return [self.hovered_img, self.hovered_rect]
        
    def display_shop(self, screen):
        screen.blit(self.image, self.rect)
        pygame.display.update()
    
        