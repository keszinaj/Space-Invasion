#main file of my game
import pygame
from settings import global_settings
from characters import protagonist, enemy, bullet
from logic_function import deployEnemies
from lvl import level
from button_cl import button
from screens import highscore_win, you_win, you_lose, info_win
from game import game_main
import time

#here i save all most important varibles

pygame.init()
pygame.display.set_mode()    
game = global_settings(1000, 900)
           





def main_menu():
    logo = pygame.image.load('../assets/logo.png').convert_alpha()
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
            game_main(game)
            game.finishGame = False
            game.current_level = 1
            game.score = 0
            continue
        if highscore.draw_button():
            highscore_win(game)
            print('highscore.')
            continue
        if info.draw_button():
            info_win(game)
            print('Info win')
            continue
        if quit.draw_button():
            run = False
            print('Quit')
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False	

        
        pygame.display.update()


    pygame.quit()
        
main_menu()
#game_main()