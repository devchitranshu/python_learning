nb = int(input("Enter the number: "))
factorial = 1
if nb < 0 :
    print("negative number ka factorial nhi hota")
elif nb == 0:
    print("the facctorial of zero is 1")
else:
    for i in range(1,nb+1):
        factorial = factorial*i
    print("the factorial of a",nb,"is",factorial)


