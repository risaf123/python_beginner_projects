# ENCRYPTION & DECRYPTION
import random
import string
chars=chars = string.ascii_letters + string.digits + string.punctuation + " "

chars=list(chars)
key=chars.copy()
random.shuffle(key)
print(f'{chars}')
print(f'{key}')

# ENCRYPTION
def encrypt():
    plain_text=input('enter the plain text')
    cipher_text=''
    for letters in plain_text:
        index=chars.index(letters)
        cipher_text+=key[index]
    print(f'cipher text is : {cipher_text}')
encrypt()

# DECRYPTION
def decrypt():
    cipher_text=input('enter the cipher text')
    plain_text=''
    for letters in cipher_text:
        index=key.index(letters)
        plain_text+=chars[index]
    print(f'plain text is : {plain_text}')
decrypt()



   