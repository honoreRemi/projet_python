#coding utf-8
def change_name(new_name):
    global terminal_name
    terminal_name = new_name
    print(f"Le nom du terminal a été modifié pour '{terminal_name}'.")

def show_help():
    print("Liste des commandes disponibles :")
    print("name : Modifie le nom du terminal.")
    print("help : Affiche la liste des commandes.")
    print("quit : Quitte le terminal.")

def quit_terminal():
    print("Au revoir !")
    exit()

terminal_name = "default"

while True:
    user_input = input(f"{terminal_name} > ")

    if user_input == "name":
        new_name = input("Entrez le nouveau nom du terminal : ")
        change_name(new_name)
    elif user_input == "help":
        show_help()
    elif user_input == "quit":
        quit_terminal()
    else:
        print("Commande invalide. Tapez 'help' pour afficher la liste des commandes.")