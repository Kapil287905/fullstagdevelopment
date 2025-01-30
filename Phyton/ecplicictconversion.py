"""
# float to all (int,str,bool,complex)
# n = 34.45
#n = 34.55
# n = 0.0
print(type(n),n)
n_int = int(n)
print(type(n_int),n_int) #34 trincates decimal
n_str = str(n)
print(type(n_str),n_str) # str
n_bool = bool(n)
print(type(n_bool),n_bool) # bool-true when n is zero then only false
n_complex = complex(n)
print(type(n_complex),n_complex) # complex
"""

# str to all (int,str,bool,complex)
# n = "welcome"
# n = ""
# print(type(n),n)
# n_int = int(n)
# print(type(n_int),n_int) # error ValueError: invalid literal for int() with base 10: 'welcome'
# n_float = float(n)
# print(type(n_float),n_float) # ValueError: could not convert string to float: 'welcome'
# n_bool = bool(n)
# print(type(n_bool),n_bool) # bool-True when n is "z" then only False
# n_complex = complex(n)
# print(type(n_complex),n_complex) # error ValueError: complex() arg is a malformed string


# complex to all (int,str,bool,complex)
# n = 5j
n = 0j
print(type(n),n)
# n_int = int(n)
# print(type(n_int),n_int) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
# n_float = float(n)
# print(type(n_float),n_float) # TypeError: float() argument must be a string or a real number, not 'complex'
#n_bool = bool(n)
# print(type(n_bool),n_bool) # bool-True when n is 0j then only False
# n_str = str(n)
# print(type(n_str),n_str) # str

# None to all (int,str,bool,complex)
n = None
print(type(n),n)
# n_int = int(n)
# print(type(n_int),n_int) # error TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
# n_float = float(n)
# print(type(n_float),n_float) # TypeError: float() argument must be a string or a real number, not 'complex'
# n_bool = bool(n)
# print(type(n_bool),n_bool) # False only
# n_str = str(n)
# print(type(n_str),n_str) # 
# n_complex = complex(n)
# print(type(n_complex),n_complex) # TypeError: complex() first argument must be a string or a number, not 'NoneType'

# int to all (int,str,bool,complex)
n = 15
# n = 0
print(type(n),n)
n_str = str(n)
# print(type(n_str),n_str) # str
n_float = float(n)
print(type(n_float),n_float) # float
n_bool = bool(n)
print(type(n_bool),n_bool) # bool-True when n is "z" then only False
n_complex = complex(n)
print(type(n_complex),n_complex) # error ValueError: complex() arg is a malformed string