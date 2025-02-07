n = int(input("Enter n = "))
i = 1
fact = 1
while i <= n:
    fact = fact * i
    i+=1
print(f"Factorial of {n} = {fact}")