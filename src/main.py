#main file of my game
import pygame
import os


class global_settings(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Space Invasion")
        #load background
        self.backg = pygame.image.load("../assets/backg.jpeg")
        self.win.blit(self.backg, (0,0))
        self.run = True
    def draw(self):
        self.win.blit(self.backg, (0,0))
        


class protagonist(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.flyLeft = pygame.image.load('../assets/playerLeft.png')
        self.flyRight = pygame.image.load('../assets/playerRight.png')
        self.flyCenter = pygame.image.load('../assets/player.png')
    def draw(self):
        game.win.blit(self.flyCenter , (self.x, self.y))


class enemy(object):
    def __init__(self):
        pass

pygame.init()

game = global_settings(600, 600)
def main():
    def redraw():
        game.draw()
        player.draw()

    player = protagonist(15, 15, 99, 75)
    player.draw()
    while game.run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x>0:
            player.x -= player.vel
        elif keys[pygame.K_RIGHT] and game.width > player.x +player.width:
            player.x += player.vel
        if keys[pygame.K_UP] and player.y>0:
            player.y -= player.vel
        elif keys[pygame.K_DOWN]and game.height > player.y+player.height:
            player.y += player.vel
        else:
            pass
        redraw()
        pygame.display.update()
            
    

main()
