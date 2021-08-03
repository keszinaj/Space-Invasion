f = open("./high_score.txt", "r")
list = []
for line in f:
	line = int(line)
	list.append(line)
print(list)