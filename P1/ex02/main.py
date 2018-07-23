#!/usr/bin/env python3

from animal import Animal
from dog import Dog
from cat import Cat

def main():
    a = Animal()
    d = Dog()
    c = Cat()
    array = ["An Animal", "A Dog", "A Cat"]
    for i in range(0, len(array)):
        print("Making " + array[i])
    a.speak()
    d.speak()
    c.speak()
    a.sleep()
    d.sleep()
    c.sleep()
if __name__ == "__main__":
    main()
