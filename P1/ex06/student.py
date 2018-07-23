from person import Person

class Student(Person):
    def greet(self, teacher):
        print(self.name + ": Good morning, " + teacher.name)
