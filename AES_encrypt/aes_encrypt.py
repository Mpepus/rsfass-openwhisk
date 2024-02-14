from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def read_key_from_file(key_file_path):
    with open(key_file_path, 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_file(file_path, key, output_file_path):
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    block_size = algorithms.AES.block_size // 8
    #plaintext += b'\0' * (block_size - len(plaintext) % block_size)
    iv = os.urandom(block_size)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(output_file_path, 'wb') as encrypted_file:
        encrypted_file.write(iv + ciphertext)

    print("Le fichier a été chiffré avec succès.")


# Chemin vers le fichier à chiffrer
file_to_encrypt = "../Inputs_Faas/hello.js"

# Chemin vers le fichier contenant la clé de chiffrement
key_file_path = "../Inputs_Faas/key.txt"

# Lecture de la clé de chiffrement depuis le fichier
key = read_key_from_file(key_file_path)

# Chemin pour le fichier chiffré en sortie
encrypted_output_file_path = "../Outputs_Faas/hello_cipher.js"

# Appel de la fonction pour chiffrer le fichier
encrypt_file(file_to_encrypt, key, encrypted_output_file_path)

