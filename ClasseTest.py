#coding utf-8

class voiture(object):
    def __init__(self):
        self._roues = 4

    @property
    def roues(self):
        print('Récupérer le nombre de roues')
        return self._roues

    @roues.setter
    def roues(self, a):
        print('Changement de roues')
        self._roues = a

v = voiture()  

print(v.roues)  
v.roues = 6  

print(v.roues)  