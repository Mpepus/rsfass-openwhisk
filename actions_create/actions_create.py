import subprocess
import os

def terminal_commande(commande):
    try:
        #Exécutons la commande dans le terminal
        subprocess.run(commande, shell=True, check=True)
        print("action créer")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'éxécution de la commande : {e}")
    

#Nous allons exécuter la commande pour créer une action 
command = "wsk action create hello_decrypt ../Outputs_Faas/hello_decrypt.js"
terminal_commande(command)