n = int(input("Enter fibb range = "))
i = 1
a = 0
b = 1
print(a)
print(b)
while i<=n-2:
    c = a + b
    print(c)
    a = b
    b = c
    i += 1