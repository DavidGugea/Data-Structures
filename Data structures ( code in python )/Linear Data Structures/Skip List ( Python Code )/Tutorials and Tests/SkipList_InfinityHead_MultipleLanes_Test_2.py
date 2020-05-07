import random
import math

class Node(object):
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None
        self.down = None
        self.up = None

class SkipList(object):
    def __init__(self):
        for i in range(5):
            exec("self.head{0} = Node(-math.inf)\nself.last{0} = Node(-math.inf)".format(i))

        for i in range(5):
            if i == 0:
                self.head0.down = None
                self.head0.up = self.head1

                self.last0.down = None
                self.last0.up = self.last1
            elif i == 4:
                self.head4.down = self.head3
                self.head4.up = None

                self.last4.down = self.last3
                self.last4.up = None
            else:
                exec("self.head{0}.down = self.head{2}\nself.head{0}.up = self.head{1}\nself.last{0}.down = self.last{2}\nself.last{0}.up = self.last{1}".format(i, i+1, i-1))

    def display(self):
        LAYERS_NODE_DATA = self.getNodeData()
        for i in range(4, -1, -1):
            print("LAYER {0} -- > {1}".format(i, LAYERS_NODE_DATA[i])) 


    def getNodeData(self):
        LAYERS_NODE_DATA = [ list() for i in range(5) ] 

        for LAYER_COUNTER in range(5):
            exec("current = self.head{0}\nwhile current:\n\tLAYERS_NODE_DATA[{0}].append(current.data)\n\tcurrent = current.next".format(LAYER_COUNTER))

        return LAYERS_NODE_DATA

    def search(self, data):
        prev = None
        current = self.head4
        START_CURRENT = current

        while current:
            if current.data == data: return current
            elif current.data < data and current.next:
                prev = current
                current = current.next
            elif current.data > data and not prev:
                current = START_CURRENT.down
                START_CURRENT = current
                prev = None
            elif current.data > data and prev:
                current = prev.down
                START_CURRENT = current
                prev = None
            elif current.data < data and not current.next and current.down:
                current = current.down
                START_CURRENT = current
                prev = None

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

        current = self.last0
        randomSkip = random.randint(1, 2)
        LAYER_COUNTER = 1

        '''
        if not self.head1.next:
            self.last1 = Node(data)
            
            self.last1.down = current
            current.up = self.last1

            self.last1.prev = self.head0
            self.head0.next = self.last1
        else:
            NEW_APPEND_NODE = Node(data)

            NEW_APPEND_NODE.prev = self.last1
            self.last1.next = NEW_APPEND_NODE

            NEW_APPEND_NODE.down = current
            current.up = NEW_APPEND_NODE

            self.last1 = self.last1.next
        '''

        while randomSkip != 2:
            exec("if not self.head{0}.next:\n\tself.last{0} = Node(data)\n\tself.last{0}.down = current\n\tcurrent.up = self.last{0}\n\tself.last{0}.prev = self.head{0}\n\tself.head{0}.next = self.last{0}\nelse:\n\tNEW_APPEND_NODE = Node(data)\n\tNEW_APPEND_NODE.prev = self.last{0}\n\tself.last{0}.next = NEW_APPEND_NODE\n\tNEW_APPEND_NODE.down = current\n\tcurrent.up = NEW_APPEND_NODE\n\tself.last{0} = self.last{0}.next".format(LAYER_COUNTER))

            LAYER_COUNTER += 1
            if LAYER_COUNTER == 5:
                break

            randomSkip = random.randint(1, 2)
            current = current.up
    

SL = SkipList()

for i in range(1, 6):
    SL.append(i)

for i in range(3):
    print()

'''
print(SL.last4.down.data)

for i in range(5):
    exec("print('looking at self.last{0}.down'.format(i))\nx = SL.last{0}.down\nif x:\n\tprint(x.data)\nelse:\n\tprint(x)".format(i))
    for i in range(2):
        print()
'''

print(SL.search(5))

for i in range(3):
    print()

SL.display()
