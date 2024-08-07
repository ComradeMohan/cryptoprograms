def generate_playfair_square(keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_square = []
    for char in keyword:
        if char not in key_square and char != 'J':
            key_square.append(char)
    for char in alphabet:
        if char not in key_square:
            key_square.append(char)
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def find_position(char, key_square):
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == char:
                return row, col
    return None

def prepare_text(plaintext):
    plaintext = plaintext.replace('J', 'I').upper()
    prepared_text = ""
    i = 0
    while i < len(plaintext):
        prepared_text += plaintext[i]
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            prepared_text += 'X'
        elif i + 1 < len(plaintext):
            prepared_text += plaintext[i + 1]
            i += 1
        else:
            prepared_text += 'X'
        i += 1
    return prepared_text

def playfair_encrypt(plaintext, key_square):
    prepared_text = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(prepared_text), 2):
        a, b = prepared_text[i], prepared_text[i + 1]
        row_a, col_a = find_position(a, key_square)
        row_b, col_b = find_position(b, key_square)
        if row_a == row_b:
            ciphertext += key_square[row_a][(col_a + 1) % 5] + key_square[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += key_square[(row_a + 1) % 5][col_a] + key_square[(row_b + 1) % 5][col_b]
        else:
            ciphertext += key_square[row_a][col_b] + key_square[row_b][col_a]
    return ciphertext

def playfair_decrypt(ciphertext, key_square):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row_a, col_a = find_position(a, key_square)
        row_b, col_b = find_position(b, key_square)
        if row_a == row_b:
            plaintext += key_square[row_a][(col_a - 1) % 5] + key_square[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            plaintext += key_square[(row_a - 1) % 5][col_a] + key_square[(row_b - 1) % 5][col_b]
        else:
            plaintext += key_square[row_a][col_b] + key_square[row_b][col_a]
    return plaintext

keyword = "ATHENS"
plaintext = "COMMUNICATE"
key_square = generate_playfair_square(keyword)
print("Key Square:")
for row in key_square:
    print(row)
ciphertext = playfair_encrypt(plaintext, key_square)
print("Encrypted text:", ciphertext)
decrypted_text = playfair_decrypt(ciphertext, key_square)
print("Decrypted text:", decrypted_text)