def get_by_address(ID):
    if ID == 0:
        return None

    ids = list()

    for gv in tuple(globals().values()):
        if id(gv) == ID:
            ids.append(gv)

    if ids == list():
        return None
    else:
        return ids[0]

class Node(object):
    def __init__(self, data):
        self.data = data
        self.address_store = None
        
        # HSNN = Has Set Near Nodes ( set it to true after using self.setNearNodes )
        self.HSNN = False

    def get_address(self):
        return id(self)

    def setNearNodes(self, prev_node = None, next_node = None):
        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.get_address()

        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.get_address()

        self.address_store = prev_address ^ next_address
        self.HSNN = True

    def getNextNode(self, prev_node):
        if self.address_store is None:
            raise Exception("The node doesn't have an address store, you must set the near nodes first.") 

        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.get_address()
        
        next_node_address = self.address_store ^ prev_address
        return get_by_address(next_node_address)

    def getPrevNode(self, next_node):
        if self.address_store is None:
            raise Exception("The node doesn't have an address store, you must set the near nodes first.") 

        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.get_address()

        prev_node_address = self.address_store ^ next_address
        return get_by_address(prev_node_address)

node1 = Node("A")
node2 = Node("X")

class XORLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        appendNode = Node(data)

        if not self.head:
            self.head = Node(data) 
            self.head.setNearNodes(None, None)
        else:
            self.head.setNearNodes(None, node2)
            print("ASD")

XLL = XORLinkedList()
XLL.append("A")

for i in range(2):
    print()

XLL.append("B")
print("NODE AFTER HEAD -- > {0}".format(XLL.head.getNextNode(None)))

'''
node1 = Node("A")
node2 = Node("B")

node1.setNearNodes(None, None)

print("node1 next -- > {0}".format(node1.getNextNode(None)))
print("node1 prev -- > {0}".format(node1.getPrevNode(None)))

for i in range(3):
    print()

node1.setNearNodes(None, node2)
node2.setNearNodes(node1, None)

print("node1 next -- > {0}".format(node1.getNextNode(None).data))
print("node1 prev -- > {0}".format(node1.getPrevNode(node2)))
print()
print("node2 next -- > {0}".format(node2.getNextNode(node1)))
print("node2 prev -- > {0}".format(node2.getPrevNode(None).data))
'''
