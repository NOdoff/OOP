from stack import Stack

string = input("Enter the string to be reversed: ")

def strrev(input_string):
    s = Stack()
    l_string = list(input_string)
    for value in l_string:
        s.push(value)
    n_string = []
    for value in range(0, s.size() - 1):
        n_string.append(s.pop())
    print("Reversed String: " + ''.join(n_string)) 

strrev(string)
