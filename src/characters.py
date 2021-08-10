import pygame

class bullet(object):
    def __init__(self, w,  x, y, width, height, game):
        self.w = w
        self.x = x
        self.y = y
        self.width = width
        self.height =height
        self.vel = 12
        self.skin =  pygame.image.load('../assets/laserGreen.png')
        self.game = game
        #for hit check
        self.rect = pygame.Rect(x, y, width, height)
    def draw(self):
        self.game.win.blit(self.skin , (self.x, self.y))
        self.y += self.w * 4
         #for hit check
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class protagonist(object):
    def __init__(self, x, y, width, height, game):
        # x y to spawn protagonist
        self.x = x
        self.y = y
        # height and width of protagonist
        self.width = width
        self.height = height
        #how much on x and y protagonist fly
        self.vel = 5
        #position for skin 1 def 2-left 3-right
        self.pos = 1
        #skins for protagonist
        self.flyLeft = pygame.image.load('../assets/playerLeft.png')
        self.flyRight = pygame.image.load('../assets/playerRight.png')
        self.flyCenter = pygame.image.load('../assets/player.png')
        self.flyDamaged = pygame.image.load('../assets/playerDamaged.png')
        # self health:
        self.health = 4   
        self.healthImage = pygame.image.load('../assets/life.png')
        #for checking if hit
        self.rect = pygame.Rect(x, y, width, height)
        
        self.game = game
    #draw protagonist
    def draw(self):
        for h in range(self.health):
            self.game.win.blit(self.healthImage , (self.game.width - 50, self.game.height - (h + 1) * 50))
        if self.pos == 1 and self.health > 2:
            self.game.win.blit(self.flyCenter , (self.x, self.y))
        elif self.health <= 2:#IDK chyba to wywale
            self.game.win.blit(self.flyDamaged , (self.x, self.y))
        elif self.pos == 2:
            self.game.win.blit(self.flyLeft , (self.x, self.y))
        elif self.pos == 3: 
            self.game.win.blit(self.flyRight  , (self.x, self.y))

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
       # self.hitbox= (self.x , self.y, self.width, self.height) # ta czerwona ramka
       # pygame.draw.rect(self.game.win, (255,0,0), self.hitbox, 2)


class enemy(object):
    def __init__(self, x, y, width, height, skin, game, can_shot, points):
        # x and y to spawn enemy
        self.x = x
        self.y = y
        self.width = width
        self.height =height
        self.vel = 2
        self.skin = skin
        self.health = 1
         #for hit check
        self.rect = pygame.Rect(x, y, width, height)
        self.game =game
        self.delayShoot = 0
        self.can_shot = can_shot
        self.points = points

    def draw(self):
        
        self.game.win.blit(self.skin , (self.x, self.y))
        #pygame.draw.rect(game.win, (255, 0 ,0), (self.x, self.y, 50, 50), 0)
        self.y += self.vel
        #self.hitbox= (self.x , self.y, self.width, self.height) # ta czerwona ramka
         #for hit check
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(self.game.win, (255,0,0), self.hitbox, 2)
    def hit(self):
        self.health -= 1
        if(self.health == 0):
            self.visible = False
        print('hit')


class boss(object):
    def __init__(self, x, y, width, height, skin, game):
        # x and y to spawn enemy
        self.x = x
        self.y = y
        self.width = width
        self.height =height
        self.vel = 2
        self.skin = skin
        self.health = 1
         #for hit check
        self.rect = pygame.Rect(x, y, width, height)
        self.game =game
        self.delayShoot = 0
        self.points = 100

    def draw(self):
        
        self.game.win.blit(self.skin , (self.x, self.y))
        #pygame.draw.rect(game.win, (255, 0 ,0), (self.x, self.y, 50, 50), 0)
        self.y += self.vel
        #self.hitbox= (self.x , self.y, self.width, self.height) # ta czerwona ramka
         #for hit check
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(self.game.win, (255,0,0), self.hitbox, 2)
    def hit(self):
        self.health -= 1
        if(self.health == 0):
            self.visible = False
        print('hit')