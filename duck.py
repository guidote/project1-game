import pygame

class Player:
    rightSprite = pygame.image.load('data/gfx/player.png')
    leftSprite = pygame.transform.flip(rightSprite, True, False)
    currentSprite = rightSprite
