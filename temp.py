import pygame, sys,random, math
from pygame.locals import *
from pygame.math import Vector2
from groundObject import GroundObject
from toolkit import check_pick_up, check_duck_position
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
    ground_objects = []
    for i in range(5): ground_objects.append(GroundObject('weed'))
    for i in range(3): ground_objects.append(GroundObject('flower'))
    for i in range(2): ground_objects.append(GroundObject('worm'))
    
    #Assigning them a random starting position
    # TODO: make a check to not generate two items on the same spot
    # TODO: below can be simplified into one line but it was giving me indentation error
    for i in ground_objects:
            randomx = random.randrange(screen.get_width() - i.sprite.get_width())
            randomy = random.randrange(screen.get_height() - i.sprite.get_height())
            i.position.xy = randomx, randomy

    #Game Loop
    while True:
        
        screen.fill(GRASS_GREEN)
        
        #Display GroundObjects
        for i in ground_objects:
            screen.blit(i.sprite, i.position.xy)
            
        # Duck Previous Position
        mouse = pygame.mouse.get_pos()
        previous_position_x = mouse[0]
        previous_position_y = mouse[1]
        
        #Event Handler
        for event in pygame.event.get():
            
            # Mouse Moving Event = Move Duck
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                Duck.position.x, Duck.position.y = mouse 

                movement = check_duck_position(previous_position_x, previous_position_y, mouse[0], mouse[1])
                print("(1)", previous_position_x , " --- " , mouse[0])
                Duck.display_duck(mouse, screen, movement)
                pygame.display.update()
                

            #Check for Pick up and action of GroundObjects
            for i in ground_objects:
                if (check_pick_up(Duck, i.position.x, i.position.y, i.sprite.get_width(), i.sprite.get_height())):
                    randomx = random.randrange(screen.get_width() - i.sprite.get_width())
                    randomy = random.randrange(screen.get_height() - i.sprite.get_height())
                    i.position.xy = randomx, randomy
        
            #To Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            pygame.display.update()
            
        #fpsClock.tick(MAX_FPS)
        
main()
    
    
    