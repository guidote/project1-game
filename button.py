# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:31:46 2022

@author: Caste
"""

import pygame

class Button:
    def __init__(self, button_image):
        self.count = 0
        # FOR LATER DEVELOPMENT : LEVELS
        #self.level = 1   
        self.sprite = button_image