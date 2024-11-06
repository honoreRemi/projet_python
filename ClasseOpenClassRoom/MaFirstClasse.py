#coding utf-8

class Personne: #definition de notre classe personne
    """classe definissant une personne crarctérisée par 
    -son nom
    -son prenom
    -son age
    -son lieu de Residence"""

    def __init__(self): #notre methode constructeur par defaut
        self.nom = 'honore'
        self.prenom = ' remi'
        self.age = 27
        self.lieuResidence = 'yaounde'

    def __init__(self, nom_pers='honore', prenom_pers='remi', age_pers=27, lieu_residence_pers='yaounde'):
        self.nom = nom_pers
        self.prenom = prenom_pers
        self.age = age_pers
        self.lieuResid = lieu_residence_pers
    
    def __getattr__(self, noms): #les getattr permettent de definir une methode d'acces à nos attributs et à les modfiers.
        print('Alert! il n\'y a pas d\'attrribut {} ici ! '.format(noms))
        help(self.__getattr__)  # Affiche les informations de la méthode

reslt = Personne() #on a creer un objet result avec le constructeur par defaut
print(reslt.nom)

#creons a present un objet avec le constructeur parametrique
resul1 = Personne('honore remi', 'Manito', 27, 'yaounde')
print(resul1.lieuResid)
        

