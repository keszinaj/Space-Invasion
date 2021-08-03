
f = open("./high_score.txt", "w")
list = [1, 2, 3, 4, 5]
for l in list:
    straa = str(l) + "\n" 
    f.write(straa)
f.close()
