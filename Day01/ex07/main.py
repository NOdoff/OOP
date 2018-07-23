#!/usr/bin/env python3

from dad import Dad
from joke import Joke

def main():
    dad = Dad()
    joke = Joke()
    dad.speak()
    joke.reply()

if __name__ == '__main__':
    main()
