from teacher import Teacher
from student import Student

class Classroom:
    capacity = 20
    def __init__(self, teacher):
        self.students = []
        self.teacher = teacher
        teacher = " "
        self.num_students = 0
    def add_student(self, student):
        self.students.append(Student(student))
        self.num_students += 1


    def get_info(self):
        print("The classroom has a standart capacity of " + str(Classroom.capacity)
        + " and is run by " + self.teacher.name + ". It currently has {} students".format(self.num_students))
    def greeting(self):
        for i in range(len(self.students)):
            self.teacher.greet(self.students[i])
            self.students[i].greet(self.teacher)
