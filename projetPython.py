# Projet : Calculatrice avancée en ligne de commande

#coding utf-8

import math

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro"

def puissance(a, b):
    return a ** b

def racine_carree(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Erreur : Impossible de calculer la racine carrée d'un nombre négatif"

def logarithme(a):
    if a > 0:
        return math.log10(a)
    else:
        return "Erreur : Impossible de calculer le logarithme d'un nombre nul ou négatif"

def calculatrice():
    print("=== Calculatrice ===")
    while True:
        print("Opérations disponibles :")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Puissance")
        print("6. Racine carrée")
        print("7. Logarithme")
        print("0. Quitter")

        choix = input("Choisissez une opération : ")

        if choix == "0":
            print("Au revoir !")
            break

        if choix in ["1", "2", "3", "4", "5", "6", "7"]:
            if choix == "1":
                a = float(input("Entrez le premier nombre : "))
                b = float(input("Entrez le deuxième nombre : "))
                resultat = addition(a, b)
                print("Résultat :", resultat)
            elif choix == "2":
                a = float(input("Entrez le premier nombre : "))
                b = float(input("Entrez le deuxième nombre : "))
                resultat = soustraction(a, b)
                print("Résultat :", resultat)
            elif choix == "3":
                a = float(input("Entrez le premier nombre : "))
                b = float(input("Entrez le deuxième nombre : "))
                resultat = multiplication(a, b)
                print("Résultat :", resultat)
            elif choix == "4":
                a = float(input("Entrez le premier nombre : "))
                b = float(input("Entrez le deuxième nombre : "))
                resultat = division(a, b)
                print("Résultat :", resultat)
            elif choix == "5":
                a = float(input("Entrez le nombre : "))
                b = float(input("Entrez l'exposant : "))
                resultat = puissance(a, b)
                print("Résultat :", resultat)
            elif choix == "6":
                a = float(input("Entrez le nombre : "))
                resultat = racine_carree(a)
                print("Résultat :", resultat)
            elif choix == "7":
                a = float(input("Entrez le nombre : "))
                resultat = logarithme(a)
                print("Résultat :", resultat)
        else:
            print("Erreur : Choix invalide")

# Point d'entrée du programme
if __name__ == "__main__":
    calculatrice()