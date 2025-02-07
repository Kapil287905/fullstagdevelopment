# WAP to show reverse of any +ve int number 
try:
    n = int(input("Enter n = "))
    n1 = n
    rev = 0
    while n > 0:
        rem = n % 10
        n = n // 10
        rev = rev * 10 +rem
    print(f"reverse of number of {n1} = {rev}") 
except:
    print("invalid input")