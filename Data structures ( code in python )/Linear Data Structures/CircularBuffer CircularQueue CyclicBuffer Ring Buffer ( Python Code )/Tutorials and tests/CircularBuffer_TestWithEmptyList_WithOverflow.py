class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity

        self.head = 0
        self.tail = -1

        self.items = list()

    def is_empty(self):
        return self.items == list()

    def is_full(self):
        return len(self.items) == self.capacity

    def getBufferItems(self):
        return self.items

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("The buffet is full. It can't enqueue any items.")
        
        self.tail += 1
        self.items.insert(self.tail, item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("The buffer is empty. It can't dequeue any items.")

        self.head += 1
        del self.items[0]

        if self.head == self.capacity:
            self.head = 0

cb = CircularBuffer(7)
print("START -- > ")
print("HEAD -- > {0}".format(cb.head))
print("TAIL -- > {0}".format(cb.tail))
print("ITEMS -- {0}".format(cb.getBufferItems()))
print("< -- START")

for i in range(3):
    print()

for charCode in list(range(ord("A"), ord("A") + cb.capacity, 1)):
    cb.enqueue(chr(charCode))

cb.dequeue()

for i in range(3):
    print()

print("END -- > ")
print("HEAD -- > {0}".format(cb.head))
print("TAIL -- > {0}".format(cb.tail))
print("ITEMS -- > {0}".format(cb.items))
print("< -- END")
