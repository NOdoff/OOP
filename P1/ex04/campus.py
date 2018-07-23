#!/usr/bin/env python3

from building import Building

class Campus:
    def __init__(self):
       self.buildings = []
       self.num_buildings = 0
       self.capacity = 0
    def add_building(self, Building):
        self.buildings.append(Building.name)
        self.num_buildings += 1
        self.capacity += Building.capacity
    def get_info(self):
        print("The campus has {} building(s) with compiled capacity of".format(str(self.num_buildings))
        + " " + str(self.capacity) + " people")
