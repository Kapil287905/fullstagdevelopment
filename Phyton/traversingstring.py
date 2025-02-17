# traversing via for loop and while

# s = "pyathon is too easy"
# for i in s:
#     print(i)

# 1)show along with index number
# for i in s:
#     print(i,s.index(i))

# msg = "welcome to python world"
# # for i in range(len(msg)):
# #     print(msg[i],i)

# i = 0
# while i < len(msg):
#     print(msg[i],i)
#     i+=1

# 2) WAP to traverse every 2nd charcter of any string entred by user
# n = input("Enter string = ")
# for i in range(2,len(n),2):
#      print(n[i])

# for i in range(1,len(n),2):
#      print(n[i])

# 3) WAP to print number of occurances of enter
# character from any string by using loop

# str = input("Enter string = ")
# char = input("Enter char = ")
# count = 0
# flag = False
# for i in str.lower():
#     if i==char.lower():
#         count+=1
#         flag = True
# if flag:    
#     print(f"count of {char}={count}")
# else:
#     print(f"Entred '{char} not present in {str}' thats why count = {count}")


# 4) WAP to find character index by using loop

# str = input("Enter string = ")
# char = input("Enter char = ")
# # indexnum = []
# indexnum = 0
# flag = False
# for i in range(len(str.lower())):
#     if char.lower() == str[i]:
#      #indexnum.append(i)
#      indexnum = i
#      flag = True

# if flag:
#    print(f"Index of {char} = {indexnum}")
# else:
#    print(f"Wntered '{char}' not present in {str}")

# 5) WAP to show reverse of string by whiout loop

# str = input("Enter string = ")
# print(str)
# print(reversed(str)) # reversed object at 0x000002CEBC46AEC0
# print("".join(reversed(str)))
# print(str[::-1])

# for i in reversed(str):
#     print(i, end="")

# # via loop
# for i in str[::-1]:
#     print(i, end="")

# via loop type2
# for i in range(len(str)-1,-1,-1):
#     print(str[i], end="")

# via loop type3
# s=""
# for i in str:
#     s= i+s
# print(s)

# 6) WAP to show vowels and count from entred string

# str = input("Enter string = ")
# vowels = "aeiou"
# acount,ecount,icount,ocount,ucount=0,0,0,0,0

# for i in str.lower():
#     if i == "a":
#         acount+=1
#     elif i == "e":
#         ecount+=1
#     elif i == "i":
#         icount+=1
#     elif i == "o":
#         ocount+=1
#     elif i == "u":
#         ucount+=1

# print(f"vowels count \na={acount}\ne={ecount}\ni={icount}\no={ocount}\nu={ucount}")

# 7) WAP to show vowels and consonent seperately with total count from entred string
# str = input("Enter string = ").lower()
# v,c = 0,0
# vowels = "aeiou"
# vow = ""
# conso = ""
# for i in str:
#     if i in vowels:
#         vow = vow + i
#         v+=1
#     else:
#         conso = conso + i
#         c+=1
# print(f"Vowels present in {str}={vow} and count={v}")
# print(f"consonent present in {str}={conso} and count={c}")

# 8) WAP to show find and replace for entred char as per entred string

str = input("Enter string = ").lower()
char = input("Enter character to find and replace = ").lower()
flag = False
result = ""
for i in str:
    if i == char:
        print("Character found")
        x= input("entred replace char = ").lower()
        flag = True
        result = result + x
    else:
        result = result + i

if flag:
    print(f"Repalce string={result}")
else:
    print(f"Entred '{result}' not found")
    