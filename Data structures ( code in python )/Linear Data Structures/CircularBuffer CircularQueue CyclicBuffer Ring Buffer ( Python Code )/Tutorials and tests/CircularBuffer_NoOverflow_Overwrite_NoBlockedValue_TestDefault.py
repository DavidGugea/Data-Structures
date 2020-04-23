class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity

        self.head = -1
        self.tail = -1

        self.items = [None] * self.capacity
        self.fullRotation = False 

    def is_empty(self):
        return self.head == -1 and self.tail == -1

    def getBufferItems(self):
        return self.items 

    def enqueue(self, item):
        if self.head == -1:
            self.head = 0
            
        self.tail += 1

        if self.tail == self.capacity:
            self.fullRotation = True
            self.tail = 0

        self.items[self.tail] = item

    def dequeue(self):
        self.items[self.head] = None

        self.head += 1
        if self.head == self.capacity:
            self.head = 0
    
cb = CircularBuffer(7)
print("START -- > ")
print("IS_EMPTY -- > {0}".format(cb.is_empty()))
print("HEAD -- > {0}".format(cb.head))
print("TAIL -- > {0}".format(cb.tail))
print("ITEMS -- > {0}".format(cb.items))
print("< -- START ")

for i in range(3):
    print()

cb.enqueue("A")
cb.enqueue("B")
cb.enqueue("C")
cb.enqueue("D")
cb.enqueue("E")
cb.enqueue("F")
cb.enqueue("G")

cb.dequeue()

cb.enqueue("X")
cb.enqueue("Y")

for i in range(3):
    print()

print("END -- > ")
print("IS_EMPTY -- > {0}".format(cb.is_empty()))
print("HEAD -- > {0}".format(cb.head))
print("TAIL -- > {0}".format(cb.tail))
print("ITEMS -- > {0}".format(cb.items))
print("< -- END ")
