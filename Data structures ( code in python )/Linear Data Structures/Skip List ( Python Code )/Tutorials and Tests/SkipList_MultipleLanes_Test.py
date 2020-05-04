import random

class Node(object):
    def __init__(self, data):
        self.data = data

        self.next = None
        self.prev = None
        self.up = None
        self.down = None

class SkipList(object):
    def __init__(self, max_layers):
        self.max_layers = max_layers

        self.head_low = None
        self.head_high = None

    def getNodeData(self):
        LAYERS = list()

        current = self.head_high
        START_CURRENT = current
        
        for i in range(self.max_layers):
            print(current.data)
            print("LAYER {0}".format(self.max_layers - i)) 

            if current.next:
                print("CURRENT.NEXT -- > {0}".format(current.next.data))
            else:
                print("CURRENT.NEXT -- > {0}".format(current.next))

            if current.down:
                print("CURRENT.DOWN -- > {0}".format(current.down.data))
            else:
                print("CURRENT.DOWN -- > {0}".format(current.down))

            for i in range(2):
                print()

            current = START_CURRENT.down
            START_CURRENT = current


    def append(self, data):
        if not self.head_low and not self.head_high:
            self.head_low = Node(data)

            prev = None
            current = self.head_low

            for i in range(self.max_layers - 1):
                # Set up node
                current.up = Node(data)
                
                # Keep track of prev & current 
                prev = current
                current = current.up
                
                # Set down node
                current.down = prev

            self.head_high = current
        else:
            # Iterate & find last place possible
            current = self.head_low
            
            while current.next:
                current = current.next

            current.next = Node(data)

            # Go up
            prev = None
            current = current.next

            randomUp = random.randint(1, 10)

            while randomUp % 2 != 0:
                current.up = Node(data)

                prev = current
                current = current.up

                current.down = prev

                randomUp = random.randint(1, 10)
            
SL = SkipList(5)

SL.append(1)
SL.append(2)

for i in range(3):
    print()


for i in range(3):
    print()

SL.getNodeData()

'''
counter = SL.max_layers - 1  
for layer in SL.getNodeData():
    print("Layer No. {0} -- > {1}".format(counter, layer))
    counter -= 1 
'''
