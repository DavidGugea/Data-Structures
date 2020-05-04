class Node(object):
    def __init__(self, data):
        self.data = data

        self.next = None
        self.expressLane_next = None

class SkipList(object):
    def __init__(self, skipCounter):
        self.head = None

        self.skipCounter = skipCounter
        self.counter = 0

    def updateExpressLane(self, node):
        current = self.head

        while current.expressLane_next:
            current = current.expressLane_next

        current.expressLane_next = node

    def getNodeData(self):
        nodeData = list()

        current = self.head
        NL_LIST = list() # NL_LIST = normal lane list

        while current:
            NL_LIST.append(current.data)
            current = current.next

        current = self.head
        EL_LIST = list() # EL_LIST = express lane list

        while current:
            EL_LIST.append(current.data)
            current = current.expressLane_next

        nodeData.append(EL_LIST)
        nodeData.append(NL_LIST)

        return nodeData

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            appendNode = Node(data)

            current = self.head
            while current.next:
                current = current.next

            current.next = appendNode
            
            if self.counter % self.skipCounter == 0:
                self.updateExpressLane(appendNode)

        # Increment the counter
        self.counter += 1

    def search(self, data):
        # Look in the express lane first
        prev = None
        current = self.head
        NEXT_NL_NODE = None
        
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                NEXT_NL_NODE = prev
                break
            else:
                prev = current
                current = current.expressLane_next

        if not current:
            NEXT_NL_NODE = prev

        while NEXT_NL_NODE:
            NEXT_NL_NODE = NEXT_NL_NODE.next
            
            if NEXT_NL_NODE.data == data:
                return NEXT_NL_NODE

        raise ValueError("The given data couldn't be found in the skip list.")

SL = SkipList(5)

for i in range(1, 16):
    SL.append(i)

for i in range(3):
    print()

print(SL.search(2).data)
        
for i in range(3):
    print()

LANES = SL.getNodeData()

print("EXPRESS LANE -- > {0}".format(LANES[0]))
print("NORMAL LANE  -- > {0}".format(LANES[1]))
