#coding utf-8

class Personnel() :
    def __init__(self) -> None:
        self.nom = "honore "
        self.titre = "etudiant "
    def Travail(self):
        print('bien venu au travail')
    def __str__(self):
        return f"Enseignant - Nom: {self.nom}, Âge: {self.titre}"

class Enseignant(Personnel):
    def __init__(self) -> None:
        super().__init__()
        self.nom = 4
        self.age = 34
    def  travail(self):
        print("bien venu en entreprise")

    def __str__(self):
        return f"Enseignant - Nom: {self.nom}, Âge: {self.age}"

p = Personnel()
E = Enseignant()

print(p)