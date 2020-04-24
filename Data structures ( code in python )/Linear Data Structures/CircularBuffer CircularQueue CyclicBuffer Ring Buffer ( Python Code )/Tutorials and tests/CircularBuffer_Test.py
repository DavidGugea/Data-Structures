class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity

        self.head = 0 
        self.tail = 0 

        self.items = [None] * self.capacity 

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return len(self.items[self.head : self.tail + 1]) == self.capacity or self.tail == self.head - 1

    def getBufferItems(self):
        return self.items

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("The buffer is full. It can't enqueue any more items to it.")

        if self.is_empty():
            self.items[self.tail] = item
            self.tail += 1
        else:
            self.items[self.tail] = item
            self.tail += 1

            if self.tail == self.capacity:
                self.tail = 0
