class Deque(object):
    def __init__(self, capacity = None, input_restriction = None, output_restriction = None):
        '''
        if capacity is None, then the deque has no capacity. Hence we are allowed to add as many items as we want. If it's not None and it's a number, that is the maximum capacity that the deque can reach 
        '''
        
        # Check the capacity
        if capacity is not None:
            if type(capacity) != int:
                raise ValueError("The capacity must be either None, which means that the deque doesn't have a capacity, or it must be a number which will indicate the maximum capacity that the deque can have.")
        self.capacity = capacity

        if input_restriction != None and input_restriction != 'front' and input_restriction != 'rear':
            raise Exception("The input restriction represents one end where you won't be allowed to add items. Hence it must be front, rear or None in case that there is no input restriction and both ends can be used like in a default dequeue")
        if output_restriction != None and output_restriction != 'front' and output_restriction != 'rear':
            raise Exception("The output restriction represents one end where you won't be allowed to delete items. Hence it must be front, rear or None in case that there is no output restriction and you can delete items from both ends like in a default dequeue")

        # Create the items list.
        self.items = list()

        # Create the front & rear index indicators. By default, rear is 0 & front is -1
        self.front = -1 
        self.rear = 0

        self.input_restriction = input_restriction
        self.output_restriction = output_restriction

    def getSize(self):
        return len(self.items) 

    def __len__(self):
        return len(self.items) 

    def __str__(self):
        return str(self.items)

    def peek(self):
        if self.isEmpty():
            raise Exception("The dequeue is empty.")

        return self.items[-1]

    def peekLeft(self):
        if self.isEmpty():
            raise Exception("The dequeue is empty.")

        return self.items[0]

    def isFull(self):
        if self.capacity == None:
            return None
        return len(self.items) == self.capacity

    def isEmpty(self):
        return not self.items

    def insertAtFront(self, item):
        if self.input_restriction == "front":
            raise Exception("There is an input restriction on the front")

        if self.capacity:
            if len(self.items) == self.capacity:
                raise Exception("The deque is full")

        self.front += 1
        self.items.append(item)

    def insertAtRear(self, item):
        if self.input_restriction == "rear":
            raise Exception("There is an input restriction on the rear")

        if self.capacity:
            if len(self.items) == self.capacity:
                raise Exception("The deque is full")

        self.items.insert(0, item)

    def deleteFromFront(self):
        if self.output_restriction == "front":
            raise Exception("There is an output restriction on the front")

        if self.isEmpty():
            raise Exception("The dequeue is empty.")

        self.front -= 1
        return self.items.pop()

    def deleteFromRear(self):
        if self.output_restriction == "rear":
            raise Exception("There is an output restriction on the rear")

        if self.isEmpty():
            raise Exception("The dequeue is empty.")

        firstItem = self.items[0]
        del self.items[0]
        
        return firstItem
