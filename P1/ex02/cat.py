#!/usr/bin/env python3

from animal import Animal

class Cat(Animal):
    def speak(self):
        Animal.speak(self)
        print("Meow")
    def sleep(self):
        Animal.sleep(self)
