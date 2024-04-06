def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def primitive_check(g, p, list):
    for i in range(1, p):
        list.append(pow(g, i) % p)
    for i in range(1, p):
        if list.count(i) > 1:
            list.clear()
            return -1
        return 1
list=[]      
while True:
    p=int(input("Enter values of p:"))
    g=int(input("Enter values of g:"))
    if ((is_prime(p)==True) and primitive_check(g,p,list)):
        print("correct input ")
        a=int(input("Enter values of a:"))
        b=int(input("Enter values of b:"))
        if a >= p or b >= p:
            print(f"Private Key Of Both The Users Should Be Less Than {p}!")
        else:
            y1, y2 = pow(g, a) % p, pow(g, b) % p
            k1, k2 = pow(y2, a) % p, pow(y1, b) % p
            print(f"\nSecret Key For User 1 Is {k1}\nSecret Key For User 2 Is {k2}\n")
            if k1 == k2:
                print("Keys Have Been Exchanged Successfully")
            else:
                print("Keys Have Not Been Exchanged Successfully")
            break    
    else:
        print("enter correct values")
        break   

