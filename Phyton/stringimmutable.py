# string immutable (not changable)

s = ("welcome")
print(s, id(s)) # welcome 3065476392896
print(s[0])
# s[0] = "r" #TypeError: 'str' object does not support item assignment
print(s)

# type1 by creating new variable
news = "r" + s[1:]
print(news)

# type2 by creating new variable
print(s.replace("w","r")) # relcome not store
s = s.replace("w","r")
print(s, id(s)) # relcome 3065476394672