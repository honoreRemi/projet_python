#coding utf-8

print('**********************************************************')
print('**BienVenue au combat de furry et Nganou *****************')
print('**Le combat se deroule en 04 raound **********************')
print('**********************************************************')

import random

def attaquer(joueur):
    if random.random() < 0.5:
        degats = random.randint(0, 100)
        return degats
    else:
        return 0

def afficher_etat(joueur1, joueur2):
    print(f"{joueur1['pseudo']} : {joueur1['points_de_vie']} points de vie")
    print(f"{joueur2['pseudo']} : {joueur2['points_de_vie']} points de vie")
    print()

# Demander les pseudos des joueurs
pseudo_joueur1 = input("Joueur 1, entrez votre pseudo : ")
pseudo_joueur2 = input("Joueur 2, entrez votre pseudo : ")

# Initialiser les joueurs
joueur1 = {"pseudo": pseudo_joueur1, "points_de_vie": 250}
joueur2 = {"pseudo": pseudo_joueur2, "points_de_vie": 250}

# Début du combat
print("Le combat commence !")

for _ in range(4):  # 4 attaques au total
    # Attaque du joueur 1
    print(f"{joueur1['pseudo']} attaque !")
    degats_joueur1 = attaquer(joueur1)
    if degats_joueur1 > 0:
        joueur2['points_de_vie'] -= degats_joueur1
        print(f"{joueur1['pseudo']} inflige {degats_joueur1} points de dégâts à {joueur2['pseudo']} !")
    else:
        print(f"L'attaque de {joueur1['pseudo']} a échoué.")

    # Vérifier si le joueur 2 est KO
    if joueur2['points_de_vie'] <= 0:
        print(f"{joueur2['pseudo']} est KO !")
        break

    # Attaque du joueur 2
    print(f"{joueur2['pseudo']} attaque !")
    degats_joueur2 = attaquer(joueur2)
    if degats_joueur2 > 0:
        joueur1['points_de_vie'] -= degats_joueur2
        print(f"{joueur2['pseudo']} inflige {degats_joueur2} points de dégâts à {joueur1['pseudo']} !")
    else:
        print(f"L'attaque de {joueur2['pseudo']} a échoué.")

    # Vérifier si le joueur 1 est KO
    if joueur1['points_de_vie'] <= 0:
        print(f"{joueur1['pseudo']} est KO !")
        break

    # Afficher l'état des joueurs après chaque tour
    afficher_etat(joueur1, joueur2)

# Déterminer le gagnant
if joueur1['points_de_vie'] > joueur2['points_de_vie']:
    print(f"{joueur1['pseudo']} remporte la victoire !")
elif joueur2['points_de_vie'] > joueur1['points_de_vie']:
    print(f"{joueur2['pseudo']} remporte la victoire !")
else:
    print("Match nul !")