import pygame
import random
from characters import  enemy
from lvl import level
# no ta funkcja to jest na 100% do poprawy ale na razie zostawie tak jak jest bo skupmy się na działaniu samej gry
def deployEnemies(game):
    if game.levels[game.current_level].boss == False:
        list_of_enemies = []
    

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