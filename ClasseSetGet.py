#coding utf-8

class Personne: #création de notre classe
    def __init__(self, nom, age): #definition de notre constructeur parametrique
        self.nom = nom
        self.age = age

    @property
    def nom(self):  #declaration de l'accesseur (getter)
        return self._nom
    
    @nom.setter
    def nom(self, nouveau_nom): #declaration du mutateur (setter) qui va nous permettre de modifier les objets crées
        self._nom = nouveau_nom

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, nouveau_age):
        if nouveau_age >= 0:
            self._age = nouveau_age
        else :
            raise ValueError('l\'age doit etre superieur à zéro.')
    
#utilisation des getters et setters
p1 = Personne("honore", 27)
print("votre nom est :{}" .format(p1.nom)) #utilisation ou appel du getter nom
p1.nom = 'remi' #modification de l'attribut nom bia le setter
print("votre nouveau nom est :{}" .format(p1.nom))

print("Vous avez :{} ans " .format(p1.age)) #acces à l'attribut age via le getter age
p1.age = 29 #modification de l'attribut via lme setter
print("Votre nouvel age est de  :{} ans " .format(p1.age))

class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    @property
    def nom(self):
        return self._nom 

    @nom.setter
    def nom(self, new_name):
        self._nom = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Votre âge n'est pas correct.")

class Chien(Animal):
    def __init__(self, nom, age, race):
        super().__init__(nom, age)
        self.race = race

class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)
        self.couleur = couleur

# Utilisation des getters et setters hérités
chien = Chien('bouboul', 15, 'bergé')
print('Votre chien se nomme : {}.' .format(chien.nom))
print('Et son âge est de : {} ans.' .format(chien.age))
print('Et sa race est : {}.' .format(chien.race))
chien.nom = 'rocky'
print('Le nouveau nom de votre chien est : {}' .format(chien.nom))
chien.age = 18
print('Et le nouvel âge de votre chien est : {}' .format(chien.age))

chat= Chat('minou', 10, 'noir')
print('Votre chat se nomme : {}.' .format(chat.nom))
print('Et son âge est de : {} ans.' .format(chat.age))
print('Et sa couleur est : {}.' .format(chat.couleur))
chat.nom = 'mimi'
print('Le nouveau nom de votre chat est : {}' .format(chat.nom))
chat.age = 5
print('Et le nouvel âge de votre chat est : {}' .format(chat.age))