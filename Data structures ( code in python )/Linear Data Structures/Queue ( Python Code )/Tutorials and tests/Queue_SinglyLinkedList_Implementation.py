class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue(object):
    def __init__(self):
        self.rear = None # Last node that was put in the queue
        self.front = None # First node that was put in the queue
        
        self.nodeDataList = list()
        
    def enqueue(self, item):
        enqueueNode = Node(item)
        
        if not self.rear or not self.front:
            self.rear = self.front = enqueueNode
            return
        
        enqueueNode.next = self.rear
        self.rear = enqueueNode
        
    def dequeue(self):
        if not self.front:
            raise ValueError("The queue is empty, you can't dequeue nothing from it.")
        
        prev = None
        current = self.rear
        while current.next:
            prev = current
            current = current.next
            
        prev.next = None
        return current
    
    def is_empty(self):
        return not self.rear or not self.front
    
    def getNodeDataList(self):
        nodeDataList = list()
        
        current = self.rear
        
        while current:
            nodeDataList.append(current.data)
            current = current.next
            
        return nodeDataList
    
q = Queue()
print("Queue empty -- > {0}".format(q.is_empty()))
q.enqueue('a')
q.enqueue('b')
q.dequeue()
print("Queue empty -- > {0}".format(q.is_empty()))
print(q.getNodeDataList())