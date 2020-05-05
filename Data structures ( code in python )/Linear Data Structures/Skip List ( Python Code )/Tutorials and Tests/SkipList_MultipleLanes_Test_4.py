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
        for i in range(5):
            exec("self.head{0} = None".format(i))
            exec("self.last{0} = None".format(i))
    
    def getNodeData(self):
        LAYERS_LIST = list()
        LAYER_LIST = list()

        current = self.head0
        START_CURRENT = current

        counter = 0

        while True:
            LAYER_LIST.append(current.data)

            if not current.next and not current.down and:
                LAYERS_LIST.append(LAYER_LIST)
                return LAYERS_LIST
            elif not current.next and current.down:
                current = START_CURRENT.down
                START_CURRENT = current

                LAYERS_LIST.append(LAYER_LIST)
                LAYER_LIST = list()
            else:
                current = current.next


    def append(self, data):
        if not self.head0:
            for i in range(5):
                exec("self.head{0} = Node(data)".format(i))
                exec("self.last{0} = Node(data)".format(i))

                exec("self.head{0}.next = self.last{0}".format(i))

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

SL = SkipList()
SL.append(1)

for i in range(3):
    print()


for i in range(3):
    print()

LAYERS = SL.getNodeData()
print(LAYERS)
