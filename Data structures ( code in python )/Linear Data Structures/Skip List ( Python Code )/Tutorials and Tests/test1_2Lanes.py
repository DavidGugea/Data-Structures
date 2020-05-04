import pprint

class Node(object):
    def __init__(self, data):
        # Data of node
        self.data = data
        
        # Next pointer 
        self.next = None
        
        # Upper pointer to node on express lane 
        self.expressLaneUpNode = None

        # Down pointer to node on normal lane
        self.normalLaneDownNode = None

class SkipList(object):
    def __init__(self):
        self.normalLaneHeadNode = None
        self.expressLaneHeadNode = None

        self.skipSpacing = 5
        self.counter = 0

    def getLanesNodeData(self):
        lanesNodeDataInfo = list()
        
        current_normalLane = self.normalLaneHeadNode
        normalLane_NodeData = list()

        while current_normalLane:
            normalLane_NodeData.append(current_normalLane.data)
            current_normalLane = current_normalLane.next
        
        current_expressLane = self.expressLaneHeadNode
        expressLane_NodeData = list()

        while current_expressLane:
            expressLane_NodeData.append(current_expressLane.data)
            current_expressLane = current_expressLane.next
        
        lanesNodeDataInfo.append(normalLane_NodeData)
        lanesNodeDataInfo.append(expressLane_NodeData)

        return lanesNodeDataInfo


    def append(self, data):
        appendNode = Node(data)
        
        if not self.normalLaneHeadNode and not self.expressLaneHeadNode:
            '''
                # Upper pointer to node on express lane 
                self.expressLaneUpNode = None

                # Down pointer to node on normal lane
                self.normalLaneDownNode = None
            '''

            self.normalLaneHeadNode = Node(data) 
            self.expressLaneHeadNode = Node(data) 

            self.normalLaneHeadNode.expressLaneUpNode = self.expressLaneHeadNode
            self.expressLaneHeadNode.normalLaneDownNode = self.normalLaneHeadNode
        else:
            # Append on normal lane
            currentNormal = self.normalLaneHeadNode
            while currentNormal.next:
                currentNormal = currentNormal.next
            
            currentNormal.next = appendNode
            NEW_NODE_NormalLane = currentNormal.next
            
            if self.counter % self.skipSpacing == 0:
                print("NEW EXPRESS NODE ADDED -- > self.counter ( {0} ) % self.skipSpacing ( {1} ) = {2}".format(self.counter, self.skipSpacing, self.counter % self.skipSpacing))

                # Append on express lane
                currentExpress = self.expressLaneHeadNode

                while currentExpress.next:
                    currentExpress = currentExpress.next
                
                currentExpress.next = appendNode
                
                NEW_NODE_ExpressLane = currentExpress.next

                NEW_NODE_NormalLane.expressLaneUpNode = NEW_NODE_ExpressLane
                NEW_NODE_ExpressLane.normalLaneDownNode = NEW_NODE_NormalLane

        # Increment the node counter
        self.counter += 1

    def search(self, SD): # SD = > Search data 
        # Start search on the express lane
        prev = None
        current = self.expressLaneHeadNode
        
        while current:
            if current.data == SD:
                return current.normalLaneDownNode
            elif current.data > SD:
                break

            prev = current
            current = current.next

        print("PREV     -- > {0}".format(prev.data))
        print("CURRENT  -- > {0}".format(current.data))

SL = SkipList()

for i in range(1, 8):
    SL.append(i)


# print("-- > {0}".format(SL.expressLaneHeadNode.next.normalLaneDownNode.next.data))
print("SL counter -- > {0}".format(SL.counter))
# print(SL.expressLaneHeadNode.next.next.data)

for i in range(3):
    print()

# print(SL.search())

for i in range(3):
    print()

SL_LANES = SL.getLanesNodeData()
print("EXPRESS LANE -- > {0}".format(SL_LANES[1]))
print("NORMAL LANE  -- > {0}".format(SL_LANES[0]))
