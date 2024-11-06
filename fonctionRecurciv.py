#coding: utf-8

def somNbrPaireImpaire(nombre) :
    somme = 0
    for i in range(0, nombre + 1, 2):
        if(i % 2 == 0):
              somme += i
        else:
            for i in range(1, nombre + 1, 2):
                somme += i
    return somme

nombre = int(input('entrez un nombre : '))
result = somNbrPaireImpaire(nombre)

if nombre % 2 == 0:
    print("La somme des nombres pairs jusqu'à", nombre, "est :", result)
else:
    print("La somme des nombres impairs jusqu'à", nombre, "est :", result)

def somme(a,b):
    """cette fonction calcule la somme de deux nombre et retoutrne le resultat
    paramettre
    a(int): premier nombre
    b(int): deuxieme nombre
    retourne
    int : la somme de a et b
    """ 
    return a + b
help(somme)