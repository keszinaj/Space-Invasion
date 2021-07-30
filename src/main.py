#main file of my game
import pygame
import os
import random
from settings import global_settings
from characters import protagonist, enemy
#here i save all most important varibles

# no ta funkcja to jest na 100% do poprawy ale na razie zostawie tak jak jest bo skupmy się na działaniu samej gry
def deployEnemies(n, rows, length):
        list_of_enemies = []
        p_y = 0

        first_y = length / rows    
        first_y_prev = first_y    
        for i in range(rows):
            p_x = 0
            firs_col = 600/n #to trzebas zmenić <-------
            for j in range(n):
                p_x = random.randint(p_x, firs_col)
                p_y = random.randint(p_y, first_y )
                print(" x = ", p_x)
                #dobra to gówno ale zobaczmy jak działa
                firs_col += firs_col
                list_of_enemies.append(enemy(p_x, -p_y, 92, 92, pygame.image.load('../assets/enemyUFO.png'), game))
            first_y  += first_y_prev
                
        return list_of_enemies
                


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
        if len(bullets) != 0:
            for b in bullets:
                b.draw()
                 #for hit check
                for e in proba_wroga:
                    if b.rect.colliderect(e.rect):
                        bullets.pop(bullets.index(b))
                        print("aaaa")
                        e.hit()

    # nie wiem czy to najlepszy pomysł z tym deley
    delayShoot = 0
    player = protagonist(0, 0, 92, 75, game)
    proba_wroga = deployEnemies(2, 5, 800)
    bullets = []
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
                bullets.append(bullet(player.x + 45, player.y - 37, 9, 33))
                delayShoot = 22
            else:
                delayShoot -=1
            
        else:
            pass
        
        redraw()
        pygame.display.update()
            
    

main()
