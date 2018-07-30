from stack import Stack
from queue import Queue



def revKElements(input_string, k):
    s = Stack()
    q = Queue()
    l_string = input_string.split(',')
    n_string = l_string[:k]
    
    print('L_string', l_string)
    print(n_string, 'n_string')
    for value in n_string:
        q.enqueue(value)
    print(q, "q")

    while not q.isEmpty():
        s.push(q.dequeue())
    # for value in q:
    #     value = q.dequeue()
    #     s.push(value)
    print(q, 'q2')
    print(s, 's')

    while not s.isEmpty():
        q.enqueue(s.pop())
    print(q)
    print(list(q))
    print( ', '.join(list(q) + l_string[k:]), 'q3')


    # n_string = []
    # for value in range(0, s.size() - 1):
    #     n_string.append(s.pop())
    # print(''.join(n_string))
if __name__ == '__main__':
    string = input("Enter the list of numbers: ")
    k = int(input("Enter k: "))
    
    revKElements(string, k)
