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
            self.sprite = pygame.image.load('flowerpink.jpg')
            self.sound = mixer.Sound('data/sfx/flower.wav')
        else:
            self.sprite = pygame.image.load('wormbrown.png')
            self.sound = mixer.Sound('data/sfx/crunch.wav')
            
        self.position = pygame.Vector2()
        self.position.xy