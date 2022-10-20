# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:16:14 2022
"""

def check_pick_up(Duck, b_x, b_y, b_width, b_height):
    top = Duck.position.y + Duck.height/4
    bottom = Duck.position.y - Duck.height/4
    left = Duck.position.x - Duck.width/4
    right = Duck.position.x + Duck.width/4
    
    if (b_x >= left and b_x <= right):
        if (b_y <= top and b_y >= bottom):
            return True
    return False

