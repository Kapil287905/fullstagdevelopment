mylist = ["red","green","blue","white"]
for i in mylist:
    print(i)

i = 0
while i < len(mylist):
    print(mylist[i],i)
    i+=1

# WAP to find entred elements and replace as per asked new element

mylist = ["red","green","blue","white","red"]
print(mylist)
element = input("Enter element = ").lower()
count = 0
flag = False
result = []
for i in mylist:
    if i == element:
        print("Element found")
        x= input("entred replace element = ").lower()
        flag = True
        # result = result + list(x)
        result.append(x)
    else:
        # result = result + list(i)
        result.append(i)
if flag:
    print(f"Repalce string={result}")
else:
    print(f"Entred '{result}' not found")