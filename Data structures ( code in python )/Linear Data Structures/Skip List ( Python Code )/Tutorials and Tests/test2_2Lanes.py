class Node(object):
    def __init__(self, data):
        self.data = data

        self.next = None 

        self.expressLaneUpNode = None
        self.normalLaneDownNode = None

class SkipList(object):
    def __init__(self, skipExpress):
        self.expressLaneHeadNode = None
        self.normalLaneHeadNode = None

        self.counter = 0 
        self.skipExpress = skipExpress 

    def getNodeData(self):
        nodeData = list()

        current_express = self.expressLaneHeadNode 
        expressLaneNodeData = list() 

        while current_express:
            expressLaneNodeData.append(current_express.data) 
            current_express = current_express.next

        current_normal = self.normalLaneHeadNode 
        normalLaneNodeData = list()

        while current_normal:
            normalLaneNodeData.append(current_normal.data)
            current_normal = current_normal.next

        nodeData.append(expressLaneNodeData)
        nodeData.append(normalLaneNodeData)

        return nodeData

    def append(self, data):
        if not self.expressLaneHeadNode and not self.normalLaneHeadNode:
            self.expressLaneHeadNode = Node(data)
            self.normalLaneHeadNode = Node(data)

            self.expressLaneHeadNode.normalLaneDownNode = self.normalLaneHeadNode
            self.normalLaneHeadNode.expressLaneUpNode = self.expressLaneHeadNode
        else:
            currentNL = self.normalLaneHeadNode # currentNL = current normal lane 
            while currentNL.next:
                currentNL = currentNL.next

            currentNL.next = Node(data)

            NEW_NL_NODE = currentNL.next
    
            if self.counter % self.skipExpress == 0:
                currentEN = self.expressLaneHeadNode # currentEN = current express lane
                while currentEN.next:
                    currentEN = currentEN.next

                currentEN.next = Node(data)
                NEW_EL_NODE = currentEN.next

                NEW_NL_NODE.expressLaneUpNode = NEW_EL_NODE
                NEW_EL_NODE.normalLaneDownNode = NEW_NL_NODE 

        # Increment the counter ( for the normal lane )
        self.counter += 1

    def search(self, data):
        # Search in the express lane first
        prev = None
        current = self.expressLaneHeadNode

        current_NL = None

        while current:
            if current.data == data:
                return current.normalLaneDownNode
            elif current.data > data:
                current_NL = prev.normalLaneDownNode
                break
            else:
                prev = current
                current = current.next

        if not current:
            current_NL = prev.normalLaneDownNode

        print("current_NL == > {0}".format(current_NL.data))

        while current_NL:
            if current_NL.data == data:
                return current_NL
            
            current_NL = current_NL.next

        return current_NL

SL = SkipList(5)

def SL_PRINT(i):
    if i <= 9:
        print("Appended {0}  | SL counter -- > {1}".format(i, SL.counter))
    else:
        print("Appended {0} | SL counter -- > {1}".format(i, SL.counter))


for i in range(0, 25):
    SL.append(i)
    SL_PRINT(i)

for i in range(3):
    print()

print(SL.search(23).data)

for i in range(3):
    print()

LANES = SL.getNodeData()

print("EXPRESS LANE -- > {0}".format(LANES[0]))
print("NORMAL LANE  -- > {0}".format(LANES[1]))
