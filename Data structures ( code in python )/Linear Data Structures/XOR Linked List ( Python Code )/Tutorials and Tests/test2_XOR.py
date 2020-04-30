def getByAddress(S_ID):
    # S_ID = Search ID
    if S_ID == 0:
        return None

    for gvar in tuple(globals().values()):
        if id(gvar) == S_ID:
            return gvar 
        
    return None

class Node(object):
    def __init__(self, data):
        self.data = data
        self.store_address = None

    def getNodeAddress(self):
        return id(self)

    def setNearNodes(self, prev_node = None, next_node = None):
        if prev_node is None:
            prev_address = 0
        else:
            prev_address = prev_node.getNodeAddress()

        if next_node is None:
            next_address = 0
        else:
            next_address = next_node.getNodeAddress()
    
        self.store_address = prev_address ^ next_address

    def getNextNode(self, prev_node):
        if self.store_address is None:
            raise Exception("The node doesn't have a store address. Set the near nodes first.")

        if prev_node is None:
            prev_address = 0
        else:
            prev_address = prev_node.getNodeAddress()

        next_node_address = self.store_address ^ prev_address
        return getByAddress(next_node_address)
    
    def getPrevNode(self, next_node):
        if self.store_address is None:
            raise Exception("The node doens't have a store address. Set the near nodes first") 

        if next_node is None:
            next_address = 0
        else:
            next_address = next_node.getNodeAddress()

        prev_node_address = self.store_address ^ next_address
        return getByAddress(prev_node_address)

class XORLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        # global appendNode will put the appendNode in globals().values() so when we will search for its ID it will be there
        global appendNode
        appendNode = Node(data)

        if not self.head:
            self.head = appendNode 
            # The head node doesn't have any neighbours by default 
            self.head.setNearNodes(None, None)
        else:
            prev = None
            current = self.head

            print("BEFORE WHILE LOOP -- > {0}".format(current.getNextNode(prev)))

            while current.getNextNode(prev):
                temp = current
                current = current.getNextNode(prev)
                prev = temp
                print("NEXT NODE STOP OR NOT -- > {0}".format(current.getNextNode(prev)))

            print("Current is head -- > {0}".format(current is self.head))
            print("curret data -- > {0}".format(current.data))

            current.setNearNodes(prev, appendNode)
            appendNode.setNearNodes(current, None)

    def getNodeList(self):
        nodeList = list()

        prev = None
        current = self.head

        while current:
            nodeList.append(current.data)
            
            temp = current
            current = current.getNextNode(prev)
            prev = temp

        return nodeList

XLL = XORLinkedList()

'''
print(XLL.head)
if XLL.head:
    print(XLL.head.store_address)
else:
    print("XLL.head is None. Hence it doesn't have a store address")
'''

for i in range(5):
    print()

node1_add = Node("B")
node2_add = Node("C")

print(XLL.head)
XLL.append("A")
print(XLL.head.data)
print()

XLL.append("B")
print(XLL.head.getNextNode(None).data)

for i in range(5):
    print()

XLL.append("C")
print(XLL.head.getNextNode(None).data) 

for i in range(5):
    print()
'''
print("HEAD                   -- > {0}".format(XLL.head))
if XLL.head:
    print("HEAD STORE ADDRESS     -- > {0}".format(XLL.head.store_address))
else:
    print("XLL.head is None. Hence it doesn't have a store address")

print("NODE AFTER HEAD        -- > {0}".format(XLL.head.getNextNode(None).data))
'''

print("NODE LIST -- > {0}".format(XLL.getNodeList()))

'''
node1 = Node("A")
node2 = Node("B")

node1.setNearNodes(None, node2)
node2.setNearNodes(node1, None)

print("NODE1 -- > ")
print("~ NEXT : ~")
print(node1.getNextNode(None).data)
print("~ PREV : ~")
print(node1.getPrevNode(node2))

for i in range(3):
    print()

print("NODE2 -- > ")
print("~ NEXT : ~")
print(node2.getNextNode(node1))
print("~ PREV : ~")
print(node2.getPrevNode(None).data)
'''
