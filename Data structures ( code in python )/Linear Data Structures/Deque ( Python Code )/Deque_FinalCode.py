class Deque(object):
    def __init__(self):
        self.items = list()

    def get_size(self):
        return len(self.items)

    def __len__(self):
        return len(self.items)

    def append(self, item):
        self.items.append(item) 

    def appendLeft(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop()

    def popLeft(self):
        firstItem = self.items[0]
        del self.items[0]

        return firstItem
    
    def peek(self):
        return self.items[-1]

    def peekLeft(self):
        return self.items[0]
