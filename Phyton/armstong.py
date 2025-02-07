# WAP to check number is armsstrong or not
try:
    n = int(input("Enter n = "))
    n1 = n
    n2 = n1
    counter = 0
    sum = 0
    while n > 0:
        n = n // 10
        counter = counter + 1
    print(f"Count of digit of {n1} = {counter}")
    while n1 > 0:
        rem = n1 % 10
        n1 = n1 // 10
        sum = sum+(rem**counter)
    if sum == n2:
        print(f"{n2} is armstrong number")
    else:
        print(f"{n2} is not armstrong number") 
except:
    print("invalid input")
