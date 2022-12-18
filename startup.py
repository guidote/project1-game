import pygame

def mouse_over_rect(rect, mouse):
    if rect.collidepoint(mouse):
        return True
    else:
        return False
            
class Menu_Button:
    
    collide = False

    def __init__(self, image, pos, collide = False):
        self.image = image
        self.collide = collide
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    
    def hover_button_image(self):
        self.hovered_img = pygame.transform.scale(self.image, (self.image.get_width()*1.2, self.image.get_height()*1.2))
        self.hovered_rect = self.hovered_img.get_rect(center=(self.x_pos, self.y_pos))
        return [self.hovered_img, self.hovered_rect]
        
    def display_button_image(self, screen, mouse):
        self.collide = mouse_over_rect(self.rect, mouse)
        
        if self.collide:
            screen.blit(self.hover_button_image()[0], self.hover_button_image()[1])
        else:
            screen.blit(self.image, self.rect)
    
        