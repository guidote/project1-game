import pygame, sys,random
from pygame.locals import *
from groundObject import GroundObject
from toolkit import check_pick_up, check_duck_position
from duck import Duck
from startup import Title_Screen

def main():
    pygame.init()
    
    game_state = "title_screen"
    
    #Pygame Window
    width, height = 700, 600
    screen = pygame.display.set_mode((width, height))
    
    GRASS_GREEN = (145, 211, 109)
    
    # Getting Images for the shop
    # shop = pygame.image.load('data/gfx/shop.png')
    # weeds_button = pygame.image.load('data/gfx/weeds_button.png')
    # flowers_button = pygame.image.load('data/gfx/flowers_button.png')
    # worms_button = pygame.image.load('data/gfx/worms_button.png')
    
    # buttons = []
    # buttons.append(Button(weeds_button))
    # buttons.append(Button(flowers_button))
    # buttons.append(Button(worms_button))

    #Setting up weeds, flowers and worms
    duck = Duck()
    ground_objects = []
    for i in range(5): ground_objects.append(GroundObject('weed'))
    for i in range(3): ground_objects.append(GroundObject('flower'))
    for i in range(2): ground_objects.append(GroundObject('worm'))

    
    #Assigning them a random starting position
    # TODO: make a check to not generate two items on the same spot OR IN THE SHOP
    for i in ground_objects:
            randomx = random.randrange(screen.get_width() - i.sprite.get_width())
            randomy = random.randrange(screen.get_height() - i.sprite.get_height())
            i.position.xy = randomx, randomy
            
    while game_state == "title_screen":
        game_state = "playing"

        
    #Game Loop
    while game_state == "playing":
        
        screen.fill(GRASS_GREEN)
        # Display Shop and score section
        # DISPLAY.blit(shop, (0, 0))

        # for button in buttons:
        #     DISPLAY.blit(button.sprite, (220 + (buttons.index(button)*125), 393))
        #     priceDisplay = font_small.render(str(button.price), True, (0,0,0))
            
        #     # For later development : LEVELS
        #     #levelDisplay = font_20.render('Lvl. ' + str(button.level), True, (200,200,200))
        #     #DISPLAY.blit(levelDisplay, (234 + (buttons.index(button)*125), 441))
            
        #     counter = font_small.render(str(button.count).zfill(7), True, (0,0,0))
        #    #Below is 2 coordinates that have to depend on the button's position
        #     #DISPLAY.blit(counter, (72, 394))

        
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
                Duck.display_duck(mouse, screen, movement)
                pygame.display.update()
                

            #Check for Pick up and action of GroundObjects
            for i in ground_objects:
                if (check_pick_up(Duck, i.position.x, i.position.y, i.sprite.get_width(), i.sprite.get_height())):
                    # Counters
                    #groud_objects[i].count +=1
                    # Generating a new position
                    randomx = random.randrange(screen.get_width() - i.sprite.get_width())
                    randomy = random.randrange(screen.get_height() - i.sprite.get_height())
                    i.position.xy = randomx, randomy
        
            #To Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            pygame.display.update()
        
main()
    
    
    