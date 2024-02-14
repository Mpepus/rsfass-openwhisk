import hashlib
import os 

def calculer_hash_fichier(nom_fichier):
    # Ouvre le fichier en mode lecture binaire
    with open(nom_fichier, "rb") as f:
        # Calcul du hash SHA-256
        sha256_hash = hashlib.sha256()
        while chunk := f.read(4096):  # Lecture par bloc de 4096 octets
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def verifier_integrite(nom_fichier, hash_o):
    # Calcul du hash actuel du fichier
    hash_actuel = calculer_hash_fichier(nom_fichier)
    
    # Comparaison du hash actuel avec le hash original
    if hash_actuel == hash_o:
        print("Le fichier n'a pas été modifié.")
    else:
        print("Le fichier a été modifié.")

# Chemin vers votre fichier obtenue après le déchiffrement hello_decrypt.js
hash_decrypt = "../Outputs_Faas/hello_decrypt.js"
#Chemin vers votre fichier hash original hash.js
original = "../Inputs_Faas/hello.js"
hash_original = calculer_hash_fichier(original)

# Vérification de l'intégrité du fichier plaintext
verifier_integrite(hash_decrypt, hash_original)
