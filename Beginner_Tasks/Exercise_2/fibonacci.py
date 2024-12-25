
nt = int(input("how many terms : "))
n1 , n2 = 0,1
count = 0
if nt <= 0:
    print("please enter a positive integer")
elif nt == 1:
    print(n1)
elif nt == 2:
    print(n2)
else:
    while count < nt:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1
