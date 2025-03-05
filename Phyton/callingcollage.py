# import collegedemo

# # print(dir(collegedemo))
# print(collegedemo.College.name)
# # print(collegedemo.College.show()) # TypeError: College.show() missing 1 required positional argument: 'self'
# print(collegedemo.c1.show())

# or 
from collegedemo import College,c1
# College.show() #error
c1.show()