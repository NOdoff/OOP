class Queue:

    def __init__(self):
        
        self.items = []

    def isEmpty(self):

        if self.items == []:
            return True
        else: 
            return False

    def enqueue(self, data):

        self.items.append(data)

    def dequeue(self):

        return self.items.pop(0)


    def front(self):

        return self.items[0]
        
    def size(self):

        return len(self.items)

    def __iter__(self):
        i = 0
        while i < self.size():
            yield self.items[i]
            i += 1

        
    def __str__(self):
        return ", ".join([str(x) for x in self.items]) if not self.isEmpty() else ""
        