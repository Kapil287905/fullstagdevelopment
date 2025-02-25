# books = {
#     "title":"py",
#     "author":"pp",
#     "grade":"A",
#     "price":800
#     }
# print(books)
# for i in books: # only keys
#     print(i)

# for i in books.items(): # only keys and values
#     print(i)

# for i in books.values(): # only values
#     print(i)

# for i in books.keys(): # only keys
#     print(i)

# for k,v in books.items():
#     print(k, "=", v)

# booksdb = {
#     {"title":"py","author":"pp","qty":5,"price":800},
#     {"title":"js","author":"jj","qty":8,"price":600},
#     {"title":"cpp","author":"cc","qty":10,"price":900}
# } #wrong way of writinf

booksdb = [
    {"title":"py","author":"pp","qty":5,"price":800},
    {"title":"js","author":"jj","qty":8,"price":600},
    {"title":"cpp","author":"cc","qty":10,"price":900}
]
# print(booksdb)
for i in booksdb:
    # print(i)
    for k,v in i.items():
        print(k, "=", v)