CHECK_IDS = dict()

def getByAddress(S_ID):
    if S_ID == 0:
        return None
    
    for GV in tuple(globals().values()):
        if id(GV) == S_ID:
            return GV

    return None 

class ID_CHECKER(object):
    def insertID(self, insertion_node):
        global CHECK_IDS

        if insertion_node:
            insertion_node = insertion_node.data
        else:
            insert_node = None

        CHECK_IDS[insertion_node] = id(insertion_node)
    def check_ids(self, IDS_DICT):
        return len(list(set(list(IDS_DICT.values())))) == len(list(IDS_DICT.values()))

IC = ID_CHECKER()

class Node(object):
    def __init__(self, data):
        self.data = data
        self.store_address = None
   
    def getAddress(self):
        return id(self)

    def setNearNodes(self, prev_node, next_node):
        if prev_node is None:
            prev_address = 0
        else:
            prev_address = prev_node.getAddress()

        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.getAddress()

        self.store_address = prev_address ^ next_address
    
        print("< < ------------------------------------------ > >")
        for i in range(2):
            print()
        
        print("FOR NODE DATA        -- > {0}".format(self.data))

        print()
        if prev_node:
            print("PREV NODE            -- > {0}".format(prev_node.data))
        else:
            print("PREV NODE            -- > {0}".format(prev_node))
        print("PREV_ADDRESS         -- > {0}".format(prev_address))
        print()
        if next_node:
            print("NEXT NODE            -- > {0}".format(next_node.data))
        else:
            print("NEXT NODE            -- > {0}".format(next_node))
        print("NEXT_ADDRESS         -- > {0}".format(next_address))

        print()
        print("NEW STORE_ADDRESS    -- > {0} ^ {1} = {2}".format(prev_address, next_address, self.store_address)) 


        for i in range(2):
            print()
        print("< < ------------------------------------------ > >")

    def getNextNode(self, prev_node):
        if self.store_address == None:
            raise Exception("The xor linked list doesn't have a store address. Hence it can't find the id of the next node. Make sure you set the near nodes first.")

        if prev_node == None:
            prev_address = 0 
        else:
            prev_address = prev_node.getAddress()

        next_node_address = self.store_address ^ prev_address

        return getByAddress(next_node_address)

    def getPrevNode(self, next_node):
        if self.store_address == None:
            raise Exception("The xor linked list doesn't have a store address. Hence it can't find the id of the previous node. Make sure you set the near nodes first.")

        if next_node is None:
            next_address = 0
        else:
            next_address = next_node.getAddress()

        prev_node_address = self.store_address ^ next_address

        return getByAddress(prev_node_address)

class XORLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        global appendNode
        appendNode = Node(data)

        IC.insertID(appendNode)

        if not self.head:
            self.head = appendNode
            self.head.setNearNodes(None, None)
        else:
            prev = None
            current = self.head

            print("BEFORE LOOP current.getNextNode(prev)                -- > {0}".format(current.getNextNode(prev)))
            print("BEFORE LOOP self.head.getNextNode(prev)              -- > {0}".format(self.head.getNextNode(None)))
            print("BEFORE LOOP current.getNextNode(prev) BOOLEAN VALUE  -- > {0}".format(bool(current.getNextNode(prev))))
            print()
            print("BEFORE LOOP HEAD STORE ADDRESS                       -- > {0}".format(self.head.store_address))
            print("BEFORE LOOP APPEND NODE STORE ADDRESS                -- > {0}".format(appendNode.store_address))
            print("BEFORE LOOP self.head ID                             -- > {0}".format(id(self.head)))
            print("BEFORE LOOP APPEND NODE ID                           -- > {0}".format(id(appendNode))) 
            print()
            print("CURRENT IS SELF.HEAD : {0} |  CURRENT ID : {1} | HEAD ID : {2}".format(current is self.head, id(current), id(self.head))) 
    
            while current.getNextNode(prev):
                temp = current
                current = current.getNextNode(prev)
                prev = temp 

            if prev:
                print("PREV -- > {0}".format(prev.data))
            else:
                print("PREV -- > {0}".format(prev))
    
            if current:
                print("CURRENT -- > {0}".format(current.data))
            else:
                print("CURRENT -- > {0}".format(current))

            current.setNearNodes(prev, appendNode)
            appendNode.setNearNodes(current, None)

            print()
            print("AFTER LOOP ( still in function ) current.getNextNode(prev) : {0}".format(current.getNextNode(prev).data)) 

def spaceUp():
    print("-"*75)

    for i in range(5):
        print()

XLL = XORLinkedList()

spaceUp()

print(XLL.head)

spaceUp()

XLL.append("A")
print()
print("HEAD -- > {0}".format(XLL.head.data))
print("HEAD NEXT NODE -- > {0}".format(XLL.head.getNextNode(None)))

spaceUp()

XLL.append("B")
print()
print("HEAD -- > {0}".format(XLL.head.data))
print("HEAD NEXT NODE -- > {0}".format(XLL.head.getNextNode(None).data))
print("HEAD NEXT NODE NEXT NODE -- > {0}".format(XLL.head.getNextNode(None).getNextNode(XLL.head)))

spaceUp()

XLL.append("C")
print()
print("HEAD -- > {0}".format(XLL.head.data))
print("HEAD NEXT NODE -- > {0}".format(XLL.head.getNextNode(None).data))
print("HEAD NEXT NODE NEXT NODE -- > {0}".format(XLL.head.getNextNode(None).getNextNode(XLL.head)))

spaceUp()
