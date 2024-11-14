#coding utf-8

import itertools

# Nombre total d'éléments
n = 10

# Demander à l'utilisateur combien d'éléments il souhaite combiner
r = int(input("Combien d'éléments voulez-vous combiner (max 10) ? "))

if r > n or r < 1:
    print("Veuillez entrer un nombre valide entre 1 et 10.")
else:
    # Générer toutes les combinaisons
    combinations = list(itertools.combinations(range(n), r))

    # Afficher les combinaisons
    print(f"Toutes les combinaisons de {r} éléments parmi {n} :")
    for combo in combinations:
        print(combo)