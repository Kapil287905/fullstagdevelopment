# map()-used to produce result in sequence but takes function and list of inputs or 
# sequence of object

#Syntax:- map(function,listofinputs) 

# WAP to show sequence of 1 to 10 by using map

# using comprehension
ans = {i:i*i for i in range(1,11)}
print(ans)

# using lambada

# ans = lambda:[print(i*i) for i in range(1,11)]
# ans()

ans = {i: (lambda i:i*i)(i) for i in range(1,11)}
print(ans)

#map() with lambda

print(list(map(lambda i:i*i,range(1,11))))
# print(dict(map(lambda i:i*i,range(1,11)))) # TypeError: 'dict' object is not callable

def sequare(x):
    return x*x
print(list(map(sequare,range(1,11))))

# example-2
animal = ["Cat","Dog","Triger"]
print(list(map(list,animal)))

word = "morning"
print(list(map(list,word)))

# example-3

def addition(a,b):
    return a+b

print(tuple(map(addition,(5,6),(10,20))))
print(list(map(lambda a,b:a+b,(5,6),(10,20))))

print(tuple(map(addition,("red","green"),("blue","white"))))
print(list(map(lambda a,b:a+b,("red","green"),("blue","white"))))