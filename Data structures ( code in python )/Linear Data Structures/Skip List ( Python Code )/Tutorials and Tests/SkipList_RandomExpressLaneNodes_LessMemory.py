import random

class Node(object):
    def __init__(self, data):
        self.data = data

        self.next = None
        self.expressLane_next = None

class SkipList(object):
    def __init__(self):
        self.head = None

    def getNodeData(self):
        nodeList = list()

        current = self.head
        NL_LIST = list() # NL => normal node list

        while current:
            NL_LIST.append(current.data)
            current = current.next

        current = self.head
        EL_LIST = list() # EL => express node list

        while current:
            EL_LIST.append(current.data)
            current = current.expressLane_next

        nodeList.append(EL_LIST)
        nodeList.append(NL_LIST)

        return nodeList
                
    def updateNode(self, node):
        current = self.head

        while current.expressLane_next:
            current = current.expressLane_next

        current.expressLane_next = node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            appendNode = Node(data)

            current = self.head

            while current.next:
                current = current.next

            current.next = appendNode
            NEW_NL_NODE = current.next 

            randomExpress = random.randint(1, 100)

            if randomExpress % 6 == 0:
                self.updateNode(NEW_NL_NODE)

    def search(self, data):
        # Search the express lane first
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

SL = SkipList()

for i in range(1, 36):
    SL.append(i)

for i in range(3):
    print()

print(SL.search(4).data)

for i in range(3):
    print()

LANES = SL.getNodeData()

print("EXPRESS LANE -- > {0}".format(LANES[0]))
print("NORMAL LANE  -- > {0}".format(LANES[1]))
