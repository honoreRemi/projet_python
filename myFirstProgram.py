#coding:utf-8
n = 12.0/3.0
print(n)

def somme(a,b) :
    s = a + b
    return s
print('votre resultat est :', somme(1,2))

def est_parfait(nombre):
    somme_diviseurs = 0
    for diviseur in range(1, nombre):
        if nombre % diviseur == 0:
            somme_diviseurs += diviseur
    return somme_diviseurs == nombre
borne_iniferieur = 1
borne_superieur = 1000
nombre_parfait = []
for nombre in range(borne_iniferieur, borne_superieur +1 ):
    if est_parfait(nombre) :
        nombre_parfait.append(nombre)

print('le nombre parfait entre {} et {} est {} :' .format(borne_iniferieur, borne_superieur, nombre_parfait))


import math
 
result = math.sqrt(100)
print ('la racine carrée de est :', result)

from math import sqrt 
result = math.sqrt(100)
print ('la racine carrée de est :', result)

from math import *

result = sqrt(100)
print ('la racine carrée de est :', result)