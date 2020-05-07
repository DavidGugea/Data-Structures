import random
import math

class Node(object):
    def __init__(self, data):
        self.data = data

        self.next = None
        self.prev = None
        self.down = None
        self.up = None

class SkipList(object):
    def __init__(self):
        '''
        ( None -> inf -> data ) * 5
        '''

        for i in range(5):
            exec("self.head{0} = Node(math.inf)\nself.last{0} = Node(math.inf)".format(i))

        for i in range(5):
            if i == 0:
                self.head0.down = None
                self.head0.up = self.head1

                self.last0.down = None
                self.last1.up = self.last1
            elif i == 4:
                self.head4.down = self.head3
                self.head4.up = None

                self.last4.down = self.last3
                self.last4.up = None
            else:
                exec("self.head{0}.up = self.head{1}\nself.head{0}.down = self.head{2}\nself.last{0}.up = self.last{1}\nself.last{0}.down = self.last{2}".format(i, i+1, i-1))

    def display(self):
        LAYERS = self.getNodeData()

        for i in range(4, -1, -1):
            print("LAYER {0} -- > {1}".format(i, LAYERS[i]))

    def getNodeData(self):
        LAYERS_DATA = [ list() for i in range(5) ]

        for i in range(5):
            exec("current = self.head{0}\nwhile current:\n\tLAYERS_DATA[{0}].append(current.data)\n\tcurrent = current.next".format(i))

        return LAYERS_DATA 

    def append(self, data):
        if not self.head0.next:
            self.last0 = Node(data)

            self.last0.prev = self.head0
            self.head0.next = self.last0
        else:
            NEW_APPEND_NODE = Node(data)

            NEW_APPEND_NODE.prev = self.last0
            self.last0.next = NEW_APPEND_NODE

            self.last0 = self.last0.next

        randomSkip = random.randint(1, 2)
        LAYER_COUNTER = 1

        current = self.last0
       
        '''
        if not self.head1.next:
            self.last1 = Node(data)

            self.last1.prev = self.head1
            self.last1.down = current

            self.head1.next = self.last1

            current.up = self.last1
        else:
            NEW_APPEND_NODE = Node(data)

            NEW_APPEND_NODE.down = current

            NEW_APPEND_NODE.prev = self.last1
            self.last1.next = NEW_APPEND_NODE

            self.last1 = self.last1.next

            current.up = NEW_APPEND_NODE
        '''

        while randomSkip != 2:
            exec("if not self.head{0}.next:\n\tself.last{0} = Node(data)\n\tself.last{0}.prev = self.head{0}\n\tself.last{0}.down = current\n\tself.head{0}.next = self.last{0}\n\tcurrent.up = self.last{0}\nelse:\n\tNEW_APPEND_NODE = Node(data)\n\tNEW_APPEND_NODE.down = current\n\tNEW_APPEND_NODE.prev = self.last{0}\n\tNEW_APPEND_NODE.prev = self.last{0}\n\tself.last{0}.next = NEW_APPEND_NODE\n\tself.last{0} = self.last{0}.next\n\tcurrent.up = NEW_APPEND_NODE".format(LAYER_COUNTER))
            
            LAYER_COUNTER += 1
            if LAYER_COUNTER == 5:
                break

            current = current.up
            randomSkip = random.randint(1, 2)

SL = SkipList()

for i in range(1, 21):
    SL.append(i)

for i in range(3):
    print()

for i in range(3):
    print()

SL.display()
