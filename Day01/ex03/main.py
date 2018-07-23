#!/urs/bin/env python3

from greeter import Greeter
from insult_comic import InsultComic

def main():
    g = Greeter()
    i = InsultComic()
    g.speak("Wesley")
    i.speak("Wesley")

if __name__ == "__main__":
    main()
