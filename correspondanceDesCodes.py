#coding utf-8

import subprocess

def get_device_password():
    try:
        # Exécute une commande adb pour obtenir des informations
        result = subprocess.run(['adb', 'shell', 'getprop', 'ro.build.display.id'], 
                                capture_output=True, text=True)
        # Affiche le résultat
        print("Informations du téléphone :", result.stdout.strip())
    except Exception as e:
        print("Erreur lors de l'accès au téléphone :", e)

if __name__ == "__main__":
    get_device_password()