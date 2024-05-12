def encDec(word, key):
    if len(word) != len(key):
        raise ValueError("Word and key must have the same length.")
    result = []
    for i in range(len(word)):
        res = (ord(word[i]) - 65) ^ (ord(key[i]) - 65)
        res %= 26
        result.append(chr(res + 65))
    return ''.join(result)

word = 'RAMSWARUPK'
key = 'RANCHOBABA'
encrypted_result = encDec(word=word, key=key)
print(f'Encrypted: {encrypted_result}')
decrypted_result = encDec(word=encrypted_result, key=key)
print(f'Decrypted: {decrypted_result}')
