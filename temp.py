# -*- coding: utf-8 -*-
#!pip install pygame


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
import pygame, sys,random, math
from pygame.locals import *
from pygame.math import Vector2
from groundObject import GroundObject
from toolkit import check_pick_up
from duck import Duck

def main():
    pygame.init()
    
    MAX_FPS = 60
    
    #Pygame Window
    width, height = 700, 600
    screen = pygame.display.set_mode((width, height))
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRASS_GREEN = (145, 211, 109)
    
    #Setting up weeds, flowers and worms
    duck = Duck()
    weeds = []
    flowers = []
    worms = []
    for i in range(5): weeds.append(GroundObject('weed'))
    for i in range(3): flowers.append(GroundObject('flower'))
    for i in range(2): worms.append(GroundObject('worm'))
    
    #Assigning them a random starting position
    # TODO: make a check to not generate two items on the same spot : Big Array with the positions of eveything?
    # TODO: below can be simplified into one line but it was giving me indentation error
    ground_objects = [weeds,flowers,worms]
    
    # for go in ground_objects:
    #     for element in go[element]:
    #         # add array index
    #     randomx = random.randrange(screen.get_width() - go.sprite.get_width())
    #     randomy = random.randrange(screen.get_height() - go.sprite.get_height())
    #     go.position.xy = randomx, randomy
    
    for weed in weeds:
        randomx = random.randrange(screen.get_width() - weed.sprite.get_width())
        randomy = random.randrange(screen.get_height() - weed.sprite.get_height())
        weed.position.xy = randomx, randomy

    for flower in flowers:
        randomx = random.randrange(screen.get_width() - flower.sprite.get_width())
        randomy = random.randrange(screen.get_height() - flower.sprite.get_height())
        flower.position.xy = randomx, randomy
    
    for worm in worms:
        randomx = random.randrange(screen.get_width() - worm.sprite.get_width())
        randomy = random.randrange(screen.get_height() - worm.sprite.get_height())
        worm.position.xy = randomx, randomy

    #Game Loop
    while True:
        
        screen.fill(GRASS_GREEN)
        
        #Display GroundObjects
        for weed in weeds:
            screen.blit(weed.sprite, weed.position.xy)
        for flower in flowers:
            screen.blit(flower.sprite, flower.position.xy)
        for worm in worms:
            screen.blit(worm.sprite, worm.position.xy)
        
        #Event Handler
        for event in pygame.event.get():
            
            #Mouse Moving Event = Move Duck
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                duck.position.x, duck.position.y = mouse 
                print(pygame.mouse.get_pos())
                Duck.display_duck(event.type, mouse, screen)
                pygame.display.update()
                
            # Check for Pick up and action of GroundObjects
            
            
            for weed in weeds:
                if (check_pick_up(duck.position.x, duck.position.y, Duck.width, Duck.height, weed.position.x, weed.position.y, weed.sprite.get_width(), weed.sprite.get_height())):
                    #This is where we would call the function to do something (add/remove points etc)
                    randomx = random.randrange(screen.get_width() - weed.sprite.get_width())
                    randomy = random.randrange(screen.get_height() - weed.sprite.get_height())
                    weed.position.xy = randomx, randomy
                    
        
            #To Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            pygame.display.update()
            
        #fpsClock.tick(MAX_FPS)
        
main()
    
    
    