import random
def deployEnemies(n, rows, length):
        list_of_enemies = []
        p_y = 0

        first_y = length / rows  
        first_y_prev = first_y    
        for i in range(rows):
            p_x = 0
            firs_col = 600/n
            for j in range(n):
                p_x = random.randint(p_x, firs_col)
                p_y = random.randint(p_y, first_y )
                print(first_y)
                #print(" x = ", p_x)
                #print(" y = ",  p_y)
                #dobra to gówno ale zobaczmy jak działa
                firs_col += firs_col
                list_of_enemies.append(p_x)
                p_x += 10
            first_y  += first_y_prev
                
        return list_of_enemies

deployEnemies(5, 5, 300)