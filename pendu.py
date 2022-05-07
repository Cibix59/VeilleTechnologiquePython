from pickle import TRUE
import random


enJeu = TRUE
motDevine = []
vie = 5

#genere la visualisation du mot actuel
def getMotActuel(mot, motDevine=[]):
    motActuelTMP = ''
    lettreTrouvees = motDevine
    for x in range(len(mot)):
        if mot[x] != ' ':
            motActuelTMP += '_ '
            for i in range(len(lettreTrouvees)):
                print("mo  : "+motDevine[i])
                if mot[x] == lettreTrouvees[i]:
                    motActuelTMP = motActuelTMP[:-2]
                    motActuelTMP += mot[x].upper() + ' '
        elif mot[x] == ' ':
            motActuelTMP += ' '
    return motActuelTMP


file = open('mots.txt')
f = file.readlines()
i = random.randrange(0, len(f) - 1)

mot = f[i][:-1]

print(mot)

while enJeu:
    lettreChoisie = str(input())

    motDevine.append(lettreChoisie)


    if lettreChoisie.lower() not in mot.lower():
        print("mauvaise lettre") 
        vie = vie -1
    else:
        print("Bonne lettre")
        motActuel = getMotActuel(mot, motDevine)
        print(motActuel)
        if motActuel.count('_') == 0:
            print("bien Joué !")
            quit()

    print("vie : "+ str(vie))
    if vie == 0:
        print("Game Over")
        quit()