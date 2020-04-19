class Queue(object):
    '''
    Operations on Queue:
    Mainly the following four basic operations are performed on queue:
    
    Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
    Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.
    Front: Get the front item from queue.
    Rear: Get the last item from queue.
    '''
    def __init__(self, capacity):
        self.items = list()
        
        self.capacity = capacity
        
        self._front = None
        self._rear = None
        
    def getFront(self):
        return self._front
    
    def getRear(self):
        return self._rear
    
    def enqueue(self, item):
        if len(self.items) == self.capacity:
            raise OverflowError("The queue reached it's maximum capacity of {0} elements.".format(
                self.capacity
            ))
        
        self.items.insert(0, item)
        self._rear = item
        self._front = self.items[-1]
    
    def dequeue(self):
        if not self.items:
            raise ValueError("The queue is empty, can't dequeue anything.")
        
        self._front = self.items[-2]
        return self.items.pop()
    
    def getLength(self):
        return len(self.items)
    
    def is_empty(self):
        return not self.items
    
    def get_queue(self):
        return self.items
    
q = Queue(5)

for i in list(range(1, 6)):
    q.enqueue(i)
    
print(q.get_queue())
print("FRONT -- > {0}".format(q.getFront()))
print("REAR  -- > {0}".format(q.getRear()))

for i in range(3):
    print()
    
q.dequeue()
print(q.get_queue())
print("FRONT -- > {0}".format(q.getFront()))
print("REAR  -- > {0}".format(q.getRear()))