from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key():
    """Génère une clé AES aléatoire de 16 octets."""
    return get_random_bytes(16)

def encrypt(plain_text, key):
    """
    Crypte un texte en utilisant AES.
    
    :param plain_text: Texte à crypter.
    :param key: Clé AES utilisée pour le cryptage.
    :return: Texte crypté.
    """
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return cipher.iv + ct_bytes

def decrypt(cipher_text, key):
    """
    Décrypte un texte crypté en utilisant AES.
    
    :param cipher_text: Texte à décrypter.
    :param key: Clé AES utilisée pour le décryptage.
    :return: Texte décrypté.
    """
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(cipher_text[AES.block_size:]), AES.block_size)
    return pt.decode()

# Interface utilisateur
key = generate_key()
user_input = input("Entrez le texte à crypter: ")
encrypted = encrypt(user_input, key)
print("Texte crypté:", encrypted)

decrypted = decrypt(encrypted, key)
print("Texte décrypté:", decrypted)
