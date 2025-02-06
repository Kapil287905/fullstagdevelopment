# WAP to show sum of digit of entred positive interger number

try:
    n = int(input("Enter any digit number = "))
    sum = 0
    n1 = n
    while n > 0:
        rem = n % 10
        n = n // 10
        sum = sum + rem
    print(f"sum of digit of {n1} = {sum}")
    
except:
    print("invalid input")