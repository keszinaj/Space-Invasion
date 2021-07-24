#main file of my game
import pygame
import os
import random
#here i save all most important varibles
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
    # to redraw the windows
    def draw(self):
        self.win.blit(self.backg, (0,0))
        


class protagonist(object):
    def __init__(self, x, y, width, height):
        # x y to spawn protagonist
        self.x = x
        self.y = y
        # height and width of protagonist
        self.width = width
        self.height = height
        #how much on x and y protagonist fly
        self.vel = 3
        #skins for protagonist
        self.flyLeft = pygame.image.load('../assets/playerLeft.png')
        self.flyRight = pygame.image.load('../assets/playerRight.png')
        self.flyCenter = pygame.image.load('../assets/player.png')
    #draw protagonist
    def draw(self):
        game.win.blit(self.flyCenter , (self.x, self.y))


class enemy(object):
    def __init__(self, x, y, width, height):
        # x and y to spawn enemy
        self.x = x
        self.y = y
        self.width = width
        self.height =height
        self.vel = 2
        self.skin = pygame.image.load('../assets/enemyShip.png')
    def draw(self):
        game.win.blit(self.skin , (self.x, self.y))
        #pygame.draw.rect(game.win, (255, 0 ,0), (self.x, self.y, 50, 50), 0)
        self.y += self.vel


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
                list_of_enemies.append(enemy(p_x, -p_y, 10, 10))
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
    def draw(self):
        game.win.blit(self.skin , (self.x, self.y))
        self.y -= 4
        
        


pygame.init()
game = global_settings(1000, 1000)

def main():
    #redraw window
    def redraw():
        game.draw()
        player.draw()
        for wrog in proba_wroga:
            wrog.draw()
        if len(bullets) != 0:
            for b in bullets:
                b.draw()

    # nie wiem czy to najlepszy pomysł z tym deley
    delayShoot = 0
    player = protagonist(0, 0, 99, 75)
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
                bullets.append(bullet(player.x + 45, player.y - 37, 10, 10))
                delayShoot = 22
            else:
                delayShoot -=1
            
        else:
            pass
        
        redraw()
        pygame.display.update()
            
    

main()
