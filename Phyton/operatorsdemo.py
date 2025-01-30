# Qperators->Symbols which performs some operations in operands which can be one or many
# Unary->only one operands +(plus),-(minus),!(not)
#Binary=>more then one operands >,<,in,+=

# 1) Arithmatic operatots->+,-,*,/,%,//(floor divison),**(powerof)
# 2) Reational/condition/comparation-> >,<>=,<=,==,!=
# 3) assigment  operatots->+=,-=,*=,/=,%=,//=(floor divison),**=(powerof),
# 4)
# 5)
# 6)
# 7)
# 8)
# 9)

# Arithmatic
# a = int(input("Enter a="))
# b = int(input("Enter b="))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b) # always gives answer in float
# print(a % b) # remainder always gives answer in int 
# print(a // b) # floor division always gives answer in int
# print(a**b) # powerof

# relation # gives result in True or false (boolean)
# a = int(input("Enter a="))
# b = int(input("Enter b="))
# print(a>b)
# print(a>=b)
# print(a<b)
# print(a<=b)
# print(a==b)
# print(a!=b)

#assigment
a = int(input("Enter a="))
b = int(input("Enter b="))
# print(a+=b) # Error print() dosen't alloe =(Assifment) SyntaxError: invalid syntax
a = b
print("a=",a) # 5
print("b=",b) # 5
a += b #a=a+b
print("a=",a)
b *= 10
print("b =",b)
b-=a
print("a=",a)