
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def gcd(a,b):
    if a == b :
        return a

    elif b>a :
        return gcd(b,a)
    else:
        return gcd(b,a-b)
print(gcd(a,b))
