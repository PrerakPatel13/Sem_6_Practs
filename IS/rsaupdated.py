import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

p = 17
q = 13
pt=int((input("Enter plain text:")))
phi = (p - 1) * (q - 1)
n = pt + phi


e = random.randint(1, phi)
while not is_prime(e):
    e = random.randint(1, phi)
print("Prime e:",e)
i = 1
d = 1
while True:
    if (phi * i + 1) % e != 0:
        i += 1
    else:
        d = (phi * i + 1) // e
        break

c = (pt ** e) % n
print("Cipher text is:", c)

p = (c ** d) % n
print("Decrypted text is:", p)
