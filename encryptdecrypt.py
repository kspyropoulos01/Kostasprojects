#######################################################
# Name:   Kostas Spyropoulos
# Class:   CIS-1400-NET07
# Assignment: Homework 12  Spring 2021
# File:   Homework_12.py
# Purpose: Encrypts Plain Text to be Caesar Ciphers & Decrypts Caesar Ciphers
#######################################################

print('\n**  Kostas Spyropoulos  **\n')  # Display author's name

# Named Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'  # Constant of all letters of alphabet


def main():
    # Show user to either encrypt or decrypt
    print('Encrypt/Decrypt Program')
    print('1 - Encrypt String')
    print('2 - Decrypt String')
    # Ask user to either enter 1, 2, or enter
    prompt = input('Please enter 1 or 2, press enter to exit:')
    # While loop that permits pressing enter to exit, 1 to encrypt,
    # and 2 to decrypt
    while prompt != '':
        # Pressing 1 leads to encryption
        if prompt == '1':
            print()
            # Enter text to be encrypted and its key
            encryption = str(input('Enter string to encrypt:'))
            key_1 = int(input('Enter key:'))
            # Run caesar_encrypt(encryption,key_1) function next
            caesar_encrypt(encryption, key_1)
            # Ask user to encrypt, decrypt, or exit
            prompt = input('Please enter 1 or 2, press enter to exit:')
        # Pressing 2 leads to decryption
        elif prompt == '2':
            print()
            # Enter text to be decrypted and its key
            decryption = str(input('Enter string to decrypt:'))
            key_2 = int(input('Enter key:'))
            # Run caesar_decrypt(decryption,key_2) function next
            caesar_decrypt(decryption, key_2)
            # Ask user to encrypt, decrypt, or exit
            prompt = input('Please enter 1 or 2, press enter to exit:')


def caesar_encrypt(encryption, key_1):
    # Make message to be encrypted all lower case
    encryption_1 = encryption.lower()
    # Shift ALPHABET by key_1 to make new_alphabet_1 for encryption
    new_alphabet_1 = ALPHABET[key_1:26] + ALPHABET[0:key_1]
    # Encrypt message entered
    translationtable = str.maketrans(ALPHABET, new_alphabet_1)
    # Print encryption
    print (encryption_1.translate(translationtable))
    print()


def caesar_decrypt(decryption, key_2):
    # Make message to be decrypted all lower case
    decryption_1 = decryption.lower()
    # Shift ALPHABET by key_2 to make new_alphabet_2 for decryption
    new_alphabet_2 = ALPHABET[key_2:26] + ALPHABET[0:key_2]
    # Decrypt message entered
    translationtable = str.maketrans(new_alphabet_2, ALPHABET)
    # Print decryption
    print (decryption_1.translate(translationtable))
    print()

# Call main procedure
main()

