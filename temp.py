# -*- coding: utf-8 -*-
#! pip install pygame


'''
#Pygame base template for opening a window
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

'''
import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    
    MAX_FPS = 60
    
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRASS_GREEN = (145, 211, 109)
    
    while True:
        
        screen.fill(GRASS_GREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                print(pygame.mouse.get_pos())
                pygame.draw.rect(screen, BLACK, pygame.Rect(mouse[0], mouse[1], 50, 50))
                pygame.display.flip()
    
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            pygame.display.update()
            
        #fpsClock.tick(MAX_FPS)
        
main()
    
    
    