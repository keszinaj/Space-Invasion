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
        # myfont = pygame.font.SysFont('Raleway', 72, bold=True, italic=False)
        self.font = pygame.font.SysFont('Constantia', 30, bold=True, italic=False)
        self.font_2 = pygame.font.SysFont('Constantia', 90, bold=True, italic=False)
        
        #load background
        self.backg = pygame.image.load("../assets/backg.jpeg")
        self.win.blit(self.backg, (0,0)) #hmm should i delete it?
        self.run = True #hmmm
        # level logic
        self.score = 0
        self.highscore = []
        self.max_level = 6
        self.current_level = 1
        self.levels = {
            1 : level(100, 20, 10, False),
            2 : level(180, 3, 0, False),
            3 : level(150, 2, 5, False),
            4 : level(150, 1, 1, False),
            5 : level(140, 1, 0, False),
            6 : level(1400, 15, 15, True),      
        }
        #1 : level(1000, 20, 0, False),
        #    2 : level(1800, 30, 0, False),
          #  3 : level(1500, 20, 5, False),
           # 4 : level(1500, 20, 19, False),
           # 5 : level(1400, 30, 29, False),
           # 6 : level(1400, 15, 15, True),  
        self.finishLevel = False
        self.finishGame = False
    # to redraw the windows
    def draw(self):
        self.win.blit(self.backg, (0,0))
    def draw_score(self):
        text_score = "Score: " + str(self.score)
        score_img = self.font.render(text_score , True, (255, 255, 255))
        self.win.blit(score_img, (20, 10))
    def read_highscore(self):
        f = open("./high_score.txt", "r")
        list = []
        for line in f:
            line = int(line)
            list.append(line)
        f.close()
        self.highscore = list
    def check_if_new_high_score(self, score):
        yes = False
        for s in self.highscore:
            if s < score:
                self.highscore.insert(self.highscore.index(s), score)
                self.highscore.pop()
                yes = True
                break
        if yes:
            f = open("./high_score.txt", "w")
            for l in self.highscore:
                straa = str(l) + "\n" 
                f.write(straa)
            f.close()
        return yes
                    



#tests:
#a = global_settings(200, 200)
#print( a.levels[1].amoun_of_ships)
