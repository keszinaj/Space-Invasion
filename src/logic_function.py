import pygame
import random
from characters import  enemy, boss
from lvl import level
# no ta funkcja to jest na 100% do poprawy ale na razie zostawie tak jak jest bo skupmy się na działaniu samej gry
def deployEnemies(game):
    if game.levels[game.current_level].boss == False:
        list_of_enemies = []
        len = game.levels[game.current_level].length
        plus_space = len // game.levels[game.current_level].amount_of_ufos
        end = plus_space
        start = 0
        

        for e in range(game.levels[game.current_level].amount_of_ufos):
            y = -random.randint(start, end)
            x = random.randint(46, game.width - 46)
            print(y)
            start = end
            end += len
            list_of_enemies.append(enemy(x, y, 91, 91, game.levels[game.current_level].ufo_skin, game, False, 10))
        if game.levels[game.current_level].amoun_of_ships != 0:
            plus_space = len // game.levels[game.current_level].amoun_of_ships
        end = plus_space
        start = 0
        for e in range(game.levels[game.current_level].amoun_of_ships):
            y = -random.randint(start, end)
            x = random.randint(0, game.width)
            start = end
            end += len
            list_of_enemies.append(enemy(x, y, 92, 52, game.levels[game.current_level].ship_skin, game, True, 15))
            
                
        return list_of_enemies
    else:
        #class enemy(object):
    #def __init__(self, x, y, width, height, skin, game, can_shot, points):
        return boss( 400, 0, 200, 111, game.levels[game.current_level].boss_skin, game)