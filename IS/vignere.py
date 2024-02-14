def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            encrypted_text += encrypted_char  
    return encrypted_text
plain_text = input("Enter Plain text:")
key = input("Enter key:")
plain_text=plain_text.upper()
key = key.upper()
encrypted_text = encrypt_vigenere(plain_text, key)
print("Encrypted text:", encrypted_text)
