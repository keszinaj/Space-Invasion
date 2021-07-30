import pygame
class protagonist(object):
    def __init__(self, x, y, width, height, game):
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

        self.game.win.blit(self.flyCenter , (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hitbox= (self.x , self.y, self.width, self.height) # ta czerwona ramka
        pygame.draw.rect(self.game.win, (255,0,0), self.hitbox, 2)


class enemy(object):
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

    def draw(self):
        
        self.game.win.blit(self.skin , (self.x, self.y))
        #pygame.draw.rect(game.win, (255, 0 ,0), (self.x, self.y, 50, 50), 0)
        self.y += self.vel
        self.hitbox= (self.x , self.y, self.width, self.height) # ta czerwona ramka
         #for hit check
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.game.win, (255,0,0), self.hitbox, 2)
    def hit(self):
        self.health -= 1
        if(self.health == 0):
            self.visible = False
        print('hit')