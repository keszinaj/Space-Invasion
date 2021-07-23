#main file of my game
import pygame
from pygame.constants import WINDOWHITTEST

class global_settings(object):
    def __init__(self):
        pass

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.flyLeft = pygame.image.load('../assets/playerLeft.png')
        self.flyRight = pygame.image.load('../assets/playerRight.png')
        self.flyCenter = pygame.image.load('../assets/player.png')

class enemy(object):
    def __init__(self):
        pass

pygame.init()

win = pygame.display.set_mode((650, 480))
pygame.display.set_caption("First Game")
bg = pygame.image.load('../assets/backg.jpeg')