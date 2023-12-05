# Projet de Chiffrement Python

Ce projet comprend trois scripts Python pour démontrer différents types de chiffrement : asymétrique avec RSA, symétrique avec AES et un exemple simple de chiffrement symétrique.

## Fichiers

1. **chiffrageAsymetrique.py** : Utilise RSA pour le chiffrement et le déchiffrement asymétrique.
2. **chiffrageSymetriqueAES.py** : Utilise AES pour le chiffrement et le déchiffrement symétrique.
3. **chiffrageSymetrique.py** : Un exemple simple de chiffrement et déchiffrement symétrique.

## Utilisation

### 1. Chiffrement Asymétrique (RSA)

Pour utiliser le script de chiffrement asymétrique :

python
`python chiffrageAsymetrique.py`

#### Cela générera une paire de clés RSA, chiffrera un message saisi par l'utilisateur et le déchiffrera ensuite.

### 2. Chiffrement Symétrique (AES)

Pour le script utilisant AES : 

python
`python chiffrageSymetriqueAES.py`

Ce script permet de saisir un texte, qui sera ensuite chiffré et déchiffré avec une clé AES générée aléatoirement.

### 3. Chiffrement Symétrique Simple

Pour exécuter l'exemple simple de chiffrement symétrique :

python
`python chiffrageSymetrique.py`

Ce script permet de saisir un texte et de choisir de le chiffrer ou le déchiffrer en utilisant une clé numérique.

## Dépendances

- PyCryptodome

Installez PyCryptodome via pip pour utiliser ces scripts :

bash
`pip install pycryptodome`

## Licence

Ce projet est privé.