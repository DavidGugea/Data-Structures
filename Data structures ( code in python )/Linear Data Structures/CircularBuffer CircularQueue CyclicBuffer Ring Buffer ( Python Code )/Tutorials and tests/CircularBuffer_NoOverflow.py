class CircularBuffer_NoOverflow(object):
    '''
        https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html
        ( my code + website code )
    '''
    def __init__(self, capacity, blockedDefaultValue = None, storeOverflowedValues = False):
        # Blocked default value & capacity
        self.blockedDefaultValue = blockedDefaultValue
        self.capacity = capacity

        # Check the overflowed values ( store them in a list or not )
        self.overflowedValues = list()
        self.overflowActive = False
        self.storeOverflowedValues = storeOverflowedValues

        # Index pointers
        self.tail = None
        self.head = None

        # Items
        self.items = [self.blockedDefaultValue] * self.capacity

    def enqueue(self, item):
        if item == self.blockedDefaultValue:
            raise ValueError("The given item is equal to the blocked default value. The item can't be anything but that. Try again.")

        if self.is_empty():
            self.tail = self.head = 0
            self.items[self.tail] = item
        else:
            self.tail += 1
        
            if self.tail == self.capacity:
                # Change the tail to be the first item in the list in case that the buffer exceeds it's capacity. Therefore there is not overflow error possible. The buffer will overwrite the first item. After that, it will be 0. It can increase after that in 1, 2 etc. But it will overwrite the values in the buffer, it will not append or insert anything to the buffer. 
                self.tail = 0

                # Active the 'overflow'. That means that the buffer reached it's maximum capacity but we continued adding items to it. So it will have to replace those values with the new items that we want to add. By setting the property 'overflowActive' to True, in case that the user chose to store the replace / overflowed values in a list, we will add all the replaced values in a list, otherwise we will just replace the values and move on 
                self.overflowActive = True
        
            replacedValue = self.items[self.tail]
            self.items[self.tail] = item

            if self.overflowActive and self.storeOverflowedValues:
                self.overflowedValues.append(replacedValue)

    def dequeue(self):
        if self.is_empty():
            raise Exception("The buffer is empty, we can't dequeue any items")
        
        self.items[self.head] = self.blockedDefaultValue
        self.head += 1


    def is_empty(self):
        return self.items == [self.blockedDefaultValue] * self.capacity

    def reachedCapacity(self):
        return self.blockedDefaultValue not in self.items

    def getItems(self):
        return self.items

    def getOverflowedValues(self):
        if self.storeOverflowedValues:
            return self.overflowedValues
        else:
            raise Exception("In order to get the overflowed values of the buffer you must change the storeOverflowedValues property from the constructor to be True, otherwise, no values will be stored.")

    def clearOverflowedValues(self):
        if self.storeOverflowedValues:
            self.overflowedValues = list()
        else:
            raise Exception("In order to clear the overflowed / replaced values from the buffer, you must chagne the storeOverflowedValues property from the constructor to be True, otherwise no values can be cleared.") 

cb = CircularBuffer_NoOverflow(7, storeOverflowedValues = True)
print("START -- > ")
print("Buffer items -- > {0}".format(cb.getItems()))
print("Tail -- > {0}".format(cb.tail))
print("Head -- > {0}".format(cb.head))
print("OVERFLOWED VALUES -- > {0}".format(cb.getOverflowedValues()))

for i in range(3):
    print()

##############################################################

for charCode in list(range(ord("A"), ord("A") + cb.capacity, 1)):
    cb.enqueue(chr(charCode))

cb.enqueue("X")
cb.enqueue("Y")
cb.enqueue("Z")

for i in range(cb.capacity):
    cb.dequeue()

##############################################################

for i in range(3):
    print()

print("END -- > ")
print("Buffer items -- > {0}".format(cb.getItems()))
print("Tail -- > {0}".format(cb.tail))
print("Head -- > {0}".format(cb.head))
print("OVERFLOWED VALUES -- > {0}".format(cb.getOverflowedValues()))
