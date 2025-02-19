# traverse tuple via for loop and while loop

colors=("red","green","blue","white","grey","black","orange")

# for i in colors:
#     print(i)

# for i in reversed(colors):
#     print(i,end=" ")

# for i in colors[::-1]:
#     print(i)

# while loop
# i=0
# while i < len(colors):
#     print(colors[i])
#     i = i + 1

# WAP to shpw count of element entred by user below tuple
# colors=("red","green","blue","white","red","grey","black","orange")
# element = input("Enter element = ").lower()
# count = 0
# flag = False
# for i in colors:
#      if i==element:
#         count+=1
#         flag = True
# if flag:    
#     print(f"count of {element}={count}")
# else:
#     print(f"Entred '{element} not present in '{colors}' thats why count = {count}")

# WAP to shpw index of element entred by user below tuple
# colors=("red","green","blue","white","red","grey","black","orange")
# element = input("Enter element = ").lower()
# indexnum = []
# #indexnum = 0
# flag = False
# for i in range(len(colors)):
#     if element == colors[i]:
#      indexnum.append(i)
#      #indexnum = i
#      flag = True

# if flag:
#    print(f"Index of {element} = {indexnum}")
# else:
#    print(f"Entered '{element}' not present")



colors=("red","green","blue","white","red","grey","black","orange")
element = input("Enter element = ").lower()

flag = False
result = ()
for i in colors:
    if i == element:
        print("Element found")
        x= input("entred replace element = ").lower()
        flag = True
        result = result + x
    else:
        result = result + i

if flag:
    print(f"Repalce string={result}")
else:
    print(f"Entred '{result}' not found")