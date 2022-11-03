#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:28:47 2022

@author: gabrielleguidote
"""

import pygame

class Title_Screen:
    
    duck_title = pygame.image.load("data/gfx/main_menu/duck_title.png")
    hovered_duck_title = pygame.transform.scale(duck_title, (duck_title.get_width()*1.2, duck_title.get_height()*1.2))
    
    start_title = pygame.image.load("data/gfx/main_menu/start_title.png")
    hovered_start_title =pygame.transform.scale(start_title, (start_title.get_width()*1.2, start_title.get_height()*1.2))
    
    mouse_over = False