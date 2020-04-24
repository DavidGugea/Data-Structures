class CircularBuffer(object):
    ''' FIFO Buffer ( my code )'''
    def __init__(self, capacity, blockDefaultValue = None):
        self.items = [blockDefaultValue]*capacity 

        # Index indicators
        self.tail = None
        self.head = None
        self.capacity = capacity 

        self.blockDefaultValue = blockDefaultValue

    def enqueue(self, item):
        if item == self.blockDefaultValue:
            raise ValueError("The item that you want to add it's the same as the block default value. You can only add items that are not the same as the block default value.")

        if self.is_empty():
            self.tail = 0
            self.items[0] = item

            if not self.head:
                self.head = self.tail
        elif not self.is_full():
            blockedValueIndex = self.items.index(self.blockDefaultValue)

            self.items[blockedValueIndex] = item
            self.tail = blockedValueIndex
        else:
            raise OverflowError("The buffer has reached it's maximum capacity.It can't enqueue any item")

    def dequeue(self):
        if self.is_empty():
            raise Exception("The buffer is empty. It can't dequeue any item")

        self.items[self.head] = self.blockDefaultValue
        self.head += 1

        if self.head >= self.capacity:
            self.head = 0

    def is_empty(self):
        return self.items.count(self.blockDefaultValue) == self.capacity 

    def is_full(self):
        return self.blockDefaultValue not in self.items

    def getBufferData(self):
        return self.items

    def getTail(self):
        return { self.tail : self.items[self.tail] }
    
    def getHead(self):
        return { self.head : self.items[self.head] }

cb = CircularBuffer(7)
print("START -- >")
print("Buffer data -- > {0}".format(cb.getBufferData()))
print("HEAD -- > {0}".format(cb.head))
print("TAIL -- > {0}".format(cb.tail))

print("is_empty -- > {0}".format(cb.is_empty()))
print("is_full -- > {0}".format(cb.is_full()))

for i in range(3):
    print()

for charCode in list(range(ord("A"), ord("A") + cb.capacity, 1)):
    cb.enqueue(chr(charCode))

cb.dequeue()
cb.enqueue("X")

for i in range(3):
    cb.dequeue()

cb.enqueue("Y")
cb.enqueue("Z")

for i in range(3):
    print()

print("END -- >")
print("Buffer data -- > {0}".format(cb.getBufferData()))
print("HEAD -- > {0}".format(cb.head))
print("TAIL -- > {0}".format(cb.tail))
print("is_empty -- > {0}".format(cb.is_empty()))
print("is_full -- > {0}".format(cb.is_full())) 
