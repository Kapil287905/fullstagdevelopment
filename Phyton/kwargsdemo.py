# def bookdata(**kwargs):
#     # print(kwargs)
#     for k,v in kwargs.items():
#         print(k, "=", v)

# bookdata(title="py", author="pp")
# # bookdata("js", "jj") # TypeError: bookdata() takes 0 positional arguments but 2 were given

# *atgs and kwargs

def bookdata(*data, **moredata):
    print(data)
    print(moredata)

bookdata(1001,"python","pp",peice=800,qty=6)
# bookdata(peice=800,qty=6,1001,"python","pp") # error Positional argument cannot appear after keyword argumen
# bookdata(1001,peice=800,qty=6,"python") #incorrect
bookdata(1001,"python",peice=800)
