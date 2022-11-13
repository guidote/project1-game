import pygame, sys,random
from pygame.locals import *
from groundObject import GroundObject
import toolkit
from duck import Duck
from startup import Title_Screen

# Pygame Window
WIDTH, HEIGHT = 700, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
GRASS_GREEN = (145, 211, 109)

def main_menu():
    pygame.display.set_caption("Duck Menu")
    
    #Create title screen
    title_screen = Title_Screen()
    
    while True:
        SCREEN.fill(GRASS_GREEN)
        mouse = pygame.mouse.get_pos()
        
        title_screen.display_duck_title(SCREEN, mouse)
        
        for event in pygame.event.get():
            # Mouse click start playing
            if event.type == pygame.MOUSEBUTTONDOWN:
                if title_screen.collide:
                    play()
                
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
def play():
    pygame.display.set_caption("Duck Game")
    
    #Create a duck
    duck = Duck()
    
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
    ground_objects = []
    for i in range(5): ground_objects.append(GroundObject('weed'))
    for i in range(3): ground_objects.append(GroundObject('flower'))
    for i in range(2): ground_objects.append(GroundObject('worm'))

    
    #Assigning them a random starting position
    # TODO: make a check to not generate two items on the same spot OR IN THE SHOP
    for i in ground_objects:
            randomx = random.randrange(SCREEN.get_width() - i.sprite.get_width())
            randomy = random.randrange(SCREEN.get_height() - i.sprite.get_height())
            i.position.xy = randomx, randomy

    while True:
        
        SCREEN.fill(GRASS_GREEN)
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
            SCREEN.blit(i.sprite, i.position.xy)
            
            
        # Duck Previous Position
        mouse = pygame.mouse.get_pos()
        previous_position_x = mouse[0]
        previous_position_y = mouse[1]
        
        #Event Handler
        for event in pygame.event.get():
            
            # Mouse Moving Event = Move Duck
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                duck.position.x, duck.position.y = mouse 

                movement = duck.check_duck_position(previous_position_x, previous_position_y, mouse[0], mouse[1])
                duck.display_duck(mouse, SCREEN, movement)
                pygame.display.update()
                

            #Check for Pick up and action of GroundObjects
            for i in ground_objects:
                if (duck.check_pick_up(i.position.x, i.position.y, i.sprite.get_width(), i.sprite.get_height())):
                    # Counters
                    #groud_objects[i].count +=1
                    # Generating a new position
                    randomx = random.randrange(SCREEN.get_width() - i.sprite.get_width())
                    randomy = random.randrange(SCREEN.get_height() - i.sprite.get_height())
                    i.position.xy = randomx, randomy
        
            #To Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            pygame.display.update()
    

def main():
    
    # SET UP
    pygame.init()
    
    game_state = "title_screen"
    
    #Pygame Window
    width, height = 700, 600
    SCREEN = pygame.display.set_mode((width, height))
    
    GRASS_GREEN = (145, 211, 109)
    
    #Create a duck
    duck = Duck()
    
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
    ground_objects = []
    for i in range(5): ground_objects.append(GroundObject('weed'))
    for i in range(3): ground_objects.append(GroundObject('flower'))
    for i in range(2): ground_objects.append(GroundObject('worm'))

    
    #Assigning them a random starting position
    # TODO: make a check to not generate two items on the same spot OR IN THE SHOP
    for i in ground_objects:
            randomx = random.randrange(SCREEN.get_width() - i.sprite.get_width())
            randomy = random.randrange(SCREEN.get_height() - i.sprite.get_height())
            i.position.xy = randomx, randomy
       
    # TITLE SCREEN
    title_screen = Title_Screen()
    while game_state == "title_screen":
        
        SCREEN.fill(GRASS_GREEN)
        mouse = pygame.mouse.get_pos()
        
        title_screen.display_duck_title(SCREEN,mouse)
        
        for event in pygame.event.get():
            # Mouse click start playing
            if event.type == pygame.MOUSEBUTTONDOWN:
                if title_screen.hover:
                    game_state = "playing"
                
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        
    # GAME LOOP
    while game_state == "playing":
        
        SCREEN.fill(GRASS_GREEN)
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
            SCREEN.blit(i.sprite, i.position.xy)
            
            
        # Duck Previous Position
        mouse = pygame.mouse.get_pos()
        previous_position_x = mouse[0]
        previous_position_y = mouse[1]
        
        #Event Handler
        for event in pygame.event.get():
            
            # Mouse Moving Event = Move Duck
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
                duck.position.x, duck.position.y = mouse 

                movement = duck.check_duck_position(previous_position_x, previous_position_y, mouse[0], mouse[1])
                duck.display_duck(mouse, SCREEN, movement)
                pygame.display.update()
                

            #Check for Pick up and action of GroundObjects
            for i in ground_objects:
                if (duck.check_pick_up(i.position.x, i.position.y, i.sprite.get_width(), i.sprite.get_height())):
                    # Counters
                    #groud_objects[i].count +=1
                    # Generating a new position
                    randomx = random.randrange(SCREEN.get_width() - i.sprite.get_width())
                    randomy = random.randrange(SCREEN.get_height() - i.sprite.get_height())
                    i.position.xy = randomx, randomy
        
            #To Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            pygame.display.update()
        
main_menu()
    
    
    