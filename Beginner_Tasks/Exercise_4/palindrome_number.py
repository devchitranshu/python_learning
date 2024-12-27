n = int(input ("Enter a number : "))
v = n
rev = 0
while n != 0:
    rev = rev * 10 + n % 10
    n = n // 10
if v == rev:
  print ("the number is palindrome")
else :
    print ("the number is not palindrome")