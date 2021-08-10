#main file of my game
import pygame
from settings import global_settings
from characters import protagonist, enemy, bullet
from logic_function import deployEnemies
from lvl import level
from button_cl import button
from screens import highscore_win, you_win, you_lose, info_win
import time

#here i save all most important varibles


                


        


pygame.init()
game = global_settings(1000, 900)
             

def game_main():
    shot_effect = pygame.mixer.Sound('../assets/laser1.wav')
    hit_effect = pygame.mixer.Sound('../assets/Explosion.wav')
     
    delayShoot = 0
    player = protagonist(game.width / 2 - 40, game.height - 200, 92, 75, game)
   
    

    while not game.finishGame:
        #check if game is finished and set varible to exit loops
        if game.current_level > game.max_level:
            game.finishGame = True
            game.finishLevel = True
            you_win()
            game.check_if_new_high_score(game.score)
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
                    #add credit to music Author: dklon
                    #pygame.mixer.music.load('../assets/laser1.wav')
                    #pygame.mixer.music.play()
                   # effect = pygame.mixer.Sound('../assets/laser1.wav')
                    shot_effect.play()
                    friendly_bullets.append(bullet(-1, player.x + 45, player.y - 37, 9, 33, game))
                    delayShoot = 22
                else:
                    delayShoot -=1
                
            else:
                pass
            game.levels[game.current_level].redraw(game, player, enemies, enemy_bullet, friendly_bullets, hit_effect)
            pygame.display.update()
            if player.health == 0:
                you_lose(game)
                game.finishLevel = True
                game.finishGame = True
                game.check_if_new_high_score(game.score)
                


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
            game.score = 0
        if highscore.draw_button():
            highscore_win(game)
            print('highscore.')
        if info.draw_button():
            info_win(game)
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