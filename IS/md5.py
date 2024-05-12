def left_rotate(x, n):
    return (x << n) & 0xFFFFFFFF
def md5(message):
    padding_length = 0
    if (len(message) + 64) % 512:
        message += "1"
        padding_length = 512 - ((len(message) + 64) % 512)     
    message += "0" * padding_length
    print(f"Padding Length  : {padding_length+1}")
    message_words = [int(message[i : i + 32], 2) for i in range(0, len(message), 32)] #bin to int 32 bitwise
    message_words.append(len(message)-64) #rest 64 bits
    a,b,c,d = [0x01234567, 0x89ABCDEF, 0xFEDCBA98, 0x76543210]
    def F(x, y, z):
        return (x & y) | (~x & z)
    for i in range(0, len(message_words), 16):
        f = F(b, c, d)
        g = random.randint(1,100) # k voh flowchart mein
        for j in range(16):
            if i + j < len(message_words):
                temp = (a + f + message_words[i + j] + g) & 0xFFFFFFFF
                a,b,c,d = d,(b+left_rotate(temp, 7)) & 0xFFFFFFFF,b,c
    return (format(a, "08x")+format(b, "08x")+format(c, "08x")+format(d, "08x"))
import random
random_message = "".join([random.choice(["0", "1"]) for _ in range(1000)])
print(f"Random 1000-bit message:{random_message}\nAfter first round:{md5(random_message)}")