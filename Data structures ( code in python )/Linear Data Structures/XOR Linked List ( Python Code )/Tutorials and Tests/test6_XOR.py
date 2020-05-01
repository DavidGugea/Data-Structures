GLOBALS = dict()

def getByAddress(S_ID):
    # S_ID => search ID
    if S_ID == 0:
        return None

    for gVar in tuple(GLOBALS.values()):
        if id(gVar) == S_ID:
            return gVar

    return None

class Node(object):
    def __init__(self, data):
        self.data = data
        self.store_address = None

    def getAddress(self):
        return id(self)

    def setNearNodes(self, prev_node, next_node):
        if prev_node == None:
            prev_address = 0 
        else:
            prev_address = prev_node.getAddress()
    
        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.getAddress()
        
        '''
        print("~ setting up store address for node with data : {0} ~".format(self.data))
        print()
        print("SELF ID      - > {0}".format(self.getAddress()))
        print("prev_address - > {0}".format(prev_address))
        print("next_address - > {0}".format(next_address))
        '''

        self.store_address = prev_address ^ next_address

        # print("self.store_address = prev_address ^ next_address = {0} ^ {1} = {2}".format(prev_address, next_address, self.store_address))

    def getNextNode(self, prev_node):
        if self.store_address == None:
            raise Exception("The XOR Linked List doesn't have any store address. Hence it can't find the next node. Make sure you set the near nodes first.") 

        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.getAddress()


        print("< Trying to reach for the next node ( NODE DATA : {0} ) ~ >".format(self.data)) 
        print()
        print("SELF ID              == > {0}".format(self.getAddress()))
        print("self.store_address   == > {0}".format(self.store_address))
        print("prev_address         == > {0}".format(prev_address))

        # self.store_address ^ prev_address = next_address ^ prev_address ^ prev_address = next_address ^ 0 = next_address 
        next_node_address = self.store_address ^ prev_address
        
        print("next_node_address = self.store_address ^ prev_address = {0} ^ {1} = {2}".format(
            self.store_address,
            prev_address,
            next_node_address
        ))

        return getByAddress(next_node_address)

    def getPrevNode(self, next_node):
        if self.store_address == None:
            raise Exception("The XOR Linked List doesn't have any store address. Hence it can't find the next node. Make sure your set the near nodes first.")

        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.getAddress()

        prev_node_address = self.store_address ^ next_address

        return getByAddress(prev_node_address)


class XORLinkedList(object):
    def __init__(self):
        self.head = None
        self.c = 0

    def append(self, data):
        appendNode = Node(data)
        GLOBALS[appendNode] = id(appendNode) 

        if self.head == None:
            self.head = appendNode
            self.head.setNearNodes(None, None)
            self.c += 1
        else:
            if self.c >= 2:
                print("< ------------------------- >")
                for i in range(10):
                    print()


                print(list(map(id, globals().values())))

                print(self.head.getNextNode(None))
                print(self.head.store_address)
            else:
                prev = None
                current = self.head

                while current.getNextNode(prev):
                    temp = current
                    current = current.getNextNode(prev)
                    prev = temp

                current.setNearNodes(prev, appendNode) # SA = id(appendNode) 
                appendNode.setNearNodes(current, None) # SA = id(HEAD)

            self.c += 1


XLL = XORLinkedList()

print(XLL.head)

for i in range(3):
    print()

XLL.append("A")

print("HEAD -- > {0}".format(XLL.head.data))

for i in range(3):
    print()

XLL.append("B")

print("HEAD NEXT NODE -- > {0}".format(XLL.head.getNextNode(None).data))
print(XLL.c)

XLL.append("X")
