#!/usr/bin/env python3

from classroom import Classroom
from teacher import Teacher
from student import Student

def main():

    t1 = Teacher("Wesley")
    c1 = Classroom(t1)
    t2 = Teacher("Anand")
    c2 = Classroom(t2)
    c1_s1 = ("Alice")
    c1_s2 = ("Carol")
    c1_s3 = ("Eve")
    c2_s1 = ("Bob")
    c2_s2 = ("Dave")
    c1.add_student(c1_s1)
    c1.add_student(c1_s2)
    c1.add_student(c1_s3)
    c2.add_student(c2_s1)
    c2.add_student(c2_s2)
    c1.get_info()
    c2.get_info()
    c1.greeting()
    c2.greeting()
if __name__ == '__main__':
    main()
