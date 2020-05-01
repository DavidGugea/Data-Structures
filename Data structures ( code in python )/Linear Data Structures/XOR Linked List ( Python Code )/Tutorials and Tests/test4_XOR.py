def getByAddress(S_ID):
    # S_ID == > search id

    # The ID '0' represents None  
    if S_ID == 0:
        return None

    # Iterate through all the global values and find the global variable that has the same id as the one we are searching for. 
    for global_var in tuple(globals().values()):
        if id(global_var) == S_ID:
            return global_var
    
    # If no global variable was found with the S_ID, return None  
    return None

###########################
GLOBALS = list()
###########################

def getByAddress_TEST(S_ID):
    # The ID '0' represents None  
    if S_ID == 0:
        return None

    # Iterate through all the global values and find the global variable that has the same id as the one we are searching for. 
    for global_var in tuple(GLOBALS):
        if id(global_var) == S_ID:
            return global_var
    
    # If no global variable was found with the S_ID, return None  
    return None
   

class Node(object):
    def __init__(self, data):
        self.data = data
        self.store_address = None

    def getAddress(self):
        return id(self)

    def setNearNodes(self, prev_node = None, next_node = None):
        GLOBALS.extend([prev_node, next_node])

        if prev_node is not None:
            prev_address = prev_node.getAddress()
        else:
            prev_address = 0

        if next_node is not None:
            next_address = next_node.getAddress()
        else:
            next_address = 0

        self.store_address = prev_address ^ next_address

    def getNextNode(self, prev_node):
        if self.store_address is None:
            raise Exception("The node doesn't have a store address. Hence it can't find the next node. Make sure you set the near nodes first.")

        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.getAddress()
        
        # self.store_address ^ prev_address = NEXT_ID ^ ( PREV_ID ^ PREV_ID ) = NEXT_ID ^ 0 = NEXT_ID ( therefore we get the address of the next node ) 
        next_node_address = self.store_address ^ prev_address 
        return getByAddress_TEST(next_node_address)
    
    def getPrevNode(self, next_node):
        if self.store_address is None:
            raise Exception("The node doesn't have a store address. Hence it can't find the next node. Make sure you set the near nodes first.")

        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.getAddress()
        
        # self.store_address ^ next_address = PREV_ID ^ ( NEXT_ID ^ NEXT_ID ) = PREV_ID ^ 0 = PREV_ID 
        prev_node_address = self.store_address ^ next_address
        return getByAddress_TEST(prev_node_address)

class XORLinkedList(object):
    def __init__(self):
        self.head = None

    def check(self):
        prev = None
        current = self.head

        while current.getNextNode(prev):
            temp = current
            current = current.getNextNode(prev)
            prev = temp
       
        if prev:
            print("IN THE END PREV -- > {0}".format(prev.data))
        else:
            print("IN THE END PREV -- > {0}".format(prev))

        if current:
            print("IN THE END CURRENT -- > {0}".format(current.data))
        else:
            print("IN THE END CURRENT -- > {0}".format(current))


    def append(self, data):
        global AN
        AN = Node(data)

        if not self.head:
            self.head = AN
            self.head.setNearNodes(None, None)
        else:
            '''

            self.head.setNearNodes(None, AN)
            AN.setNearNodes(self.head, TEST_NODE)
            TEST_NODE.setNearNodes(self.head, None)

            '''

            prev = None
            current = self.head

            while current.getNextNode(prev):
                temp = current
                current = current.getNextNode(prev)
                prev = temp
  
            print("-"*100)
            for i in range(3):
                print()


            if prev:
                print("PREV     -- > {0}".format(prev.data)) 
            else:
                print("PREV     -- > {0}".format(prev)) 

            print("CURRENT  -- > {0}".format(current.data))

            for i in range(3):
                print()

            current.setNearNodes(prev, AN)
            AN.setNearNodes(current, None)

        '''
        global AN # AN = APPEND NODE
        AN = Node(data)

        if not self.head:
            self.head = AN
            self.head.setNearNodes(None, None)
        else:
            prev = None 
            current = self.head 
    
            try:
                while current.getNextNode(prev):
                    temp = current
                    current = current.getNextNode(prev)
                    prev = temp
            except Exception as __e__:
                
                for i in range(3):
                    print()

                print("ERROR -- > {0}".format(str(__e__)))

                print("PREV    -- > {0}".format(prev.data))
                print("CURRENT -- > {0}".format(current.data))

                for i in range(3):
                    print()

            current.setNearNodes(prev, AN)
            AN.setNearNodes(current, None)
        '''

