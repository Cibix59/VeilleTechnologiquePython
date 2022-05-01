import random


enJeu = true

file = open('mots.txt')
f = file.readlines()
i = random.randrange(0, len(f) - 1)

mot = f[i][:-1]

print(mot)

while enJeu:
    lettreChoisie = str(input())

    if lettreChoisie.lower() not in mot.lower():
        print("mauvaise lettre") 
    else:
        print("Bonne lettre")
