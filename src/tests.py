def main():
        def redraw():
        game.draw()
        player.draw()
        for e in enemies:
            if e.health == 0:
                enemies.pop(enemies.index(e))
            elif e.rect.colliderect(player.rect):
                enemies.pop(enemies.index(e))
                player.health -= 1
            else:
              e.draw()
        if len(friendly_bullets) != 0:
            for b in friendly_bullets:
                b.draw()
                 #for hit check
                for e in enemies:
                    if b.rect.colliderect(e.rect):
                        friendly_bullets.pop(friendly_bullets.index(b))
                        print("aaaa")
                        e.hit()
    delayShoot = 0
    player = protagonist(0, 0, 92, 75, game)
    while not game.finishGame:
        enemies = deployEnemies(game)
        friendly_bullets = []
        enemy_bullet = []
        player.draw()
        for e in enemies:
            e.draw()
        while not game.finishLevel:
            game.clock.tick(60)#fps
            #handle delay shoot
            if delayShoot != 0:
                delayShoot -= 1
            #handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False
        #handle keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x>0:
            player.x -= player.vel
        elif keys[pygame.K_RIGHT] and game.width > player.x +player.width:
            player.x += player.vel
        if keys[pygame.K_UP] and player.y>0:
            player.y -= player.vel
        elif keys[pygame.K_DOWN]and game.height > player.y+player.height:
            player.y += player.vel
        if keys[pygame.K_SPACE]:
            if delayShoot == 0:
                friendly_bullets.append(bullet(player.x + 45, player.y - 37, 9, 33))
                delayShoot = 22
            else:
                delayShoot -=1
            
        else:
            pass
            redraw()
            pygame.display.update()

main()