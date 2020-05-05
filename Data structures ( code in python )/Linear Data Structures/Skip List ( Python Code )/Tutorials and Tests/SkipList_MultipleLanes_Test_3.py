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
        # Create 5 layers
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
        LAYERS_DATA = list()

        # Start from up & go down
        current = self.head4
        START_CURRENT = current

        LAYER_LIST = list()

        while True:
            LAYER_LIST.append(current.data)

            if not current.next and not current.down:
                LAYERS_DATA.append(LAYER_LIST)
                return LAYERS_DATA
            elif not current.next and current.down:
                current = START_CURRENT.down
                START_CURRENT = current

                LAYERS_DATA.append(LAYER_LIST)
                LAYER_LIST = list()
            else:
                current = current.next

    def append(self, data):
        if not self.head0:
            # Create the layers heads

            #######################
            self.head0 = Node(data)
            #######################

            #######################
            self.head1 = Node(data)
            #######################

            #######################
            self.head2 = Node(data)
            #######################

            #######################
            self.head3 = Node(data)
            #######################

            #######################
            self.head4 = Node(data)
            #######################

            # Set the pointers ( ups & downs )

            ###############################
            self.head0.up = self.head1
            self.head0.down = None
            ###############################

            ##############################
            self.head1.up = self.head2
            self.head1.down = self.head0
            ##############################

            ##############################
            self.head2.up = self.head3
            self.head2.down = self.head1
            ##############################

            ##############################
            self.head3.up = self.head4
            self.head3.down = self.head2 
            ##############################

            ##############################
            self.head4.up = None
            self.head4.down = self.head3
            ##############################
        else:
            if not self.last0:
                self.last0 = Node(data)

                self.last0.prev = self.head0
                self.head0.next = self.last0
            else:
                print("ASD")
                appendNode = Node(data)
                self.last0.next = appendNode
                appendNode.prev = self.last0
                
                self.last0 = self.last0.next 

            current = self.last0
            randomSkip = random.randint(1, 2)

            layerUp = 1
            while randomSkip != 2:
                if layerUp == 1:
                    if not self.last1:
                        self.last1 = Node(data)

                        self.head1.next = self.last1
                        self.last1.prev = self.head1

                        self.last1.down = current
                        current.up = self.last1
                    else:
                        newUpNode = Node(data)

                        current.up = newUpNode
                        newUpNode.down = current
                        
                        self.last1.next = newUpNode
                        newUpNode.prev = self.last1

                        self.last1 = self.last1.next
                if layerUp == 2:
                    if not self.last2:
                        self.last2 = Node(data)

                        self.head2.next = self.last2
                        self.last2.prev = self.head2

                        self.last2.down = current
                        current.up = self.last2
                    else:
                        newUpNode = Node(data)

                        current.up = newUpNode
                        newUpNode.down = current
                        
                        self.last2.next = newUpNode
                        newUpNode.prev = self.last2

                        self.last2 = self.last2.next

                if layerUp == 3:
                    if not self.last3:
                        self.last3 = Node(data)

                        self.head3.next = self.last3
                        self.last3.prev = self.head3

                        self.last3.down = current
                        current.up = self.last3
                    else:
                        newUpNode = Node(data)

                        current.up = newUpNode
                        newUpNode.down = current
                        
                        self.last3.next = newUpNode
                        newUpNode.prev = self.last3

                        self.last3 = self.last3.next

                if layerUp == 4:
                    if not self.last4:
                        self.last4 = Node(data)

                        self.head4.next = self.last4
                        self.last4.prev = self.head4

                        self.last4.down = current
                        current.up = self.last4
                    else:
                        newUpNode = Node(data)

                        current.up = newUpNode
                        newUpNode.down = current
                        
                        self.last4.next = newUpNode
                        newUpNode.prev = self.last4

                        self.last4 = self.last4.next
                    
                    break

                current = current.up
                layerUp += 1
                randomSkip = random.randint(1, 2)

SL = SkipList()
SL.append(1)
SL.append(2)
SL.append(3)
SL.append(4)
SL.append(5)

for i in range(3):
    print()

if SL.last1:
    print("SL.last1 -- > {0}".format(SL.last1.data))
else:
    print("SL.last1 -- > {0}".format(SL.last1))

if SL.last2:
    print("SL.last2 -- > {0}".format(SL.last2.data))
else:
    print("SL.last2 -- > {0}".format(SL.last2))



for i in range(3):
    print()

LAYERS = SL.getNodeData()
for LAYER_NO in range(4, -1, -1):
    print("LAYER {0} -- > {1}".format(LAYER_NO, LAYERS[4 - LAYER_NO]))
