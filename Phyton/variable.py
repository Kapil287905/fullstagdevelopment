'''
variable=identifier/lable ise to store some value
syntax

variable_name=value

Rules:-
1) it must start with alphabets or _(underscore)
2) special char are not allowed except _(underscore)
3) keyword cannot be used as variable name
4) length can br any
5) if value is alphabets or special char then it must be enclosed in quotes
6) cannot start with digit but can be used in between
'''
name='priya'
print(name)
print(type(name)) #data type
print(id(name)) #2515228066848 show object id unique

name='komal'
print(name)
print(type(name)) #data type
print(id(name)) #2468367336528 show object id unique

#1mag="welcome" #syntax error
m1sg="welcome"
print(m1sg)
_=23435
print(_)
roll_number=234
print(roll_number)
#print(rollnumber) #NameError: name 'rollnumber' is not defined. Did you mean: 'roll_number'?

#email@id="abc@gmail.com" #syntax error
#print(email@id)
#grade=A
#print(grade) #NameError: name 'A' is not defined

number=1,2,3
print(number) #(1, 2, 3) tuple datatype

#a,b=100 #TypeError: cannot unpack non-iterable int object

#Multi-veriable assigning value

a,b=100,200 #multivalued variable
print(a,b)


