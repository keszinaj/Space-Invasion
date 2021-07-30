import pygame
class level(object):
    def __init__(self, length,  ufo, ship, boss, boss_skin):
        self.length = length
        self.amount_of_ufos = ufo
        self.ufo_skin = pygame.image.load('../assets/enemyUFO.png')
        self.amoun_of_ships = ship
        self.ship_skin = pygame.image.load('../assets/enemyShip.png')
        self.boss = boss
        self.boss_skin = boss_skin