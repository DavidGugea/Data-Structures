class Node(object):
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None

        self.counter = 0

class SelfOrganizingList(object):
    def __init__(self):
        self.head = None

    def getNodeData(self):
        NODE_DATA_LIST = list()
        current = self.head

        while current:
            NODE_DATA_LIST.append(current.data)
            current = current.next

        return NODE_DATA_LIST

    def getNodeDictCounter(self):
        NODE_DICT_COUNTER = dict()
        current = self.head

        while current:
            NODE_DICT_COUNTER[current.data] =  current.counter
            current = current.next

        return NODE_DICT_COUNTER

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            prev = None
            current = self.head

            while current:
                prev = current
                current = current.next

            APPEND_NODE = Node(data)

            APPEND_NODE.prev = prev 
            prev.next = APPEND_NODE 

    # DEFAULTS 

    def MTF(self, node):
        # MTF = Move To Front
        PREV_NODE = node.prev
        NEXT_NODE = node.next

        if NEXT_NODE:
            NEXT_NODE.prev = PREV_NODE

        PREV_NODE.next = NEXT_NODE

        self.head.prev = node
        node.next = self.head

        self.head = node

    def TM(self, node):
        # TM = transpose method
        node.data, node.counter, node.prev.data, node.prev.counter = node.prev.data, node.prev.counter, node.data, node.counter

    def search(self, data):
        current = self.head
        
        while current:
            print(current.data)
            current = current.next
        
        '''
        if not current:
            raise ValueError("The given data couldn't be found in the self organizing list.")
        else:
            current.counter += 1
            if self.head.counter < current.counter:
                self.MTF(current)
            else:
                while current.prev:
                    if current.prev.counter < current.counter:
                        self.TM(current)
                        current = current.prev
                    else:
                        break
        '''
    

                    
SOL = SelfOrganizingList()

def present():
    print(SOL.getNodeData())
    print(SOL.getNodeDictCounter())

    for i in range(2):
        print()

print(SOL.head)
print(bool(SOL.head))

for i in range(2): print() 

SOL.append(1)

print(SOL.head)
print(bool(SOL.head))

for i in range(2): print() 

'''
present()

for i in range(1, 4): SOL.append(i)


present()
'''



'''
for i in range(2): SOL.search(4)

present()

SOL.search(3)

present()
'''
