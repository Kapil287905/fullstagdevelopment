# WAP to check number is palindrom or not
try:
    n = int(input("Enter n = "))
    n1 = n
    rev = 0
    while n > 0:
        rem = n % 10
        n = n // 10
        rev = rev * 10 +rem
    if rev == n1:
        print(f"{n1} is palindrome")
    else:
        print(f"{n1} is not palindrome") 
except:
    print("invalid input")