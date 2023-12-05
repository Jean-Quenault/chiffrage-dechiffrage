# input un texte, le print, créer une clé, faire deux méthodes crypter et decrypter avec deux parametres en entres, avec un menu pour crypter ou decrypter


def get_input():
    return input("Entrez le texte à traiter: ")

def crypter(texte, cle):
    # Exemple simple de cryptage (à améliorer selon vos besoins)
    return "".join(chr(ord(char) + cle) for char in texte)

def decrypter(texte, cle):
    # Exemple simple de décryptage (à améliorer selon vos besoins)
    return "".join(chr(ord(char) - cle) for char in texte)

def main():
    texte = get_input()
    print("Texte saisi:", texte)

    cle = int(input("Entrez la clé de cryptage (un nombre): "))

    choix = input("Tapez 'c' pour crypter ou 'd' pour décrypter: ")

    if choix.lower() == 'c':
        texte_crypte = crypter(texte, cle)
        print("Texte crypté:", texte_crypte)
    elif choix.lower() == 'd':
        texte_decrypte = decrypter(texte, cle)
        print("Texte décrypté:", texte_decrypte)
    else:
        print("Choix non valide")

if __name__ == "__main__":
    main()
