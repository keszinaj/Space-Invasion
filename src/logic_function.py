import pygame
import random
from characters import  enemy, boss
from lvl import level
# no ta funkcja to jest na 100% do poprawy ale na razie zostawie tak jak jest bo skupmy się na działaniu samej gry
def deployEnemies(game):
    if game.levels[game.current_level].boss == False:
        list_of_enemies = []
        n = game.levels[game.current_level].length
        

        for e in range(game.levels[game.current_level].amount_of_ufos):
            y = -random.randint(0, game.levels[game.current_level].length)
            x = random.randint(46, game.width - 46)
            print(y)
            
            list_of_enemies.append(enemy(x, y, 92, 92, game.levels[game.current_level].ufo_skin, game, False, 10))
        for e in range(game.levels[game.current_level].amoun_of_ships):
            y = -random.randint(0, game.levels[game.current_level].length)
            x = random.randint(0, game.width)
            list_of_enemies.append(enemy(x, y, 92, 52, game.levels[game.current_level].ship_skin, game, True, 15))
            
                
        return list_of_enemies
    else:
        #class enemy(object):
    #def __init__(self, x, y, width, height, skin, game, can_shot, points):
        return boss( 400, 0, 200, 111, game.levels[game.current_level].boss_skin, game)