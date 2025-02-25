# methods
# students = {}
# print(students)
# #update
# students.update({"name":"raj"})
# print(students)
# students.update({"name":"komal"})
# print(students)
# students.update({"grade":"A","per":89.67,"degree":"BCA"})
# print(students)
# students.update({"subjects":["py","js","cpp"]})
# print(students)
# students.update({"email":("k@gmail","k1@gmail.com")})
# print(students)
# # students.update({["city","pincode"]:["mumbai",400098]}) # key list not allow
# students.update({("city","pincode"):("mumbai",400098)})
# print(students)

# # remove elements
# students.pop("per")
# print(students)
# # students.pop("percentahr") # KeyError: 'percentahr'
# # print(students)
# students.popitem() # last element
# print(students)
# students.popitem() # last element
# print(students)

# students.clear()
# print(students)

# values(),get(),keys(),items()
numbers = {1:100,2:200,3:300,4:400}
print(numbers)
print(numbers.values())
print(numbers.keys())
print(numbers.items())
print(numbers.get(1)) # reade key and show value
print(numbers.get(100)) # None 100 key is not present
print(list(numbers.items()))
print(tuple(numbers.items()))
print(set(numbers.items()))

# copy()
numbers1 = numbers.copy()
print(numbers1)

# fromkeys{}
n = [1,2,3]
print(n)
n = dict.fromkeys(n,"ITV") 
print(n)

# setdeafult{}
movie = {"name":"kgf","stars": 5}
print(movie)
x = movie.setdefault("duration","2.10mins")
print(movie)
print(x)
movie.update({"duration":"3hrs"})
print(movie)
movie.update({"duration":x})
print(movie)



