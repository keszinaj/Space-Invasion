import pygame
import random
from characters import bullet
class level(object):
    def __init__(self, length,  ufo, ship, boss):
        self.length = length
        self.amount_of_ufos = ufo
        self.ufo_skin = pygame.image.load('../assets/enemyUFO.png').convert_alpha()
        self.amoun_of_ships = ship
        self.ship_skin = pygame.image.load('../assets/enemyShip.png').convert_alpha()
        self.boss = boss
        self.boss_skin = pygame.image.load('../assets/boss.png').convert_alpha()
        self.green_hit   = pygame.image.load('../assets/laserGreenShot.png').convert_alpha()
        self.red_hit= pygame.image.load('../assets/laserRedShot.png').convert_alpha()
        self.boss_bum = pygame.image.load('../assets/boss_died.png').convert_alpha()
    def redraw(self, game, player, enemies, enemy_bullet, friendly_bullets, hit_effect):
        if self.boss:
            game.draw()
            player.draw()
            game.draw_score()

            if enemies.health == 0:
                game.win.blit(self.boss_bum, (enemies.x, enemies.y))
                game.current_level += 1
                game.finishLevel = True
            elif enemies.rect.colliderect(player.rect):
                player.health -= 1
                enemies.y = 0
                enemies.x = game.width/2
                player.y += 3
                #fix bug
                enemies.rect = pygame.Rect(0,game.width/2, enemies.width, enemies.height)
                game.score -= 10
            elif enemies.y > game.height:
                game.current_level += 1
                game.finishLevel = True
                
            else:
                enemies.draw()
            
            if enemies.delayShoot == 0:
                enemy_bullet.append(bullet(1, enemies.x + 148, enemies.y + 100, 9, 33, game))
                enemy_bullet.append(bullet(1, enemies.x + 45, enemies.y + 100, 9, 33, game))
                enemies.delayShoot = 100
            else:
                enemies.delayShoot -= 1

            if len(friendly_bullets) != 0:
                imax  = len(friendly_bullets)
                i = 0
                while i < imax:
                    if friendly_bullets[i].y < 0:
                        friendly_bullets.pop(i)
                        imax -= 1
                    else:
                        friendly_bullets[i].draw()
                        #for hit check
                        if friendly_bullets[i].rect.colliderect(enemies.rect):
                            hit_effect.play()
                            game.win.blit(self.green_hit, (friendly_bullets[i].x - 24, friendly_bullets[i].y - 3))
                            friendly_bullets.pop(i)
                            imax -= 1
                            print("aaaa")
                            enemies.hit()
                        else:
                            i += 1
            if len(enemy_bullet) != 0:
                imax  = len(enemy_bullet)
                i = 0
                while i < imax:
                    b = enemy_bullet[i]
                    b.draw()
                    #for hit check
                    if b.y > game.height:
                        enemy_bullet.pop(i)
                        imax -= 1
                    elif b.rect.colliderect(player.rect):
                        enemy_bullet.pop(i)
                        print("aaaa")
                        hit_effect.play()
                        player.health -= 1
                        imax -= 1
                    else:
                        i += 1
            
        else:
            game.draw()
            player.draw()
            game.draw_score()
            amount_of_enemies = len(enemies)
            i = 0
            
            #while loop fix the problem with flash
            while i < amount_of_enemies:
                e = enemies[i]
                if e.health == 0:
                    enemies.pop(enemies.index(e))
                    amount_of_enemies -= 1
                    game.score += e.points
                    print(game.score)
                elif e.rect.colliderect(player.rect):
                    game.win.blit(self.red_hit, (e.x + e.width // 4 , e.y + e.height // 4))
                    enemies.pop(enemies.index(e))
                    player.health -= 1
                    game.score -= 10
                    amount_of_enemies -= 1
                elif e.y > game.height:
                    enemies.pop(enemies.index(e))
                    amount_of_enemies -= 1
                else:
                    i += 1
                    e.draw()
                if e.y > 0 and e.can_shot:
                    if e.delayShoot == 0:
                        print("a")
                        enemy_bullet.append(bullet(1, e.x + 45, e.y + 36, 9, 33, game))
                        e.delayShoot = 100
                    else:
                        e.delayShoot -= 1
                
            if len(friendly_bullets) != 0:
                i = 0
                imax = len(friendly_bullets)
                while i < imax:
                    b = friendly_bullets[i]
                    if b.y < 0:
                        friendly_bullets.pop(i)
                        imax -= 1
                    else:
                        b.draw()
                        #for hit check
                        for e in enemies:
                            if b.rect.colliderect(e.rect):
                                game.win.blit(self.green_hit, (b.x - 24, b.y - 3))
                                hit_effect.play()                                                  
                                friendly_bullets.pop(i)
                                imax -= 1
                                i-=1
                                e.hit()
                                break
                        i += 1
                                
            if len(enemy_bullet) != 0:
                i = 0
                imax = len(enemy_bullet)
                while i < imax:
                    b = enemy_bullet[i]
                    b.draw()
                    #for hit check
                    if b.rect.colliderect(player.rect):
                        game.win.blit(self.red_hit, (b.x - 24, b.y - 3))
                        enemy_bullet.pop(i)
                        hit_effect.play()
                        imax -= 1
                        player.health -= 1
                    else:
                        i += 1
                        
            if len(enemies) == 0:
                game.current_level += 1
                game.finishLevel = True
     
    