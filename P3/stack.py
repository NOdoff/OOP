class Node:
    def __init__(self, value, next = None):
        self.data = value
        self.next = next

class Stack:
    node = Node(data)    
    def __init__(self):
        self.nodes = []

    def isEmpty(self):
        if self.nodes == []:
            return None    

    def push(self, data):
        self.nodes.append(data)

    def pop(self):
        return self.nodes.pop()

    def peek(self):
        return self.nodes[len(self.nodes) - 1]

    def size(self):
        return len(self.nodes)

    def __str__(self):
        while node is not None:
            end = ", " if node.next else "]"
            print(node.content, end = end, flush = True)
            node = node.next
        