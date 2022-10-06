# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 18:02:13 2022
Class for objects appearing on screen
Weeds, Flowers and Worms
"""
import pygame

class GroundObject:
    def __init__(self, type):
        if (type == 'weed'):
           self.sprite = pygame.image.load('weedgreen.png')
        elif (type == 'flower'):
            self.sprite = pygame.image.load('flowerpink.jpg')
        else:
            self.sprite = pygame.image.load('wormbrown.png')
        self.position = pygame.Vector2()
        self.position.xy