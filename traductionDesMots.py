from difflib import get_close_matches

def traduire_mot(mot, dictionnaire):
    mot = mot.lower()
    if mot in dictionnaire:
        return dictionnaire[mot]
    elif mot.title() in dictionnaire:
        return dictionnaire[mot.title()]
    elif mot.upper() in dictionnaire:
        return dictionnaire[mot.upper()]
    else:
        mots_similaires = get_close_matches(mot, dictionnaire.keys(), n=3, cutoff=0.8)
        if mots_similaires:
            choix = input("Le mot '{}' n'existe pas dans le dictionnaire. Voulez-vous dire l'un de ces mots ? [O/N] : {}\n".format(mot, mots_similaires))
            if choix.upper() == "O":
                mot_similaire = mots_similaires[0]
                return dictionnaire[mot_similaire]
        return "Le mot '{}' n'existe pas dans le dictionnaire.".format(mot)

def main():
    dictionnaire = {
        "chien": "dog",
    "chat": "cat",
    "maison": "house",
    "arbre": "tree",
    "soleil": "sun",
    "oiseau": "bird",
    "voiture": "car",
    "jardin": "garden",
    "ordinateur": "computer",
    "livre": "book",
    "musique": "music",
    "pomme": "apple",
    "banane": "banana",
    "orange": "orange",
    "citron": "lemon",
    "fleur": "flower",
    "étoile": "star",
    "pluie": "rain",
    "neige": "snow",
    "ciel": "sky",
    "mer": "sea",
    "montagne": "mountain",
    "route": "road",
    "train": "train",
    "avion": "airplane",
    "vélo": "bicycle",
    "piscine": "pool",
    "école": "school",
    "travail": "work",
    "argent": "money",
    "temps": "time",
    "amour": "love",
    "ami": "friend",
    "famille": "family",
    "santé": "health",
    "bonheur": "happiness",
    "cadeau": "gift",
    "vacances": "vacation",
    "restaurant": "restaurant",
    "film": "movie",
    "théâtre": "theatre",
    "musée": "museum",
    "art": "art",
    "photographie": "photography",
    "danse": "dance",
    "chanson": "song",
    "jeu": "game",
    "sport": "sport",
    "football": "football",
    "basketball": "basketball",
    "tennis": "tennis",
    "natation": "swimming",
    "course": "running",
    "voyage": "travel",
    "explorer": "explore",
    "découvrir": "discover",
    "nourriture": "food",
    "boisson": "drink",
    "café": "coffee",
    "thé": "tea",
    "pain": "bread",
    "fromage": "cheese",
    "viande": "meat",
    "poisson": "fish",
    "légumes": "vegetables",
    "fruits": "fruits",
    "sucre": "sugar",
    "sel": "salt",
    "poivre": "pepper",
    "huile": "oil",
    "herbes": "herbs",
    "épices": "spices",
    "cuisine": "kitchen",
    "recette": "recipe",
    "restaurant": "restaurant",
    "réservation": "reservation",
    "entrée": "appetizer",
    "plat principal": "main course",
    "dessert": "dessert",
    "boisson": "beverage",
    "eau": "water",
    "jus": "juice",
    "bière": "beer",
    "vin": "wine",
    "cocktail": "cocktail",
    "santé": "cheers",
    "bon appétit": "enjoy your meal",
    "s'il vous plaît": "please",
    "merci": "thank you",
    "excusez-moi": "excuse me",
    "pardon": "sorry",
    "aéroport": "airport",
    "hôtel": "hotel",
    "station": "station",
    "métro": "subway",
    "taxi": "taxi",
    "bus": "bus",
    "train": "train",
    "voiture": "car",
    "vélo": "bicycle",
    "moto": "motorcycle",
    "bateau": "boat",
    "avion": "airplane",
    "arrivée": "arrival",
    "départ": "departure",
    "horaires": "schedule",
    "bagages": "luggage",
    "passeport": "passport",
    "visa": "visa",
    "carte d'embarquement": "boarding pass",
    "chambre": "room",
    "clé": "key",
    "lit": "bed",
    "salle de bain": "bathroom",
     "aujourd'hui": "today",
    "demain": "tomorrow",
    "lundi": "Monday",
    "mardi": "Tuesday",
    "mercredi": "Wednesday",
    "jeudi": "Thursday",
    "vendredi": "Friday",
    "samedi": "Saturday",
    "dimanche": "Sunday",
    "janvier": "January",
    "février": "February",
    "mars": "March",
    "avril": "April",
    "mai": "May",
    "juin": "June",
    "juillet": "July",
    "août": "August",
    "septembre": "September",
    "octobre": "October",
    "novembre": "November",
    "décembre": "December",
    "printemps": "spring",
    "été": "summer",
    "automne": "autumn",
    "hiver": "winter",
    "fête": "party",
    "anniversaire": "birthday",
    "mariage": "wedding",
    "cérémonie": "ceremony",
    "cadeau": "gift",
    "invitation": "invitation",
    "décoration": "decoration",
    "gâteau": "cake",
    "bougie": "candle",
    "serviette": "towel",
    "savon": "soap",
    "shampoing": "shampoo",
    "peigne": "comb",
    "brosse à dents": "toothbrush",
    "dentifrice": "toothpaste",
    "miroir": "mirror",
    "télévision": "television",
    "téléphone": "phone",
    "ordinateur": "computer",
    "internet": "internet",
    "wifi": "wifi",
    "chargeur": "charger",
    "batterie": "battery",
    "écouteurs": "headphones",
    "appareil photo": "camera",
    "journal": "newspaper",
    "magazine": "magazine",
    "livre": "book",
    "stylo": "pen",
    "crayon": "pencil",
    "feutre": "marker",
    "gomme": "eraser",
    "cahier": "notebook",
    "papier": "paper",
    "carte": "card",
    "enveloppe": "envelope",
    "timbre": "stamp",
    "argent": "money",
    "pièce de monnaie": "coin",
    "billet": "bill",
    "porte-monnaie": "wallet",
    "carte de crédit": "credit card",
    "compte bancaire": "bank account",
    "reçu": "receipt",
    "facture": "invoice",
    "numéro": "number",
    "date": "date",
    "heure": "hour",
    "minute": "minute",
    "seconde": "second",
    "jour": "day",
    "semaine": "week",
    "mois": "month",
    "année": "year",
    "matin": "morning",
    "après-midi": "afternoon",
    "soir": "evening",
    "nuit": "night"
    }

    print("=== Application de traduction ===")
    while True:
        mot = input("Entrez un mot en français (ou 'q' pour quitter) : ")
        if mot.lower() == "q":
            break
        traduction = traduire_mot(mot, dictionnaire)
        print("Traduction est :", traduction)
        print()

    print("Merci d'avoir utilisé l'application de traduction.")

# Point d'entrée du programme
if __name__ == "__main__":
    main()