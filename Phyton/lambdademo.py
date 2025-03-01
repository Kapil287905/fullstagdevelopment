# lambda function-anonymous function (not know function) without using def keyword
# syntax:
# variable_name=lambda argument:excpression

# by using def
# def display():
#     print("def finctopn")

# display()

# # by using lambda
# x = lambda:print("lambda function")
# x()
# print(type(x)) # function

# position argument
def addition(a,b):
    return a+b

print("Addition = ",addition(45,89))

# or 
#type1
addition = lambda a,b:a+b
print("Addition = ",addition(45,89))

#type2
addition = (lambda a,b:a+b)(45,89)
print("Addition = ",addition)

#type3
(lambda a,b:print("addition = ",a+b))(45,89)

# WAP to shpw +ve and -ve numbers in lambda function
(lambda n:print(n,"+ve numner") if n > 0 else print(n,"-ve number"))(n=int(input("enter n = ")))

ans = lambda n:print(n,"+ve numner") if n > 0 else print(n,"-ve number")
ans(-4)

# WAP show 1 to 10 number by using lambda
ans=lambda:[i for i in range(1,11)]
print(ans())

ans = lambda:[print(i) for i in range(1,11)]
ans()

