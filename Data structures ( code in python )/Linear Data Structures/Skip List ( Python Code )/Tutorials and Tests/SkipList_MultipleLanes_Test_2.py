import random

class Node(object):
    def __init__(self, data):
        self.data = data

        self.up = None
        self.next = None
        self.prev = None
        self.down = None

class SkipList(object):
    def __init__(self):
        # 5 lanes

        self.head0 = None
        self.last0 = None

        self.head1 = None
        self.last1 = None

        self.head2 = None
        self.last2 = None 

        self.head3 = None
        self.last3 = None 
    
        self.head4 = None
        self.last4 = None

    def getNodeData(self):
        LAYERS = list()

        current = self.head4
        START_CURRENT = current

        LAYER_LIST = list()
        
        '''
        if not current.next and not current.down:
            print("ASD")
        elif not current.next and current.down:
            print("BCD")
        '''

        LAYER_LIST.append(current.data)

        if not current.next and not current.down:
            print("ASD")

            LAYERS.append(LAYER_LIST)
            return LAYERS
        elif not current.next and current.down:
            print("BCD")

            current = START_CURRENT.down
            START_CURRENT = current

            LAYERS.append(LAYER_LIST)
            LAYER_LIST = list()

        current = current.next
         


    def append(self, data):
        if not self.head0:
            for i in range(5):
                self.head0 = Node(data)
                self.last0 = Node(data)

                self.head1 = Node(data)
                self.last1 = Node(data)

                self.head2 = Node(data)
                self.last2 = Node(data)

                self.head3 = Node(data)
                self.last3 = Node(data)

                self.head4 = Node(data)
                self.last4 = Node(data)

                #################################
        
                self.head0.up = self.head1
                self.head0.down = None

                self.head1.up = self.head2
                self.head1.down = self.head0 

                self.head2.up = self.head3
                self.head2.down = self.head1

                self.head3.up = self.head4
                self.head3.down = self.head2

                self.head4.up = None
                self.head4.down = self.head3 

SL = SkipList()
SL.append(1)

for i in range(3):
    print()

for i in range(3):
    print()

print(SL.getNodeData())
