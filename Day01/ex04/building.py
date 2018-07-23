#!/usr/bin/env python3

class Building:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def get_info(self):
        print("Building \"" + self.name + "\" can hold {} people".format(self.capacity))





