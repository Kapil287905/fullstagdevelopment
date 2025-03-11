# raise

# x=int(input("Enter number = "))
# if x>0:
#     print("Accepted x = ",x)
# else:
#     raise Exception("Rejected -ve number not allowed")

try:
    x=int(input("Enter number = "))
    if x>0:
        print("Accepted x = ",x)
    else:
        raise Exception("Rejected -ve number not allowed")
except ValueError:
    print("value must be inter number only")
except KeyboardInterrupt:
    print("Execution cancelled by you. try again")