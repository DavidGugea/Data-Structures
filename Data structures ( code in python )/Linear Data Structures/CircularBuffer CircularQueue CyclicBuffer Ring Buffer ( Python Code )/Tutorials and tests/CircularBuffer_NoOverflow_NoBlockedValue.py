class CircularBuffer(object):
    def __init__(self, capacity, storeOverflowedValues = False):
        self.items = list()
    
        # Keep track of the head & tail of the buffer 
        self.head = None
        self.tail = None

        self.storeOverflowedValues = storeOverflowedValues
        self.overflowActive = False
        self.overflowedValues = list()

        self.capacity = capacity

    def enqueue(self, item):
        if self.is_empty():
            self.head = 0
            self.tail = 0

            self.items.insert(self.tail, item)
        else:
            self.tail += 1

            if self.is_full():
                self.overflowActive = True
                
                if self.storeOverflowedValues:
                    self.overflowedValues.append(self.items.tail)

            if self.overflowActive:
                if self.tail == self.capacity:
                    self.tail = 0

                self.items[self.tail] = item
            else:
                self.items.insert(self.tail, item) 

    def dequeue(self):
        self.overflowActive = False
        self.head = 0
        del self.items[self.head]


    def is_empty(self):
        return self.items == list()

    def is_full(self):
        return len(self.items) == self.capacity

    def getBufferItems(self):
        return self.items

cb = CircularBuffer(7)
print("START -- > ")
print(cb.getBufferItems())
print("HEAD -- > {0}".format(cb.head))
print("TAIL -- > {0}".format(cb.tail))

for i in range(3):
    print()

'''
for charCode in list(range(ord("A"), ord("A") + cb.capacity, 1)):
    cb.enqueue(chr(charCode))
'''

'''
cb.enqueue("X")
cb.enqueue("Y")
cb.enqueue("Z")
'''

cb.enqueue("A")
cb.enqueue("B")
cb.enqueue("C")

cb.dequeue()

for i in range(3):
    print()

print("END -- > ")
print(cb.getBufferItems())
print("HEAD -- > {0}".format(cb.head))
print("TAIL -- > {0}".format(cb.tail))
