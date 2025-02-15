# string methord
# s = "welcome to python"
# print(s,len(s))
# print("----count(value,startindex,stopindex)----")
# print(s.count("o")) # 3
# print(s.count("")) # 18 (len+1)
# print(s.count("o",5,14)) # 1
# print(s.count("om",5,14)) # 0 if not found then zero
# print(s.count("x",5,14)) # 0
# print("----find(value,startindex,stopindex)----")
# print(s.find("o")) # 4 first o index number
# print(s.find("")) # 0 (empty)
# print(s.find("o",5,16)) # 9
# print(s.find("om",5,14)) # -1 0 if not found then -1
# print(s.find("x",5,14)) # -1
# print("----index(value,startindex,stopindex)----")
# print(s.index("o")) # 4 first o index number
# print(s.index(""))  # 0 (empty)
# print(s.index("o",5,16)) # 9
# print(s.index("x")) # ValueError: substring not found
# print(s["0"]) # error way of writing

# print("----join()----")
# s = "Welcome to python"
# print(s,len(s))
# print(s.join("x")) # don't join
# print("x".join(s)) # wxexlxcxoxmxex xtxox xpxyxtxhxoxn
# print(" ".join(s)) # w e l c o m e   t o   p y t h o n
# print(sorted(s)) # sorting ans gives in list[]
# print("".join(sorted(s))) # Wceehlmnoooptty

# print("----split()----")
# # print(s.split()) # ['Welcome', 'to', 'python']
# # x = "puthon"
# # print(x.split()) # ['puthon']
# # y = "1,2,3,4,5"
# # print(y.split()) # ['1,2,3,4,5']
# # print(y.split(",")) # ['1', '2', '3', '4', '5']
# # print(y.split(",",3)) #['1', '2', '3', '4,5'] 

# z = "red,blue,green,white,black"
# print(z.split()) # ['red,blue,green,white,black']
# print(z.split(",")) # ['red', 'blue', 'green', 'white', 'black']
# print(z.split(",",3)) # split only for first 3 element

# print("----splitline()----")
# print(s.splitlines()) # ['Welcome to python']
# s1 = "hi\nhow are you"
# print(s1)
# print(s1.split()) # ['hi', 'how', 'are', 'you']
# print(s1.splitlines()) #['hi', 'how are you']

# print("----zfill()----")
# print(s.zfill(13)) # won't add zero becouse len is 17
# print(s.zfill(23)) # 000000Welcome to python

# print("----strip()----")
# print(s.strip())
# x = "          mengo          grapes"
# print(x)
# print(x.strip()) # remove  only starting white space

a = "Welcome to python"
b = "python12"
c = ""
d = "puthon/&@123"
e = "123"

# print(a.upper())
# print(a.lower())

# print(a.isupper()) #False
# print(a.islower()) #False
# print(b.islower()) #True
# print(e.islower()) #False

# checking with a
# print(a)
# print(a.isalnum()) #False
# print(a.isalpha()) #False
# print(a.isnumeric()) #False
# print(a.isdigit()) #False

# print(b)
# print(b.isalnum()) #True
# print(b.isalpha()) #False
# print(b.isnumeric()) #False
# print(b.isdigit()) #False

# print(c)
# print(c.isalnum()) #False
# print(c.isalpha()) #False
# print(c.isnumeric()) #False
# print(c.isdigit()) #False

# print(d)
# print(d.isalnum()) #False
# print(d.isalpha()) #False
# print(d.isnumeric()) #False
# print(d.isdigit()) #False

# print(e)
# print(e.isalnum()) #True
# print(e.isalpha()) #False
# print(e.isnumeric()) #True
# print(e.isdigit()) #True

for i in "python":
    print(1)
