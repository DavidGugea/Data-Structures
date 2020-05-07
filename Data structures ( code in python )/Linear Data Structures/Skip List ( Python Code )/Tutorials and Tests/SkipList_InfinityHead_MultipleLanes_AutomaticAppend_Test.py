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
                exec("self.head{0}.down = self.head{1}\nself.head{0}.up = self.head{2}\nself.last{0}.down = self.last{1}\nself.last{0}.up = self.last{2}".format(i, i-1, i+1))

        self.LAYER_0_NODE_DATA_INFO = [-math.inf] 

    def display(self):
        LAYERS_NODE_DATA = self.getNodeData()

        for i in range(4, -1, -1):
            print("LAYER {0} -- > {1}".format(i, LAYERS_NODE_DATA[i]))

    def getNodeData(self):
        LAYERS_NODE_DATA = [ list() for i in range(5) ] 

        for i in range(5):
            exec("current = self.head{0}\nwhile current:\n\tLAYERS_NODE_DATA[{0}].append(current.data)\n\tcurrent = current.next".format(i))

        return LAYERS_NODE_DATA

    def search(self, data, DIRECT_RETURN = True):
        current = self.head4
        START_CURRENT = current
        prev = None
        
        while current:
            if current.data == data:
                if DIRECT_RETURN: return current
                else:
                    while current.down:
                        current = current.down

                    return current
            elif current.data < data and current.next:
                prev = current
                current = current.next
            elif current.data < data and not current.next:
                current = current.down
                START_CURRENT = current
                prev = None
            elif current.data > data and prev:
                current = prev.down
                START_CURRENT = current
                prev = None
            elif current.data > data and not prev:
                current = START_CURRENT.down
                START_CURRENT = current
                prev = None
        
        raise ValueError("The given node data couldn't be found in the skip list.")

    def append(self, data):
        if not self.head0.next:
            self.last0  = Node(data)

            self.last0.prev = self.head0
            self.head0.next = self.last0
            
            randomSkip = random.randint(1, 2)
            current = self.last0
            LAYER_COUNTER = 1

            while randomSkip != 2:
                exec("self.last{0} = Node(data)\nself.last{0}.down = current\ncurrent.up = self.last{0}\nself.last{0}.prev = self.head{0}\nself.head{0}.next = self.last{0}".format(LAYER_COUNTER))

                LAYER_COUNTER += 1
                if LAYER_COUNTER == 5:
                    break
                
                current = current.up
                randomSkip = random.randint(1, 2)

            self.LAYER_0_NODE_DATA_INFO.append(data)
        else:
            NODE_DATA_INDEX_COUNTER = 0
            for i in self.LAYER_0_NODE_DATA_INFO:
                if i > data:
                    self.LAYER_0_NODE_DATA_INFO.insert(NODE_DATA_INDEX_COUNTER, data)
                    break

                NODE_DATA_INDEX_COUNTER += 1
            
            # APPEND ON LAYER 0
            PREV_TRACK = self.search(self.LAYER_0_NODE_DATA_INFO[NODE_DATA_INDEX_COUNTER-1], False)

            APPEND_NODE = Node(data)
            APPEND_NODE.prev = PREV_TRACK
            APPEND_NODE.next = PREV_TRACK.next
            if PREV_TRACK.next:
                PREV_TRACK.next.prev = APPEND_NODE
            PREV_TRACK.next = APPEND_NODE

            # MOVE UP WITH THE NEW APPEND NODE
            current = PREV_TRACK.next
            randomSkip = random.randint(1, 2)
            LAYER_COUNTER = 1
            
            while randomSkip != 2:
                while not PREV_TRACK.up:
                    PREV_TRACK = PREV_TRACK.prev

                PREV_TRACK = PREV_TRACK.up

                APPEND_NODE = Node(data)
                APPEND_NODE.prev = PREV_TRACK
                APPEND_NODE.next = PREV_TRACK.next
                APPEND_NODE.down = current 

                if PREV_TRACK.next:
                    PREV_TRACK.next.prev = APPEND_NODE
                PREV_TRACK.next = APPEND_NODE

                current.up = APPEND_NODE
                current = current.up

                if not PREV_TRACK.up and not PREV_TRACK.prev: break
                randomSkip = random.randint(1, 2)
        
SL = SkipList()

for i in range(20, -1, -1):
    SL.append(i)

for i in range(5):
    print()

SL.display()
