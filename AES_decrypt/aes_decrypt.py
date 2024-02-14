from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def read_key_from_file(key_file_path):
    with open(key_file_path, 'rb') as key_file:
        key = key_file.read()
    return key


def decrypt_file(encrypted_file_path, key, output_file_path):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        iv = encrypted_file.read(block_size := algorithms.AES.block_size // 8)
        ciphertext = encrypted_file.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    with open(output_file_path, 'wb') as decrypted_file:
        decrypted_file.write(plaintext)

    print("Le fichier a été déchiffré avec succès.")



# Chemin vers le fichier contenant la clé de chiffrement
key_file_path = "../Inputs_Faas/key.txt"

# Lecture de la clé de chiffrement depuis le fichier
key = read_key_from_file(key_file_path)

# Chemin pour le fichier chiffré en sortie
encrypted_output_file_path = "../Outputs_Faas/hello_cipher.js"

# Chemin pour le fichier déchiffré en sortie
decrypted_output_file_path = "../Outputs_Faas/hello_decrypt.js"

# Appel de la fonction pour déchiffrer le fichier chiffré
decrypt_file(encrypted_output_file_path, key, decrypted_output_file_path)
