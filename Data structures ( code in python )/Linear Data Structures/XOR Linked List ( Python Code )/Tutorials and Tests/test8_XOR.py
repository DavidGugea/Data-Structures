IDS = { 0 : None }

def getByAddress(S_ID):
    if S_ID in IDS.keys(): return IDS[S_ID]
    else: raise ValueError("The search id couldn't be found in IDS dict.") 

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
            raise Exception("The node doesn't have any store address. Hence it can't find the next node. Make sure you set the near nodes first.")

        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.getAddress()
        
        next_node_address = self.store_address ^ prev_address
        return getByAddress(next_node_address)

    def getPrevNode(self, next_node):
        if self.store_address == None:
            raise Exception("The node doesn't have any store address. Hence it can't find the next node. Make sure you set the near nodes first.")

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

    def delete(self, data):
        if self.head == None: raise ValueError("The XOR Linked List doesn't have a head node. You must first add nodes in the linked list in order to be able to delete something.") 

        if data == self.head.data:
            nextAfterHead = self.head.getNextNode(None)
            nextAfterHead.setNearNodes(None, nextAfterHead.getNextNode(self.head))
            self.head.setNearNodes(None, None)
            
            temp = self.head
            self.head = nextAfterHead

            temp = None 
        else:
            prev = None
            current = self.head

            while current.data != data:
                temp = current 
                current = current.getNextNode(prev)
                prev = temp

                if current == None:
                    raise ValueError("The given data couldn't be found in the XOR Linked List.")

            nextNode = current.getNextNode(prev)
            if nextNode:
                nextNode.setNearNodes(prev, nextNode.getNextNode(current))
            prev.setNearNodes(prev.getPrevNode(current), nextNode)
            
            current = None

    def nodeData(self):
        if self.head == None: return list()
        nodeDataList = [self.head.data] 

        prev = None
        current = self.head

        while current.getNextNode(prev):
            temp = current
            current = current.getNextNode(prev)
            prev = temp

            nodeDataList.append(current.data)
       
        return nodeDataList

XLL = XORLinkedList()

for charCode in list(range(ord("A"), ord("A") + 26)):
    XLL.append(chr(charCode))

print("NODE DATA LIST -- > {0}".format(XLL.nodeData()))

