class Deque(object):
    def __init__(self, capacity = None):
        '''
        if capacity is None, then the deque has no capacity. Hence we are allowed to add as many items as we want. If it's not None and it's a number, that is the maximum capacity that the deque can reach 
        '''
        
        # Check the capacity
        if capacity is not None:
            if type(capacity) != int:
                raise ValueError("The capacity must be either None, which means that the deque doesn't have a capacity, or it must be a number which will indicate the maximum capacity that the deque can have.")
        self.capacity = capacity

        # Create the items list.
        self.items = list()

        # Create the front & rear index indicators. By default, rear is 0 & front is -1
        self.front = -1 
        self.rear = 0

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
        if self.capacity:
            if len(self.items) == self.capacity:
                raise Exception("The deque is full")

        self.front += 1
        self.items.append(item)

    def insertAtRear(self, item):
        if self.capacity:
            if len(self.items) == self.capacity:
                raise Exception("The deque is full")

        self.items.insert(0, item)

    def deleteFromFront(self):
        if self.isEmpty():
            raise Exception("The dequeue is empty.")

        self.front -= 1
        return self.items.pop()

    def deleteFromRear(self):
        if self.isEmpty():
            raise Exception("The dequeue is empty.")

        firstItem = self.items[0]
        del self.items[0]
        
        return firstItem
