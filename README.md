# Python Encryption Project

This project includes three Python scripts to demonstrate different types of encryption: asymmetric using RSA, symmetric with AES, and a simple example of symmetric encryption.

## Files

1. **chiffrageAsymetrique.py**: Uses RSA for asymmetric encryption and decryption.
2. **chiffrageSymetriqueAES.py**: Uses AES for symmetric encryption and decryption.
3. **chiffrageSymetrique.py**: A simple example of symmetric encryption and decryption.

## Usage

### 1. Asymmetric Encryption (RSA)

To use the asymmetric encryption script:

`python chiffrageAsymetrique.py`

#### This will generate an RSA key pair, encrypt a user-entered message, and then decrypt it.

### 2. Symmetric Encryption (AES)

For the script using AES:

`python chiffrageSymetriqueAES.py`

This script allows entering text, which will then be encrypted and decrypted with a randomly generated AES key.

### 3. Simple Symmetric Encryption

To run the simple symmetric encryption example:

`python chiffrageSymetrique.py`

This script allows entering text and choosing to encrypt or decrypt it using a numerical key.

## Dependencies

- PyCryptodome

Install PyCryptodome via pip to use these scripts:

`pip install pycryptodome`
