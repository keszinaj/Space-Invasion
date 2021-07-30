import pygame
from lvl import level

class global_settings(object):
    def __init__(self, width, height):
        #size of window
        self.width = width
        self.height = height
        #window
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Space Invasion")
        self.clock = pygame.time.Clock()
        #load background
        self.backg = pygame.image.load("../assets/backg.jpeg")
        self.win.blit(self.backg, (0,0)) #hmm should i delete it?
        self.run = True #hmmm

        # level logic
        self.current_level = 1
        self.levels = {
            1 : level(800, 12, 12, False, False),
            2 : level(800, 12, 0, False, False),
            3 : level(800, 12, 0, False, False),
            4 : level(800, 12, 0, False, False),
            5 : level(800, 12, 0, False, False),
        }
    # to redraw the windows
    def draw(self):
        self.win.blit(self.backg, (0,0))



#tests:
#a = global_settings(200, 200)
#print( a.levels[1].amoun_of_ships)
