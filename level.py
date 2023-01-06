# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 15:20:45 2023

@author: Caste
"""

import pygame
from pygame import mixer 

class Level:
    def __init__(self, number):
        self.type = type
        if (number == 1):
            self.color = (145, 211, 109)
            self.season = 'Summer'
           # self.sprite = pygame.image.load('weedgreen.png')
            # self.sound = mixer.Sound('filename')
           
        elif (number == 2):
            self.color = (177,97,0)
            self.season = 'Fall'
           # self.sprite = pygame.image.load('weedgreen.png')
            # self.sound = mixer.Sound('filename')
            
        elif (number == 3):
            self.color = (252,252,252)
            self.season = 'Winter'
            # self.sprite = pygame.image.load('weedgreen.png')
            # self.sound = mixer.Sound('filename')
                
        elif (number == 4):
            self.color = (112,220,112)
            self.season = 'Spring'
            # self.sprite = pygame.image.load('weedgreen.png')
            # self.sound = mixer.Sound('filename')


    def change_seasons(self,score):
        if  score%100 > 75 and self.season== 'Winter':
            self.color = (112,220,112)
            self.season = 'Spring'
            # self.sprite = pygame.image.load('weedgreen.png')
            # self.sound = mixer.Sound('filename')
        elif score%100 > 50 and self.season== 'Fall':
            self.color = (252,252,252)
            self.season = 'Winter'
            # self.sprite = pygame.image.load('weedgreen.png')
            # self.sound = mixer.Sound('filename')
        elif score%100 > 25 and self.season== 'Summer':
            self.color = (177,97,0)
            self.season = 'Fall'
           # self.sprite = pygame.image.load('weedgreen.png')
            # self.sound = mixer.Sound('filename')
        elif score%100 <= 25 and self.season =='Spring':
            self.color = (145, 211, 109)
            self.season = 'Summer'
           # self.sprite = pygame.image.load('weedgreen.png')
            # self.sound = mixer.Sound('filename')
           

# GRASS_GREEN = (145, 211, 109)
# FALL_ORANGE = (177,97,0)
# WINTER_WHITE = (252,252,252)
# SPRING_GREEN = (112,220,112)