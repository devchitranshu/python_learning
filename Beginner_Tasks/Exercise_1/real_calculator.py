

x = int(input("Enter the phla number: "))
y = int(input("Enter the dusra number: "))

print("Choose the operation :")
print("1 for sum")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
cont = "y"
while cont.lower() == "y":
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("The sum is : ", x + y)

    elif choice == 2:
        print("the subtraction is : ", x - y)

    elif choice == 3:
        print("the multiplication is : ", x * y)

    elif choice == 4:
        if y == 0:
            print("infinity")
        else:
            print("the division is : ", x / y)
            break

    elif choice  != ("1" or "2" or "3" or "4"):
        print("jo diya gya hai kripya usme se chune")








