

a = []

n = int(input("Enter the number of element you want to enter: "))
for i in range(n):
    a.append(int(input("Enter the element: ")))
print("your list is",a)

lg = max(a)
print("The largest element is",lg)
