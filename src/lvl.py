import pygame
from characters import bullet
class level(object):
    def __init__(self, length,  ufo, ship, boss):
        self.length = length
        self.amount_of_ufos = ufo
        self.ufo_skin = pygame.image.load('../assets/enemyUFO.png')
        self.amoun_of_ships = ship
        self.ship_skin = pygame.image.load('../assets/enemyShip.png')
        self.boss = boss
        self.boss_skin = pygame.image.load('../assets/boss.png')
    def redraw(self, game, player, enemies, enemy_bullet, friendly_bullets, hit_effect):
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
                if b.y < 0:
                    friendly_bullets.pop(friendly_bullets.index(b))
                else:
                    b.draw()
                    #for hit check
                    for e in enemies:
                        if b.rect.colliderect(e.rect):
                            hit_effect.play()
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
                    hit_effect.play()
                    player.health -= 1
                    #player.hit()
     
    