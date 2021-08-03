#main file of my game
import pygame
from settings import global_settings
from characters import protagonist, enemy
from logic_function import deployEnemies
from lvl import level
from button_cl import button
import time

#here i save all most important varibles


                


class bullet(object):
    def __init__(self, w,  x, y, width, height):
        self.w = w
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
        self.y += self.w * 4
         #for hit check
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        


pygame.init()
game = global_settings(1000, 900)
def highscore_win():
    game.draw()
    n = 1
    print(game.highscore)
    for h in game.highscore:
        print(h)
        text = str(n) + ":  " + str(h)
        n += 1
        text_img = game.font_2.render(text, False, (255, 255, 255))
        text_len = text_img.get_width()
        text_len = text_img.get_width()
        game.win.blit(text_img, (game.width / 2 - (text_len/2), n * 100 - 50))

    text_3 = "Click escape to leave"
    text3_img = game.font.render(text_3, False, (255, 255, 255))
    text3_len = text3_img.get_width()
    game.win.blit(text3_img, (game.width / 2 - (text3_len/2), 800))
    pygame.display.update()
    check = True
    while check:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                check = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


def you_win():
    #game.draw()
    text_1 = "You Win!"
    text_2 = "Score: " + str(game.score)
    text_3 = "Click escape to leave"
    text1_img = game.font_2.render(text_1, False, (255, 255, 255))
    text2_img = game.font_2.render(text_2, False, (255, 255, 255))
    text3_img = game.font.render(text_3, False, (255, 255, 255))
    text1_len = text1_img.get_width()
    game.win.blit(text1_img, (game.width / 2 - (text1_len/2), 200))
    text2_len = text2_img.get_width()
    game.win.blit(text2_img, (game.width / 2 - (text2_len/2), 300))
    text3_len = text3_img.get_width()
    game.win.blit(text3_img, (game.width / 2 - (text3_len/2), 800))
    pygame.display.update()
    check = True
    while check:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                check = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    


def info_win():
    game.draw()
    text_1 = "Space Invasion is a simple shooter game."
    text_2 = "Player must destroy as much enemie's ship as he can." 
    text_3 = "Tap escape to leave"
    text1_img = game.font.render(text_1, False, (255, 255, 255))
    text2_img = game.font.render(text_2, False, (255, 255, 255))
    text3_img = game.font.render(text_3, False, (255, 255, 255))
    game.win.blit(text1_img, (10, 150))
    game.win.blit(text2_img, (10, 200))
    game.win.blit(text3_img, (10, 800))
    pygame.display.update()
    check = True
    while check:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                check = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    

def game_main():
    def redraw():
        game.draw()
        player.draw()
        game.draw_score()
        for e in enemies:
            if e.health == 0:
                enemies.pop(enemies.index(e))
                game.score += e.points
                print(game.score)
            elif e.rect.colliderect(player.rect):
                enemies.pop(enemies.index(e))
                player.health -= 1
                game.score -= 10
            elif e.y > game.height:
                enemies.pop(enemies.index(e))
            else:
                e.draw()
            if e.y > 0 and e.can_shot:
                if e.delayShoot == 0:
                    enemy_bullet.append(bullet(1, e.x + 45, e.y + 36, 9, 33))
                    e.delayShoot = 100
                else:
                    e.delayShoot -= 1
        if len(friendly_bullets) != 0:
            for b in friendly_bullets:
                b.draw()
                 #for hit check
                for e in enemies:
                    if b.rect.colliderect(e.rect):
                        friendly_bullets.pop(friendly_bullets.index(b))
                        print("aaaa")
                        e.hit()
        if len(enemy_bullet) != 0:
            for b in enemy_bullet:
                b.draw()
                 #for hit check
                if b.rect.colliderect(player.rect):
                    enemy_bullet.pop(enemy_bullet.index(b))
                    print("aaaa")
                    player.health -= 1
                    #player.hit()
     
    delayShoot = 0
    player = protagonist(game.height - 20, game.width / 2 - 40, 92, 75, game)
   
    

    while not game.finishGame:
        #check if game is finished and set varible to exit loops
        if game.current_level > game.max_level:
            game.finishGame = True
            game.finishLevel = True
            you_win()
        else:
            game.finishLevel = False
            enemies = deployEnemies(game)
            friendly_bullets = []
            enemy_bullet = []
            game.draw()
            player.draw()
            text_level = "Level    " + str(game.current_level)
            text_img = game.font_2.render(text_level, True, (255, 255, 255))
            text_len = text_img.get_width()
            game.win.blit(text_img, (game.width / 2 - (text_len/2), 200))
            pygame.display.update()
            time.sleep(2)
            


        while not game.finishLevel:
            game.clock.tick(60)#fps
            #handle delay shoot
            if delayShoot != 0:
                delayShoot -= 1
            #handle quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.finishGame = True
                    game.finishLevel = True
                   
            #handle keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x>0:
                player.x -= player.vel
                player.pos = 2
            elif keys[pygame.K_RIGHT] and game.width > player.x +player.width:
                player.x += player.vel
                player.pos = 3
            else: 
                player.pos = 1 # chyba trzeba to zmienić
            if keys[pygame.K_UP] and player.y>0:
                player.y -= player.vel
            elif keys[pygame.K_DOWN]and game.height > player.y+player.height:
                player.y += player.vel
            if keys[pygame.K_SPACE]:
                if delayShoot == 0:
                    friendly_bullets.append(bullet(-1, player.x + 45, player.y - 37, 9, 33))
                    delayShoot = 22
                else:
                    delayShoot -=1
                
            else:
                pass
            redraw()
            pygame.display.update()
            if len(enemies) == 0:
                game.current_level += 1
                game.finishLevel = True
            if player.health == 0:
                game.finishLevel = True
                game.finishGame = True
                


#counter = 0




def main_menu():
    logo = pygame.image.load('../assets/logo.png')
    play = button(410, 450, 'Play', game)
    highscore = button(410, 550, 'High Score', game)
    info = button(410, 650, 'Info', game)
    quit = button(410, 750, 'Quit', game)
    game.read_highscore()   


    run = True
    while run:

        game.draw()
        game.win.blit(logo , (50, 10))
        if play.draw_button():
            game_main()
            game.finishGame = False
            game.current_level = 1
        if highscore.draw_button():
            highscore_win()
            print('highscore.')
        if info.draw_button():
            info_win()
            print('Info win')
        if quit.draw_button():
            run = False
            print('Quit')
        
        

        #counter_img = font.render(str(counter), True, red)
        #screen.blit(counter_img, (280, 450))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False	

        
        pygame.display.update()


    pygame.quit()
        
main_menu()
#game_main()