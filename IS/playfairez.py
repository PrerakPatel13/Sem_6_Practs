def create_matrix(key):
    key = key.upper()
    matrix = [[0 for i in range(5)] for j in range(5)]
    letters_added = []
    row = 0
    col = 0
    for letter in key:
        if letter not in letters_added:
            matrix[row][col] = letter
            letters_added.append(letter)
        else:
            continue
        if (col == 4):
            col = 0
            row += 1
        else:
            col += 1
    for letter in range(65, 91):
        if letter == 74:
            continue
        if chr(letter) not in letters_added:
            letters_added.append(chr(letter))
            index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index += 1
    return matrix

def separate_same_letters(message):
    index = 0
    while (index < len(message)):
        l1 = message[index]
        if index == len(message) - 1:
            message = message + 'X'
            index += 2
            continue
        l2 = message[index + 1]
        if l1 == l2:
            message = message[:index + 1] + "X" + message[index + 1:]
        index += 2
    return message

def indexOf(letter, matrix):
    for i in range(5):
        try:
            index = matrix[i].index(letter)
            return (i, index)
        except:
            continue

def playfair(key, message, encrypt=True):
    inc = 1
    if encrypt == False:
        inc = -1
    matrix = create_matrix(key)
    message = message.upper()
    message = message.replace(' ', '')
    message = separate_same_letters(message)
    cipher_text = ''
    for (l1, l2) in zip(message[0::2], message[1::2]):
        row1, col1 = indexOf(l1, matrix)
        row2, col2 = indexOf(l2, matrix)
        if row1 == row2:
            cipher_text += matrix[row1][(col1 + inc) % 5] + matrix[row2][(col2 + inc) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1 + inc) % 5][col1] + matrix[(row2 + inc) % 5][col2]
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    return cipher_text

option = 1
while(option == 1 or option == 2):
    option = int(input("Select an option\n 1 for Encryption\n 2 for Decryption\n 3 for Exit: "))
    if(option == 1):
        plainText = input("Enter the Plain text: ")
        key = input("Enter Key: ")
        print('Encrypting')
        print(playfair(key, plainText))
    if(option == 2):
        cipherText = input("Enter the cipher text: ")
        key = input("Enter Key: ")
        print('Decrypting')
        print(playfair(key, cipherText, False))
    if (option == 3):
        break
