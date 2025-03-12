# age = int(input("Enter your age = "))
# if age >= 18:
#     raise Exception("you are eligible for vate")
# else:
#     raise Exception("you are not eligible for vote")    

# cresting new exception as AgeException
class AgeException(Exception):
    def __init__(self, msg):
        self.msg = msg

try:
    age = int(input("Enter your age = "))
    if age > 60:
        raise AgeException("you are too old give vote")
    elif age < 18:
        raise AgeException("you are too young to give vote")
    else:
        print("you are eligible for vote")

except ValueError:
    print("Age must be an integer value")
except KeyboardInterrupt:
    print("Exception stob from your side. try again")
    
