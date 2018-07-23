#!/usr/bim/env python3

from building import Building
from campus import Campus

def main():
    b = Building("Math Building", 25)
    c = Campus()
    n = Building("Science Building", 17)
    b.get_info()
    n.get_info()
    c.add_building(b)
    c.add_building(n)
    c.get_info()

if __name__ == "__main__":
    main()
