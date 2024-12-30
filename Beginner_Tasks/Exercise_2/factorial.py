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

# n = int(input("enter the number of which you want to get factorial : "))
# fac = 1
 # i = 1
# while i <= n:
#     fac *= i
#      i += 1
# print("the factorial is :"fac)


# n = int(input("Enter the number you want to find the factorial of : "))
# fac = 1

# for i in range(1,n+1):
# fac *= i
#print=("the factorial is :", fac)
