#main file of my game
import pygame
from settings import global_settings
from characters import protagonist, enemy
from logic_function import deployEnemies
from lvl import level
#here i save all most important varibles


                


class bullet(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height =height
        self.vel = 12
        self.skin =  pygame.image.load('../assets/laserGreen.png')
        #for hit check
        self.rect = pygame.Rect(x, y, width, height)
    def draw(self):
        game.win.blit(self.skin , (self.x, self.y))
        self.y -= 4
         #for hit check
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        


pygame.init()
game = global_settings(900, 900)

def main():
    #redraw window
    def redraw():
        game.draw()
        player.draw()
        for wrog in proba_wroga:
            if wrog.health == 0:
                proba_wroga.pop(proba_wroga.index(wrog))
            else:
              wrog.draw()
        if len(friendly_bullets) != 0:
            for b in friendly_bullets:
                b.draw()
                 #for hit check
                for e in proba_wroga:
                    if b.rect.colliderect(e.rect):
                        friendly_bullets.pop(friendly_bullets.index(b))
                        print("aaaa")
                        e.hit()

    # nie wiem czy to najlepszy pomysł z tym deley
    delayShoot = 0
    player = protagonist(0, 0, 92, 75, game)
    #deployEnemies(rows, length, width,  game, level):
    proba_wroga = deployEnemies(game)
    friendly_bullets = []
    player.draw()
    for wrog in proba_wroga:
        wrog.draw()
    #main loop
    while game.run:
        game.clock.tick(60)#fps
        #handle delay shoot
        if delayShoot != 0:
            delayShoot -= 1

        #handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False
        #handle keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x>0:
            player.x -= player.vel
        elif keys[pygame.K_RIGHT] and game.width > player.x +player.width:
            player.x += player.vel
        if keys[pygame.K_UP] and player.y>0:
            player.y -= player.vel
        elif keys[pygame.K_DOWN]and game.height > player.y+player.height:
            player.y += player.vel
        if keys[pygame.K_SPACE]:
            if delayShoot == 0:
                friendly_bullets.append(bullet(player.x + 45, player.y - 37, 9, 33))
                delayShoot = 22
            else:
                delayShoot -=1
            
        else:
            pass
        
        redraw()
        pygame.display.update()
            
    

main()
