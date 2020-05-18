class Node(object):
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None

        self.counter = 0

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

    def getNodeDictCounter(self):
        NODE_DICT_COUNTER = dict()
        current = self.head

        while current:
            NODE_DICT_COUNTER[current.data] = current.counter
            current = current.next

        return NODE_DICT_COUNTER

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

    def MTF(self, node):
        # MTF = Move To Front
        PREV_NODE = node.prev 
        NEXT_NODE = node.next

        PREV_NODE.next = NEXT_NODE
        NEXT_NODE.prev = PREV_NODE

        self.head.prev = node
        node.next = self.head
        node.prev = None

        self.head = node

    def TM(self, node):
        # TM = Transpose Method ( swap with the previous node )
        node.data, node.counter, node.prev.data, node.prev.counter = node.prev.data, node.prev.counter, node.data, node.counter

    def search(self, data):
        current = self.head

        while current.data != data:
            current = current.next

        current.counter += 1

        if self.head.counter < current.counter:
            self.MTF(current)
        else:
            while current.prev:
                if current.prev:
                    while current.prev.counter < current.counter:
                        self.TM(current)
                        current = current.prev

        return current

SOL = SelfOrganizingList()

def present():
    print(SOL.getNodeData())
    print(SOL.getNodeDictCounter())

    for i in range(2):
        print()

present()

for i in range(1, 5): SOL.append(i)

present()

SOL.search(3)
SOL.search(3)

present()

for i in range(4):
    SOL.search(4)

present()
