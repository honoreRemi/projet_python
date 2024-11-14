#coding utf-8

import itertools

# Nombre total d'éléments
n = 10
# Nombre d'éléments à choisir
r = 4

# Générer toutes les combinaisons
combinations = list(itertools.combinations(range(n), r))

# Afficher les combinaisons
for combo in combinations:
    print(combo)