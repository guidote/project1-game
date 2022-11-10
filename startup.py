import pygame

class Title_Screen:
    
    center_position = (200, 200)
    lower_center_position = (350, 200)
    
    ## TODO: if mouse over use one image else use other
    img = pygame.image.load("data/gfx/main_menu/duck_title.png")
    duck_title = pygame.transform.scale(img, (img.get_width()/1.5, img.get_height()/1.5))
    hovered_duck_title = pygame.transform.scale(duck_title, (duck_title.get_width()*1.2, duck_title.get_height()*1.2))
    
    img = pygame.image.load("data/gfx/main_menu/start_title.png")
    start_title = pygame.transform.scale(img, (img.get_width()/1.5, img.get_height()/1.5))
    hovered_start_title = pygame.transform.scale(start_title, (start_title.get_width()*1.2, start_title.get_height()*1.2))
    
    hover = False
    text_rect = duck_title.get_rect()
    text_rect.center = center_position
    
    
    def mouse_over(mouse):
        if Title_Screen.text_rect.collidepoint(mouse):
            Title_Screen.hover = True
        else:
            Title_Screen.hover = False
    
    def display_duck_title(screen, mouse):
        Title_Screen.mouse_over(mouse)
    
        if Title_Screen.hover:
            screen.blit(Title_Screen.hovered_duck_title, Title_Screen.text_rect)
            pygame.display.update()
        else:
            screen.blit(Title_Screen.duck_title, Title_Screen.text_rect)
            pygame.display.update()
        