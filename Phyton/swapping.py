try:
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    print(f"Before swapping a = {a} and b = {b}")
    # with using third variable
    #  c=a
    #  a=b
    #  b=c

    # without using third variable

    # a,b = b,a # only works in python

    a = a + b
    b = a - b
    a = a - b


    print(f"After swapping a = {a} and b = {b}")
except:
    print("invalid input")