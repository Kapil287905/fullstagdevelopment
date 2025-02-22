# addin element insert()
# mylist = []
# mylist.insert(5,"red")
# print(mylist)
# print(mylist[0])
# mylist.insert(3,"green")
# print(mylist)
# mylist.insert(1,"blue")
# print(mylist)
# mylist.insert(-1,"white")
# print(mylist)
# mylist.insert(len(mylist),"grey")
# print(mylist)
# # insert at middle
# mylist.insert(len(mylist) // 2,"orange")
# print(mylist)

# WAP to add elements into mylist as per count entred by user
# mylist = []
# counter = int(input("Enter list counter = "))

# for i in range(counter):
#      n = int(input(f"Enter {i+1} number = "))
#      mylist.insert(i,n)
# print(mylist)

# updating elements for exostong elements from list
# colors = []
# print(colors)
# # colors[0] = "red" # error IndexError: list assignment index out of range
# print(colors)

# colors = ["red","green","blue"]
# print(colors)
# colors[0] = "black"
# print(colors)
# colors[3] = "pink" # IndexError: list assignment index out of range
# print(colors)

# WAP to desplay vowels and consonent and counts from entred name by user
# names = input("enter name = ")
# v=[]
# c=[]
# for i in names:
#     if i in "aeiouAEIOU":
#         v.append(i)
#     else:
#         c.append(i)
# print(f"Vowels={v} and total vowels={len(v)}")
# print(f"consonent={c} and total consonent={len(c)}")

# Removing elements- pop(),remove(),del
# books = ["py","cpp","html","js","py","java"]
# print(books)
# books.pop()
# print(books)
# books.pop(3)
# print(books)
# books.pop(31) # IndexError: pop index out of range
# print(books)

# mylist = []
# mylist.pop() # IndexError: pop from empty lis

# books = ["py","cpp","html","js","py","java"]
# print(books)
# books.remove("cpp")
# print(books)
# books.remove("py") # first occurances
# print(books)
# books.remove("py")
# print(books)
# books.remove("py") # ValueError: list.remove(x): x not in list
# print(books)

# del books[0]
# print(books)

# del books[10]  # IndexError: list assignment index out of range
# print(books)

# del books # remove object
# print(books) # NameError: name 'books' is not defined. Did you mean: 'bool'?

# books = ["py","cpp","html","js","py","java"]
# print(books)

# reverse(),sort(),extend(),copy(),clear(),count()
# newbooks = books.reverse()
# print(newbooks) # None

# books.reverse()
# print(books)

# books.sort() # ascending
# print(books)

# x = ["hello", True,4.5,44]
# x.sort() # ypeError: '<' not supported between instances of 'bool' and 'str'
# print(x)

# z = [23,4,2.5,11]
# z.sort(reverse=True) # decending
# print(z)

# extend
# m = [1,2,3,]
# print(m)
# m.extend(z)
# print(m)

# student = []
# for i in range(3):
#     name = input("entred name = ")
#     grade = input("entred grade = ")
#     # student.append([name,grade]) # [['aa', 'a'], ['bb', 'b'], ['cc', 'c']]
#     student.extend([name,grade]) # ['aa', 'a', 'bb', 'b', 'cc', 'c']
# print(student)

books = ["py","cpp","html","js","py","java"]
print(books,id(books)) # 2403436159296

# copy()
# b = books
# print(b,id(b)) # 2403436159296
# bk = books.copy()
# print(b,id(bk)) # 2403438062976
# n=[1,1,1]
# print(n)
# n = books.copy()
# print(n,id(n)) # 2663697701440

# # clear
# n.clear()
# print(n)

# # count
# print(books.count("py"))
# print(books.count("")) # 0
# print(books.count("rust")) # 0

#index
# print(books.index("py")) # 0
# print(books.index("py",3,5)) # 4

books = []
while True:
    try:
        print("welcome to my libray\n----------------------------------")
        print("1:Add book\n2:Show book\n3:update book\n4:Remove book\n5:Search book\n6:Exit")
        choice=int(input("Enter choice number = "))
        if choice == 1:
            count = int(input("Enter count for book = "))
            for i in range(count):
                title=input(f"enter {i+1} books title = ").lower()
                books.append(title)
            print("Books added successfully!!")
        elif choice == 2:
            if len(books) > 0:
                print("Avaliable book",books)
            else:
                print("Books not Avaliable")
        elif choice == 3:
            if len(books) > 0:
                chktitle= input("Enter book to update title = ").lower()
                if chktitle in books:
                    print(f"{chktitle} book found")
                    newtitle = input(f"enter new title for {chktitle} = ").lower()
                    for i in range(len(books)):
                        if chktitle == books[i]:
                            books[i] = newtitle
                    print("Book title updated successfully")
                else:
                    print(f"{chktitle} is not available or entred correct title")
            else:
                print("Books database is empty so first add books then update")
        elif choice == 4:
            if len(books) > 0:
                deltitle= input("Enter book to delete = ").lower()
                if deltitle in books:
                    print(f"{deltitle} book found")
                    # for i in range(len(books)):
                    #     if deltitle == books[i]:
                    #         books.pop(i)   
                    for i in books:
                        if deltitle == i:
                            books.remove(i)
                    print("Book delete successfully")        
                else:
                    print(f"{deltitle} is not available or entred correct title")
            else:
                print("Books database is empty so first add books then delete")
        elif choice == 5:
            if len(books) > 0:
               chktitle= input("Enter book to search = ").lower()
               if chktitle in books:
                   print(f"{chktitle} book found")
               else:
                    print(f"{chktitle} is not available or entred correct title")
            else:
                print("Books database is empty so first add books then search")
        elif choice == 6:
            print("Thank you for using our service!!!")
            break
        else:
            print("Invalid choice number")
    except:
        print("Invalid input")