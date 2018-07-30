class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        if self.items == []:
            return True
        else: 
            return False
    def enqueue(self, data):
        self.items.insert(0, data)
    def dequeue(self):
        self.items.pop()
    def front(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def __str__(self):
        if not self.isEmpty():
            en_queue = enumerate(self.items)
            for index, value in en_queue:
                if (index == len(self.items) - 1):
                    print(value, end = "")
                else:
                    print(value, end = ", ")
        else:
            print('Emptty') 