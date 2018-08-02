class Stack:
 
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
            return True
        else: 
            return False


    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items == None or len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __iter__(self):
            i = 0
            while i < self.size():
                yield self.items[i]
                i += 1
                
    def __str__(self):
        return ", ".join([str(x) for x in self.items[::-1]]) if not self.isEmpty() else ""
        