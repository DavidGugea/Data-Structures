class Queue(object):
    def __init__(self):
        self.items = list()

        self.rear = None
        self.front = None

    def enqueue(self, item):
        self.items.insert(0, item)
        self.rear = item

    def dequeue(self):
        if self.items:
            self.front = self.items[-2]
            del self.items[-1]
        else:
            raise ValueError("Queue empty, can't delete anything.")
    
    def is_empty(self):
        return not self.items

    def getFront(self):
        return self.front

    def getRear(self):
        return self.rear

    def getQueue(self):
        return self.items
