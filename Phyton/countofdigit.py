try:
    n = int(input("Enter any digit number = "))
    n1 = n
    counter = 0
    while n > 0:
        n = n // 10
        counter = counter + 1
    print(f"Count of digit of {n1} = {counter}")
    
except:
    print("invalid input")