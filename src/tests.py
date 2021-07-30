def main():
    while not game.finishGame:
        enemies = deployEnemies(game)
        friendly_bullets = []
        enemy_bullet = []
        while not game.finishLevel:
