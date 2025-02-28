# 4 was of writing user defined function
# 1) default function (no parameter and no return type)
# 2) with parameter but no return type
# 3) without parameter but with return type
# 4) with parameter and with return type

# flobal variable
name = input("Enter name = ")
rollnum = input("Enter rollnumber = ")

# type1
# def display1():
#     print(f"My name is {name} and rollnumber is {rollnum}")

# display1()

# type2
# def display2(x,y):
#     print(f"My name is {x} and rollnumber is {y}")

# display2() # TypeError: display2() missing 2 required positional arguments: 'x' and 'y'
# display2(name) # TypeError: display2() missing 1 required positional argument: 'y'
# display2(name,rollnum) # argument
# display2("rakesh",121) # argument rakesh 121
# display2(rollnum,name) # argument

# type3
# def display3():
#     # return f"My name is {name} and rollnumber is {rollnum}"
#     return(name,rollnum)

# print(display3())
# ans = display3()
# print(f"My name is {ans[0]} and rollnumber is {ans[1]}")

# type4
def display4(x,y):
    # return f"My name is {x} and rollnumber is {y}"
    return(name,rollnum)

print(display4(name,rollnum))
ans = display4(name,rollnum)
print(f"My name is {ans[0]} and rollnumber is {ans[1]}")