# reduce()-used to show summarized by using functools module
#Syntax:- reduce(function,listofinputs) 

#WAP to show sum of 1 to 10 number
# without lamda

import functools # built-in module

def sum(x,y):
    return x+y

print(functools.reduce(sum,range(1,11)))

print(functools.reduce(lambda x,y:x+y,range(1,11)))