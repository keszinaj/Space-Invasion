import pygame

def highscore_win(game):
    game.draw()
    n = 1
    print(game.highscore)
    for h in game.highscore:
        print(h)
        text = str(n) + ":  " + str(h)
        n += 1
        text_img = game.font_2.render(text, False, (255, 255, 255))
        text_len = text_img.get_width()
        text_len = text_img.get_width()
        game.win.blit(text_img, (game.width / 2 - (text_len/2), n * 100 - 50))

    text_3 = "Click escape to leave"
    text3_img = game.font.render(text_3, False, (255, 255, 255))
    text3_len = text3_img.get_width()
    game.win.blit(text3_img, (game.width / 2 - (text3_len/2), 800))
    pygame.display.update()
    check = True
    while check:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                check = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

def you_win(game):
    #game.draw()
    text_1 = "You Win!"
    text_2 = "Score: " + str(game.score)
    text_3 = "Click escape to leave"
    new_highscore = game.check_if_new_high_score(game.score)
    text1_img = game.font_2.render(text_1, False, (255, 255, 255))
    text2_img = game.font_2.render(text_2, False, (255, 255, 255))
    text3_img = game.font.render(text_3, False, (255, 255, 255))
    text1_len = text1_img.get_width()
    game.win.blit(text1_img, (game.width / 2 - (text1_len/2), 200))
    text2_len = text2_img.get_width()
    game.win.blit(text2_img, (game.width / 2 - (text2_len/2), 300))
    text3_len = text3_img.get_width()
    game.win.blit(text3_img, (game.width / 2 - (text3_len/2), 800))
    if new_highscore:
        text_4 = "Good Score!!!"
        text4_img = game.font_2.render(text_4, False, (255, 255, 255))
        text4_len = text4_img.get_width()
        game.win.blit(text4_img, (game.width / 2 - (text4_len/2), 400))
    pygame.display.update()
    check = True
    while check:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                check = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
def you_lose(game):
    #game.draw()
    text_1 = "You Lose!"
    text_2 = "Score: " + str(game.score)
    text_3 = "Click escape to leave"
    text1_img = game.font_2.render(text_1, False, (255, 255, 255))
    text2_img = game.font_2.render(text_2, False, (255, 255, 255))
    text3_img = game.font.render(text_3, False, (255, 255, 255))
    text1_len = text1_img.get_width()
    game.win.blit(text1_img, (game.width / 2 - (text1_len/2), 200))
    text2_len = text2_img.get_width()
    game.win.blit(text2_img, (game.width / 2 - (text2_len/2), 300))
    text3_len = text3_img.get_width()
    game.win.blit(text3_img, (game.width / 2 - (text3_len/2), 800))
    pygame.display.update()
    check = True
    while check:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                check = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    

def info_win(game):
    game.draw()
    text_1 = "Space Invasion is a simple shooter game."
    text_2 = "Player must destroy as much enemie's ship as he can." 
    text_3 = "Tap escape to leave"
    text1_img = game.font.render(text_1, False, (255, 255, 255))
    text2_img = game.font.render(text_2, False, (255, 255, 255))
    text3_img = game.font.render(text_3, False, (255, 255, 255))
    game.win.blit(text1_img, (10, 150))
    game.win.blit(text2_img, (10, 200))
    game.win.blit(text3_img, (10, 800))
    pygame.display.update()
    check = True
    while check:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                check = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    

