#coding utf-8

class Humain :
    lieu_habitation = 'terre'
    def __init__(self, nom_pers, age_pers):#constructeur parametrique
        print('creation des humains ')
        self.nom = nom_pers
        self.age = age_pers

    def parler(self, message): #methode standard
        print('{} a dit : {}'.format(self.nom, message))

    def changer_planete(cls, nouvelle_planete): #methode classe
        Humain.lieu_habitation = nouvelle_planete
    changer_planete = classmethod(changer_planete)

    def definition(): #methode statique
        print('les humains sont les meilleures créatures de Dieu ...')
        
    definition = staticmethod(definition)

#programme pricipal

H1 = Humain('honore remi', 27)
H2 = Humain('super abel', 24)
H1.parler('bonjour tous les dev')
H1.changer_planete('CAMEROUN')


print(H1.nom)
print('la nouvelle planette est : ', H1.lieu_habitation)
print(H1.definition())


