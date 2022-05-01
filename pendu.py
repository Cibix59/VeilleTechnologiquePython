
import random



file = open('mots.txt')
f = file.readlines()
i = random.randrange(0, len(f) - 1)



print(f[i][:-1])