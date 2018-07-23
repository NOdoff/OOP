from person import Person
from student import Student

class Teacher(Person):

    def greet(self, student):
        print(self.name + ": Welcome to class, " + student.name)