XLL = XORLinkedList()
print(XLL.head)

for i in range(3):
    print()

XLL.append("A")

print(XLL.head, XLL.head.data)
print(XLL.head.getNextNode(None))

'''
TEST_NODE_ASD = Node("THIS IS ONLY A TEST NODE ~ LINE 140 ~ ")
TEST_NODE_ASD.setNearNodes(XLL.head, None)
XLL.head.setNearNodes(None, TEST_NODE_ASD)
'''

for i in range(3):
    print() 

print("CHECK -- > ")
XLL.check()

XLL.append("B")

print("HEAD -- > {0}".format(XLL.head.data))
print("HEAD NEXT NODE -- > {0}".format(XLL.head.getNextNode(None).data))
print("HEAD NEXT NODE BOOLEAN VALUE -- > {0}".format(bool(XLL.head.getNextNode(None))))
print("HEAD NEXT NODE NEXT NODE -- > {0}".format(XLL.head.getNextNode(None).getNextNode(XLL.head)))
print("HEAD NEXT NODE NEXT NODE BOOLEAN VALUE -- > {0}".format(bool(XLL.head.getNextNode(None).getNextNode(XLL.head))))


for i in range(5):
    print()

XLL.check()

'''
def spaceUp():
    print("-"*100)
    
    for i in range(3):
        print()

XLL = XORLinkedList()

print("START HEAD -- > {0}".format(XLL.head))

spaceUp()

XLL.append("X")

print("FIRST APPEND HEAD                -- > {0}".format(XLL.head))
print("FIRST APPEND HEAD DATA           -- > {0}".format(XLL.head.data))
print("FIRST APPEND HEAD NEXT NODE      -- > {0}".format(XLL.head.getNextNode(None)))
print("FIRST APPEND HEAD BOOLEAN VALUE  -- > {0}".format(bool(XLL.head)))

spaceUp()

XLL.append("Y")

print("SECOND APPEND HEAD                           -- > {0}".format(XLL.head))
print("SECOND APPEND HEAD DATA                      -- > {0}".format(XLL.head.data))

print()
print("< - >")
print()

print("SECOND APPEND HEAD NEXT NODE                 -- > {0}".format(XLL.head.getNextNode(None)))
print("SECOND APPEND HEAD NEXT NODE DATA            -- > {0}".format(XLL.head.getNextNode(None).data))
print("SECOND APPEND HEAD NEXT NODE BOOLEAN VALUE   -- > {0}".format(bool(XLL.head.getNextNode(None).data)))

print()
print("< - >")
print()

print("SECOND APPEND HEAD NEXT NODE NEXT NODE       -- > {0}".format(XLL.head.getNextNode(None).getNextNode(None)))
print("SECOND APPEND HEAD NEXT NODE NEXT NODE BOOLEAN VALUE -- > {0}".format(bool(XLL.head.getNextNode(None).getNextNode(XLL.head))))

spaceUp()
'''

for i in range(10):
    print()

class XORLinkedList_2(object):
    def __init__(self):
        self.head = None

    def checkForIteration(self):
        if self.head is None:
            return dict()

        prev = None
        current = self.head 
    
        iterationDict = dict()
        index = 0

        while current.getNextNode(prev):
            if prev is not None:
                prevString = str(prev.data)
            else:
                prevString = str(prev)

            if current is not None:
                currentString = str(current.data)
            else:
                currentString = str(current)

            iterationDict[index] = "PREV : {0} | CURRENT : {1}".format(prevString, currentString)

            temp = current
            current = current.getNextNode(prev)
            prev = temp 

        return iterationDict

    def append(self, data):
        global appendNode
        appendNode = Node(data)

        GLOBALS.append(appendNode)

        if self.head is None:
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

XLL2 = XORLinkedList_2()

print(XLL2.checkForIteration())

XLL2.append("X")
XLL2.append("Y")

print("HEAD -- > {0}".format(XLL.head.data))
print("HEAD NEXT NODE -- > {0}".format(XLL.head.getNextNode(None).data))
print("HEAD NEXT NODE NEXT NODE -- > {0}".format(XLL.head.getNextNode(None).getNextNode(XLL.head)))


for i in range(3):
    print()

print(XLL2.checkForIteration())
