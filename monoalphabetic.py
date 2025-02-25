import random
def generate_cipher_mapping():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)

    mapping = dict(zip(alphabet, shuffled_alphabet))
    return mapping
def encrypt(plaintext, mapping):
    ciphertext = ''.join(mapping.get(char, char) for char in plaintext.lower())
    return ciphertext
def decrypt(ciphertext, reverse_mapping):
    plaintext = ''.join(reverse_mapping.get(char, char) for char in ciphertext.lower())
    return plaintext
plaintext = "Hello, World!"
cipher_mapping = generate_cipher_mapping()
encrypted_text = encrypt(plaintext, cipher_mapping)
decrypted_text = decrypt(encrypted_text, {v: k for k, v in cipher_mapping.items()})

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)