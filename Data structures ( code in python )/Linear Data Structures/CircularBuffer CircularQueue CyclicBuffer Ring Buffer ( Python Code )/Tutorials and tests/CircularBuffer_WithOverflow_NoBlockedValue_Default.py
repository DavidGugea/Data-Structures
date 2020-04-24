class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity

        self.head = -1
        self.tail = -1

        self.items = [None] * self.capacity

    def is_empty(self):
        return self.head == -1 and self.tail == -1 

    def is_full(self):
        return ( self.tail == self.head - 1 ) or ( self.tail == self.capacity - 1 and self.head == 0 )

    def getBufferItems(self):
        return self.items

    def getPartitionItems(self):
        if self.head <= self.tail:
            return self.items[self.head : self.tail + 1]
        else:
            return self.items[self.head:] + self.items[:self.tail + 1] 

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("The buffer is full. It can't enqueue any other items.")

        if self.head == -1:
            self.head = 0

        self.tail += 1

        if self.tail == self.capacity:
            self.tail = 0

        self.items[self.tail] = item

    def dequeue(self):
        self.items[self.head] = None
        self.head += 1

cb = CircularBuffer(7)
print("START -- > ")
print("HEAD -- > {0}".format(cb.head))
print("TAIL -- > {0}".format(cb.tail))
print("ITEMS -- > {0}".format(cb.getBufferItems()))
print("< -- START")

for i in range(3):
    print()

print("IS_EMPTY -- > {0}".format(cb.is_empty()))
print("IS_FULL  -- > {0}".format(cb.is_full()))
print()

print("IS_EMPTY -- > {0}".format(cb.is_empty()))
print("IS_FULL  -- > {0}".format(cb.is_full()))

for i in range(3):
    print()

print("END -- > ")
print("HEAD -- > {0}".format(cb.head))
print("TAIL -- > {0}".format(cb.tail))
print("ITEMS -- > {0}".format(cb.getBufferItems()))
print("PARTITION ITEMS -- > {0}".format(cb.getPartitionItems()))
print("< -- END")
