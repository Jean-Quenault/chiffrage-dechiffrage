from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keys():
    # Création d'un couple de clés
    key = RSA.generate(1024)
    return key

def encrypt_message(public_key, message):
    # Chiffrement avec PKCS1_OAEP
    cipher = PKCS1_OAEP.new(public_key)
    enc_data = cipher.encrypt(message.encode())
    return enc_data

def decrypt_message(private_key, encrypted_message):
    # Déchiffrement avec PKCS1_OAEP
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode('utf-8')

# L'utilisateur déclenche la création des clés
key = generate_keys()

# Afficher les clés
private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')
print("Clé privée:\n", private_key.decode())
print("Clé publique:\n", public_key.decode())

# Saisie du message secret par l'utilisateur
secret_message = input("Entrez votre message secret: ")

# Chiffrage et affichage du message chiffré
encrypted_message = encrypt_message(key.publickey(), secret_message)
print("Message chiffré:", encrypted_message)

# Déchiffrage et affichage du message déchiffré
decrypted_message = decrypt_message(key, encrypted_message)
print("Message déchiffré:", decrypted_message)