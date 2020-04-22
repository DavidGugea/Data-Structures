class CircularBuffer(object):
    def __init__(self, capacity):
        self.items = list()
    
        self.head = -1
        self.tail = -1

        self.capacity = capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("The circular buffer reached it's capacity.") 

        if self.is_empty():
            self.head = 0 

        self.tail += 1
        
        if self.tail == self.capacity:
            self.tail = 0 
        
        self.items.insert(self.tail, item) 

    def dequeue(self):
        if self.is_empty():
            raise Exception("The circular buffer is empty. It can't delete anything")

        del self.items[self.head]
        self.head += 1

        if self.head >= len(self.items):
            self.head = 0

    def is_empty(self):
        return self.items == list()

    def is_full(self):
        return len(self.items) == self.capacity
    
    def getTail(self):
        return { self.tail : self.items[self.tail] }

    def getHead(self):
        return { self.head : self.items[self.head] }

    def getBufferItems(self):
        return self.items 
