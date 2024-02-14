plain_text = input("Enter plain text:").upper()
key=input("Enter key:").upper()
ciphertext=""
if len(plain_text)== len(key):
    for i in range(len(plain_text)):
        conversion=(ord(key[i])-65)^(ord(plain_text[i])-65)
        conversion=conversion%26
        ciphertext=ciphertext+chr(65+conversion)
    print("Cipher text is :",ciphertext)
else:
    print("key and plaintext not equal")        
    
    