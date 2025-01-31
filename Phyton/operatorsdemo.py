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
# a = int(input("Enter a="))
# b = int(input("Enter b="))
# # print(a+=b) # Error print() dosen't alloe =(Assifment) SyntaxError: invalid syntax
# a = b
# print("a=",a) # 5
# print("b=",b) # 5
# a += b #a=a+b
# print("a=",a)
# b *= 10
# print("b =",b)
# b-=a
# print("a=",a)

# logical operators

# print(5>6 and 5<6) #False
# print(5>6 and 5<6 and 6>5) #False
# print(5>6 or 5<6) #True
# print(5>6 or 5<6 or 6>5) #True
# print(not 5>6) #True
# print (5==6) #false

#Membership operators works with sequence data type(str,truple,list,set,dict)
# name = "python"
# print('p' in name) #True
# # n = 123547
# # print(2 in n) # error TypeError: argument of type 'int' is not iterable
# n = 26545669
# print("2" in str(n)) #True
# mylist = ["py",23,"js"]
# print(23 in mylist)

# identity operator check id() of object
# x = 12
# y = 12
# z = x
# print("x=",x,id(x)) 
# print("y=",y,id(y))
# print("z=",z,id(z))
# print(x==y) #True
# print(x is y) #True
# print(x is z) #True

# x = 12
# y = 10
# z = x
# print("x=",x,id(x)) 
# print("y=",y,id(y))
# print("z=",z,id(z))
# print(x==y) #False
# print(x is y) #False
# print(x is z) #True

# m = [1,2,3]
# n = m
# p = [1,2,3]
# print("m=",m,id(m)) 
# print("n=",n,id(n))
# print("p=",p,id(p))
# print(m==n) #True
# print(m is n) #True
# print(m==p) #True
# print(m is p) #False

# print(0 == None) #false
# print(0 is None) #Flase with SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# print('' == None) #False
# print('' is None) #Flase with SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# print('' == False) #False
# print (0 is False) #False
# print(0==False) # True brcause interpreter converts False
# # print(1 is not 1) #False
# print(1!=1) #false
# print(bool("") is bool(None)) # True

# Bitwise operator (preforms bunary operation) only with int
# &(and) |(or) ~(not) ^(xor)
# x = 5
# y = 3
# print(x&y) #1
# print(x|y) #7
# print(~x) #-6
# print(x^y) #6

# Shift operators >>(right),left(<<) binary optation
# x = 6
# print(bin(6)) #110
# print(x>>2) # 1
# print(x) # 6
# print(x<<2) #24

# Tarnary operator
# syntax Truestmt condition Falsestmt
n=int(input("enter number"))
# print("n is +ve number" if n>0 else "n is -ve number")
# ans="n is +ve number" if n>0 else "n is -ve number"
# print(ans)
# print(f"{n} is +ve number" if n>0 else f"{n} is -ve number")
ans=f"{n} is +ve number" if n>0 else f"{n} is -ve number"
print(ans)
