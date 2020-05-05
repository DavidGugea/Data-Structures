import random

class Node(object):
    def __init__(self, data):
        self.data = data

        self.next = None
        self.prev = None

        self.up = None
        self.down = None

class SkipList(object):
    def __init__(self):
        HEAD_FORMAT_STRING = "self.head{0} = None"
        LAST_FORMAT_STRING = "self.last{0} = None"

        for i in range(5):
            exec(HEAD_FORMAT_STRING.format(i))
            exec(LAST_FORMAT_STRING.format(i))

    def getNodeData(self):
        LAYERS = [ list() for i in range(5) ]

        LAYER_ITERATION_STRING = '''
current = self.head{0}
while current:
    LAYERS[{0}].append(current.data)
    current = current.next
        '''

        for i in range(5):
            exec(LAYER_ITERATION_STRING.format(i))
                

        return LAYERS

    def append(self, data):
        if not self.head0:
            HEAD_FORMAT_STRING = "self.head{0} = Node(data)"
            LAST_FORMAT_STRING = "self.last{0} = Node(data)"

            for i in range(5):
                exec(HEAD_FORMAT_STRING.format(i))
                exec(LAST_FORMAT_STRING.format(i))
        else:
            appendNode = Node(data)
            
            if not self.head0.next:
                self.last0 = appendNode

                appendNode.prev = self.head0
                self.head0.next = appendNode
            else:
                self.last0.next = appendNode
                appendNode.prev = self.last0

                self.last0 = self.last0.next
            
            current = self.last0
            counter = 1
           
            randomSkip = random.randint(1, 2)

            while randomSkip != 2:
                if counter == 1:
                    nextUpHeadNode = self.head1
                    nextUpLastNode = self.last1
                elif counter == 2:
                    nextUpHeadNode = self.head2
                    nextUpLastNode = self.last2
                elif counter == 3:
                    nextUpHeadNode = self.head3
                    nextUpLastNode = self.last3
                elif counter == 4:
                    nextUpHeadNode = self.head4
                    nextUpLastNode = self.last4

                print("nextUpLastNode == self.last1 == > {0}".format(nextUpLastNode == self.last1))
                
                if not nextUpHeadNode.next:
                    newAppendNode = Node(data)

                    newAppendNode.down = current
                    current.up = newAppendNode

                    newAppendNode.prev = nextUpHeadNode
                    nextUpHeadNode.next = newAppendNode
                    
                    if counter == 1:
                        self.last1 = newAppendNode
                    elif counter == 2:
                        self.last2 = newAppendNode
                    elif counter == 3:
                        self.last3 = newAppendNode
                    elif counter == 4:
                        self.last4 = newAppendNode
                else:
                    newUpNode = Node(data)

                    nextUpLastNode.next = newUpNode
                    newUpNode.prev = nextUpLastNode

                    newUpNode.down = current
                    current.up = newUpNode

                current = current.up
                counter += 1

                if counter == 5:
                    break

                randomSkip = random.randint(1, 2)

SL = SkipList()

for i in range(3):
    print()

for i in range(1, 6):
    SL.append(i)

print("SL.last1.down -- > {0}".format(SL.last1.down))
print("SL.last1.down == SL.last0 -- > {0}".format(SL.last1.down == SL.last0))

for i in range(3):
    print()

LAYERS = SL.getNodeData()[::-1]
for i in range(4, -1, -1):
    print("LAYER {0} -- > {1}".format(i, LAYERS[4 - i]))
