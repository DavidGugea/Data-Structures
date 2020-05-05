import random

class Node(object):
    def __init__(self,data):
        self.data = data

        self.next = None
        self.prev = None

        self.down = None
        self.up = None

class SkipList(object):
    def __init__(self):
        self.head0 = None # LAYER 1
        self.head1 = None # LAYER 2
        self.head2 = None # LAYER 3
        self.head3 = None # LAYER 4 
        self.head4 = None # LAYER 5

    def getNodeData(self):
        LAYERS = [ list() for i in range(5) ]
        
        RUN_THROUGH_STRING = '''
current = self.head{0}
while current:
    LAYERS[{0}].append(current.data)
    current = current.next
                
        '''

        for i in range(5):
            exec(RUN_THROUGH_STRING.format(i))

        return LAYERS

    def append(self, data):
        if not self.head0:
            for i in range(5):
                exec("self.head{0} = Node(data)".format(i))
                exec("self.last{0} = Node(data)".format(i))

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
                    exec("self.head{0}.down = self.head{1}".format(i, i-1))
                    exec("self.head{0}.up = self.head{1}".format(i, i+1))

                    exec("self.last{0}.down = self.last{1}".format(i, i-1))
                    exec("self.last{0}.up = self.last{1}".format(i, i+1))
        elif self.head0 and not self.head0:
            # Create last nodes
            self.last0 = Node(data)

            self.last0.prev = self.head0
            self.head0.next = self.last0

            randomSkip = random.randint(1, 2)

            current = self.last0 
            counter = 1 

            

SL = SkipList()
SL.append(1)

for i in range(3):
    print()

print(SL.getNodeData())
