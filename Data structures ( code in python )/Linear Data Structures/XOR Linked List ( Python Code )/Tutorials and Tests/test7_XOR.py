IDS = { 0 : None } 

def getByAddress(S_ID):
    if S_ID in IDS.keys(): return IDS[S_ID]
    else: raise ValueError("ID not found in IDS dict.") 

class Node(object):
    def __init__(self, data):
        self.data = data
        self.store_address = None
   
    def getAddress(self):
        return id(self)

    def setNearNodes(self, prev_node, next_node):
        if prev_node:
            IDS[id(prev_node)] = prev_node
        if next_node:
            IDS[id(next_node)] = next_node
    
        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.getAddress()

        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.getAddress()

        self.store_address = prev_address ^ next_address

    def getNextNode(self, prev_node):
        if self.store_address == None:
            raise Exception("The node doens't have a store address. Hence it can't find the next node. Make sure you set the near nodes first.") 

        if prev_node == None:
            prev_address = 0 
        else:
            prev_address = prev_node.getAddress()

        next_node_address = self.store_address ^ prev_address
        return getByAddress(next_node_address)

    def getPrevNode(self, next_node):
        if self.store_address == None:
            raise Exception("The node doens't have a store address. Hence it can't find the next node. Make sure you set the near nodes first.") 

        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.getAddress()

        prev_node_address = self.store_address ^ next_address
        return getByAddress(prev_node_address)

class XORLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        appendNode = Node(data)
        print("NEW APPEND NODE ( data : {0} ) ( ID : {1} )".format(data, id(appendNode)))
        IDS[id(appendNode)] = appendNode

        if self.head == None:
            self.head = appendNode
            self.head.setNearNodes(None, None)
        else:
            prev = None
            current = self.head

            while current.getNextNode(prev):
                temp = current
                current = current.getNextNode(prev)
                prev = temp
            
            current.setNearNodes(prev, appendNode)
            appendNode.setNearNodes(current, None)


XLL = XORLinkedList()

print(XLL.head)

for i in range(2):
    print()

XLL.append("A")
XLL.append("B")
XLL.append("C")

print("HEAD NEXT NODE -- > {0}".format(XLL.head.getNextNode(None).data))
