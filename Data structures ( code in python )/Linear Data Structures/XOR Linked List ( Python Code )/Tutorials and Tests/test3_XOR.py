def get_object_by_addressID(S_ID):
    # S_ID = > search ID

    # If S_ID is 0 -> return None 
    if S_ID == 0: 
        return None

    # Search for all the global vales in the globals() & for their ID's - > return them when S_ID is found  
    for global_var in tuple(globals().values()):
        if id(global_var) == S_ID:
            return global_var
    
    # If nothing was found, return None
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
            raise Exception("The node doesn't have a store address. Hence it can't find the next node. Make sure you set the near nodes first.")

        if prev_node is None:
            prev_address = 0
        else:
            prev_address = prev_node.getNodeAddress()

        next_node_address = self.store_address ^ prev_address
        return get_object_by_addressID(next_node_address)

    def getPrevNode(self, next_node):
        if self.store_address is None:
            raise Exception("The node doesn't have a store address. Hence it can't find the next node. Make sure you set the near nodes first.")

        if next_node is None:
            next_address = 0
        else:
            next_address = next_node.getNodeAddress()

        prev_node_address = self.store_address ^ next_address
        return get_object_by_addressID(prev_node_address)

class XORLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        global AN
        AN = Node(data) # AN == > appendNode

        if not self.head:
            self.head = AN
            self.head.setNearNodes(None, None)

XLL = XORLinkedList() 

print(XLL.head)
XLL.append("A")

print(XLL.head.data)
