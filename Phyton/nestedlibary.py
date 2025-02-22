books = [["isbn","title","author","price","qty"]]
data=[]
while True:
    try:
        print("welcome to my libray\n----------------------------------")
        print("1:Add book\n2:Show book\n3:update book\n4:Remove book\n5:Search book\n6:Exit")
        choice=int(input("Enter choice number = "))
        if choice == 1:
           count = int(input("Enter count for book = "))
           for i in range(count):
               isbn=int(input(f"Enter {i+1} book isbn = "))
               title=input(f"Enter {isbn} book title = ")
               author=input(f"Enter {isbn} book author = ")
               price=float(input(f"Enter {isbn} book price = "))
               qty=input(f"Enter {isbn} book qty = ")
               data = [isbn,title,author,price,qty]
               books.append(data)
               print("-----Avalable books------")
               for i in books:
                   for j in i:
                       print(j,end=" ")
                   print()
        elif choice == 2:
            if len(data) > 0:
                pass
            else:
                print("Books not Avaliable")
        elif choice == 3:
            if len(data) > 0:
                print("-----update books detail-----")
                chkisbn = int(input("Enter book isbn number update record = "))
                flag = False
                for i in books:
                    if i[0] == chkisbn:
                        flag = True
                        print("ISBN = ",i[0])
                        print("Title = ",i[1])
                        print("Author = ",i[2])
                        print("Price = ",i[3])
                        print("Qty = ",i[4])
                        print("-----update option as per asked below--------")
                        print("1:Title\n2:Author\n4:Qty\n5:Cancel")
                        choice = int(input("enter "))
                        if choice == 1:
                            newtitle = input(f"Enter new title for isbn {i[0]} =")
                            i[1] = newtitle
                            print("Title updated successfully")
                        elif choice == 2:
                            newauthor = input(f"Enter new author for isbn {i[0]} =")
                            i[2] = newauthor
                            print("Author updated successfully")
                        elif choice == 3:
                            newprice = float(input(f"Enter new price for isbn {i[0]} ="))
                            i[3] = newprice
                            print("Price updated successfully")
                        elif choice == 4:
                            newqty = input(f"Enter new qty for isbn {i[0]} =")
                            i[4] = newqty
                            print("QTY updated successfully")
                        elif choice == 5:                            
                            print("operation Cancelled")
                            break
                        else:
                            print("Invalid choice number")
                    
                    if flag == False:
                        print("Book not found or check ISBN number again")
            else:
                print("Books database is empty so first add books then update")
        elif choice == 4:
            if len(data) > 0:
                print("-----update delete detail-----")
                chkisbn = int(input("Enter book isbn number delete record = "))
                flag = False
                for i in books:
                    if i[0] == chkisbn:
                        flag = True
                        print("ISBN = ",i[0])
                        print("Title = ",i[1])
                        print("Author = ",i[2])
                        print("Price = ",i[3])
                        print("Qty = ",i[4])
                        choice=input("R u sure want to delete record type yes/no = ")
                        if choice.lower() == "yes" or choice.lower() == "y":
                            books.remove(i)
                            print("Record deleted successfuly")
                        elif choice.lower() == "no" or choice.lower() == "n":
                            print("Record not deleted")
                        else:
                            print("Invalid choice number try again")
                    
                    if flag == False:
                        print("Book not found or check ISBN number again")
            else:
                print("Books database is empty so first add books then delete")
        elif choice == 5:
            if len(data) > 0:
               pass
            else:
                print("Books database is empty so first add books then search")
        elif choice == 6:
            print("Thank you for using our service!!!")
            break
        else:
            print("Invalid choice number")
    except:
        print("Invalid input")