#coding utf-8

import random

def choisir_mot():
    mots = ["python", "programmation", "ordinateur", "jeu", "pendu", "algorithme"]
    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache

def demander_lettre():
    while True:
        lettre = input("Entrez une lettre : ")
        if len(lettre) == 1 and lettre.isalpha():
            return lettre.lower()
        else:
            print("Erreur : Veuillez entrer une seule lettre.")

def jouer_pendu():
    print("=== Le jeu du pendu ===")
    mot_a_deviner = choisir_mot()
    lettres_trouvees = []
    tentatives_restantes = 7

    while True:
        mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
        print("Mot à deviner :", mot_cache)
        print("Tentatives restantes :", tentatives_restantes)

        lettre = demander_lettre()

        if lettre in lettres_trouvees:
            print("Vous avez déjà trouvé cette lettre.")
        elif lettre in mot_a_deviner:
            lettres_trouvees.append(lettre)
            if mot_cache == mot_a_deviner:
                print("Félicitations ! Vous avez trouvé le mot :", mot_a_deviner)
                break
        else:
            tentatives_restantes -= 1
            print("La lettre", lettre, "n'est pas dans le mot.")

        if tentatives_restantes == 0:
            print("Vous avez perdu ! Le mot à deviner était :", mot_a_deviner)
            break

    print("Merci d'avoir joué !")

# Point d'entrée du programme
if __name__ == "__main__":
    jouer_pendu()