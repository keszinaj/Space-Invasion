import pygame
from settings import global_settings
from characters import protagonist, enemy, bullet
from logic_function import deployEnemies
from lvl import level
from screens import highscore_win, you_win, you_lose, info_win
import time



def game_main(game):
    shot_effect = pygame.mixer.Sound('../assets/laser1.wav')
    hit_effect = pygame.mixer.Sound('../assets/Explosion.wav')
     
    delayShoot = 0
    player = protagonist(game.width / 2 - 40, game.height - 200, 92, 75, game)
   
    

    while not game.finishGame:
        #check if game is finished and set varible to exit loops
        if game.current_level > game.max_level:
            game.finishGame = True
            game.finishLevel = True
            you_win(game)
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
                player.pos = 1 
            if keys[pygame.K_UP] and player.y>0:
                player.y -= player.vel
            elif keys[pygame.K_DOWN]and game.height > player.y+player.height:
                player.y += player.vel
            if keys[pygame.K_SPACE]:
                if delayShoot == 0:
                    shot_effect.play()
                    friendly_bullets.append(bullet(-1, player.x + 45, player.y - 37, 9, 33, game))
                    delayShoot = 15
                else:
                    delayShoot -=1
                
            else:
                pass
            game.levels[game.current_level].redraw(game, player, enemies, enemy_bullet, friendly_bullets, hit_effect)
            pygame.display.update()
            if player.health == 0:
                you_lose(game, player)
                game.finishLevel = True
                game.finishGame = True
                game.check_if_new_high_score(game.score)
                