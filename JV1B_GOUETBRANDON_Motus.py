import random
import colorama
from colorama import Fore, Back , Style
listeMots = ["joyeux","sphynx","yakuza","bijoux","cyborg","webcam","psycho","nymphe","jaloux","puzzle"]

mot = listeMots[random.randrange(0,10)]

def victoire (mot,proposition):
    victoire = False
    if mot == proposition:
        victoire = True
    else:
        victoire = False
    return victoire

def verification (mot,proposition):
    resultat = ""
    for i in range(len(mot)):  
        if mot[i] == proposition[i]:
            lettre = Back.RED + proposition[i] + Back.RESET
            resultat += lettre
        else :
            for j in range(len(mot)):
                if mot[i] != proposition[j]:
                    lettre = Back.BLUE + proposition[i] + Back.RESET
                else:
                    lettre = Back.YELLOW + proposition[i] + Back.RESET
                    break
            resultat += lettre
    
    return resultat



print(mot)
for i in range(0,9):
    proposition = str(input("Veuillez entrez un mot : "))
    while len(proposition) < 6 or len(proposition) > 6 :
        proposition = str(input("Veuillez entrez un mot de six lettres ! : "))
    resultat = verification(mot,proposition)
    print(resultat)
    victory = victoire(mot,proposition)
    if victory == True:
        print("Vous avez gagné ! Bien joué !")
        break


if victory == False:
    print("Vous avez perdu !")