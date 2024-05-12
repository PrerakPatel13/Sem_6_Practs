def encrypt(key,message):
    message=message.upper()
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=""
    for letter in message:
        if letter in alpha:
            letter_index=(alpha.find(letter) + key) % 26
            result=result+alpha[letter_index]
        else:
            result=result+letter
    return result      
    
def decrypt(key,message):
    message=message.upper()
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=""
    for letter in message:
        if letter in alpha:
            letter_index=(alpha.find(letter) - key) % 26
            result=result+alpha[letter_index]
        else:
            result=result+letter
    return result     

pt="meet me after the toga party"
encrypted=encrypt(3,pt)
print("Encryption:",encrypted)
decrypted=decrypt(3,encrypted)
print("Encryption:",decrypted)
    