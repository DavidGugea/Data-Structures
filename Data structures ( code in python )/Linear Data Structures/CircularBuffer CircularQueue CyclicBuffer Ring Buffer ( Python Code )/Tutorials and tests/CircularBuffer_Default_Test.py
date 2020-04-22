class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity

        self.head = 0
        self.tail = 0

        self.items = [None] * self.capacity

    def enqueue(self, item):
        if item == None:
            raise ValueError("The given value is not valid. It is None")

        if self.is_full():
            raise OverflowError("The buffer is full. it can't enqueue any item.")

        self.items[self.tail] = item
        self.tail += 1

        if self.tail == self.capacity:
            self.tail = 0

    def dequeue(self):
        if self.is_empty():
            raise Exception("The buffer is empty. It can't dequeue any items")

        self.items[self.head] = None 
        self.head += 1

        if self.head == self.capacity:
            self.head = 0 

    def is_empty(self):
        return self.items.count(None) == self.capacity - 1

    def is_full(self):
        return None not in self.items

    def getBufferItems(self):
        return self.items

cb = CircularBuffer(7)
print("START  -- > ")
print("HEAD   -- > {0}".format(cb.head))
print("TAIL   -- > {0}".format(cb.tail))
print("Buffer -- > {0}".format(cb.getBufferItems()))

for i in range(3):
    print() 

for charCode in list(range(ord("A"), ord("A") + cb.capacity, 1)):
    cb.enqueue(chr(charCode))

cb.dequeue()
cb.enqueue(False)

for i in range(3):
    print() 

print("END    -- > ")
print("HEAD   -- > {0}".format(cb.head))
print("TAIL   -- > {0}".format(cb.tail))
print("Buffer -- > {0}".format(cb.getBufferItems()))
