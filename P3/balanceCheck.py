from stack import Stack

def isBalanced(input_string):
    if len(input_string) % 2 != 0:
        return False
    elif input_string == '':
        return True
    s = Stack()
    start = list('{[(')
    end = list('}])')
    i = 0

    while i < len(input_string):
        expr = input_string[i]
        if expr in start:
            s.push(expr)
        elif expr in end:
            if s.isEmpty():
                return False
            popped_item = s.pop()
            if expr == ')' and popped_item != '(' or \
            expr == ']' and popped_item != '[' or \
            expr == '}' and popped_item != '{':
                return False 
        else:
            return False
        i += 1

    return s.isEmpty()

if __name__ == '__main__':
    seq = input("Enter the sequence: ")
    print(isBalanced(seq))