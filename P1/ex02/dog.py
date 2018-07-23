#!/usr/bin/env python3

from animal import Animal

class Dog(Animal):
    def speak(self):
        Animal.speak(self)
        print ("Woof")
    def sleep(self):
        Animal.sleep(self)
