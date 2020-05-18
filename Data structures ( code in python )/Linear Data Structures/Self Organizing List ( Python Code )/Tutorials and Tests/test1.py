class Node(object):
    def __init__(self, data):
        self.data = data
        
        ##################
        self.counter = 0 #
                         #
        self.prev = None #
        self.next = None #
        ##################

class SelfOrganizingList(object):
    def __init__(self):
        self.head = None

    def getNodeData(self):
        NODE_DATA_LIST = list()
        current = self.head

        while current:
            NODE_DATA_LIST.append(current.data)
            current = current.next

        return NODE_DATA_LIST

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            
            while current.next:
                current = current.next

            APPEND_NODE = Node(data)

            APPEND_NODE.prev = current
            current.next = APPEND_NODE 
    
    def deleteNode(self, data):
        if not self.head:
            raise ValueError("The self organizing list is empty, we can't delete anything.")
        else:
            current = self.head

            while current.data != data:
                current = current.next

            if current == self.head:
                current.next.prev = None
                self.head = current.next
            else:
                if current.next:
                    current.next.prev = current.prev

                current.prev.next = current.next
    
    def MoveToFront(self, node):
        NEXT_NODE = node.next
        PREV_NODE = node.prev
        
        if NEXT_NODE:
            NEXT_NODE.prev = PREV_NODE
        PREV_NODE.next = NEXT_NODE

        self.head.prev = node
        node.next = self.head

        self.head = node

    def TransposeMethod(self, node):
        node.data, node.counter, node.prev.data, node.prev.counter = node.prev.data, node.prev.counter, node.data, node.counter

    def search(self, data):
        current = self.head

        while current.data != data:
            current = current.next

        current.counter += 1

        if self.head.counter < current.counter:
            self.MoveToFront(current)
        else:
            while current.prev.counter < current.counter:
                self.TransposeMethod(current)
                current = current.prev

    
SOL = SelfOrganizingList()

print(SOL.getNodeData())

for i in range(2):
    print()

SOL.append(1)
SOL.append(2)
SOL.append(3)

print(SOL.getNodeData())

for i in range(2):
    print()

SOL.search(3)
SOL.search(2)
SOL.search(2)
SOL.search(3)

print(SOL.getNodeData())

for i in range(2):
    print()
