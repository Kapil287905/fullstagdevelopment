# multiple
'''
A---------B
     |
     c
'''

class collage:
    def __init__(self,collagename,degree):
        self.collagename = collagename
        self.degree = degree

class institute:
    def __init__(self,institutename,courses):
        self.institutename = institutename
        self.courses = courses

class student(collage,institute):
    def __init__(self, collagename, degree,institutename,courses,sname,percentage):
        # super().__init__(collagename, degree) # only reads first parent thats why don' use when multiple p
        self.collagename = collagename
        self.degree = degree
        self.institutename = institutename
        self.courses = courses
        self.sname = sname
        self.percentage = percentage

    def show(self):
        print(f"{self.sname} {self.percentage}")
        print(f"{self.collagename} {self.degree}")
        print(f"{self.institutename} {self.percentage}")

s = student("Acharaya","mca","itv","fsd","komal",89.34)
s.show()