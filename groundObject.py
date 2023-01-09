# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 18:02:13 2022
Class for objects appearing on screen
Weeds, Flowers and Worms
"""
import pygame
from pygame import mixer 

class GroundObject:
    def __init__(self, type):
        self.type = type
        if (type == 'weed'):
           self.sprite = pygame.image.load('weedgreen.png')
           self.sound = mixer.Sound('data/sfx/weed.wav')
        elif (type == 'flower'):
            self.sprite = pygame.image.load('data/gfx/ground_objects/summer_flower.png')
            self.sound = mixer.Sound('data/sfx/flower.wav')
        else:
            self.sprite = pygame.image.load('wormbrown.png')
            self.sound = mixer.Sound('data/sfx/crunch.wav')
            
        self.position = pygame.Vector2()
        self.position.xy
        
    def change_season(self,season):
        if self.type =='flower':
            self.change_season_flower(season)
            
    def change_season_flower (self,season):
        if season =='Summer':
            self.sprite = pygame.image.load('data/gfx/ground_objects/summer_flower.png')
        elif season =='Spring':
            self.sprite = pygame.image.load('data/gfx/ground_objects/spring_flower.png')
        elif season =='Fall':
             self.sprite = pygame.image.load('data/gfx/ground_objects/fall_flower.png')
        elif season =='Winter':
            self.sprite = pygame.image.load('data/gfx/ground_objects/winter_flower.png')