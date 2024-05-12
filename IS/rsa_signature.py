import random, hashlib
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def generate_prime_number():
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def generate_keys():
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = pow(e, -1, phi)
    return (e, n), (d, n)
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)
message = "Hello, World!"
hashed_message = hashlib.md5(message.encode()).hexdigest()
public_key, private_key = generate_keys()
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)
unhashed_message = hashlib.md5(decrypted_message.encode()).hexdigest()
print(f"Original message:{message}\nHashed message:{hashed_message}\nEncryptedMeessage:{encrypted_message}\nDecryptedMsg:{decrypted_message}\nUnhashedMsg:{unhashed_message}")