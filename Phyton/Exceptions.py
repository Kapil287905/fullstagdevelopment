# a=int(input("Enter a = "))
# b=int(input("Enter b = "))
# print(a/b)

# ValueError
# KeyboardInterrupt
# ZeroDivisionError

#Handling code in exception
# try:
#     a=int(input("Enter a = "))
#     b=int(input("Enter b = "))
#     print(a/b)
# except:
#     print("Input invalid")

# finally:
#     print("Test case done") # it show in voth case when exception are fetched or not fetched

try:
    a=int(input("Enter a = "))
    b=int(input("Enter b = "))
    print(a/b)
except ValueError:
    print("value must be inter number only")
except KeyboardInterrupt:
    print("Execution cancelled by you. try again")
except ZeroDivisionError:
    print("Denominator i.e 'b' cannot be zero")

finally:
    print("Test case done") # it show in voth case when exception are fetched or not fetched