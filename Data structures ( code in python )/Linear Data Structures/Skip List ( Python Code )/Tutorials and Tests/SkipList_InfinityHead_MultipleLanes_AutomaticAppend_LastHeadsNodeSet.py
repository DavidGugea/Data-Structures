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
        for LAYER_LEVEL in range(5):
            exec("self.head{0} = Node(-math.inf)\nself.last{0} = Node(-math.inf)".format(LAYER_LEVEL))
        
        for LAYER_LEVEL in range(5):
            if LAYER_LEVEL == 0:
                self.head0.down = None
                self.head0.up = self.head1

                self.last0.down = None
                self.last0.up = self.last1
            elif LAYER_LEVEL == 4:
                self.head4.down = self.head3
                self.head4.up = None

                self.last4.down = self.last3
                self.last4.up = None
            else:
                exec("self.head{0}.down = self.head{1}\nself.head{0}.up = self.head{2}\nself.last{0}.down = self.last{1}\nself.last{0}.up = self.last{2}".format(LAYER_LEVEL, LAYER_LEVEL-1, LAYER_LEVEL+1))

        self.LAYER_0_NODE_DATA = [-math.inf] 

    def display(self):
        LAYERS_NODE_DATA = self.getNodeData()

        for i in range(4, -1, -1):
            print("LAYER {0} -- > {1}".format(i, LAYERS_NODE_DATA[i]))

    def getNodeData(self):
        LAYERS_NODE_DATA = [ list() for i in range(5) ] 

        for LAYER_LEVEL in range(5):
            exec("current = self.head{0}\nwhile current:\n\tLAYERS_NODE_DATA[{0}].append(current.data)\n\tcurrent = current.next".format(LAYER_LEVEL))

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
                current = START_CURRENET.down
                START_CURRENT = current
                prev = None
        
        raise ValueError("The given data couldn't be found in the node data.")

    def append(self, data):
        if not self.head0.next:
            self.last0 = Node(data)
            
            self.last0.prev = self.head0
            self.head0.next = self.last0

            randomSkip = random.randint(1, 2)
            LAYER_COUNTER = 1 
            current = self.last0

            while randomSkip != 2:
                exec("self.last{0} = Node(data)\nself.last{0}.prev = self.head{0}\nself.last{0}.down = current\nself.head{0}.next = self.last{0}\ncurrent.up = self.last{0}".format(LAYER_COUNTER))
                
                LAYER_COUNTER += 1
                if LAYER_COUNTER == 5:
                    break

                randomSkip = random.randint(1, 2)
                current = current.up

            self.LAYER_0_NODE_DATA.append(data)
        else:
            NODE_INSERT_INDEX = 0
            for i in self.LAYER_0_NODE_DATA:
                if i > data:
                    self.LAYER_0_NODE_DATA.insert(NODE_INSERT_INDEX, data)
                    break
                
                NODE_INSERT_INDEX += 1
            
            if NODE_INSERT_INDEX == len(self.LAYER_0_NODE_DATA):
                self.LAYER_0_NODE_DATA.append(data)
            
            # APPEND ON LAYER 0
            PREV_TRACK = self.search(self.LAYER_0_NODE_DATA[NODE_INSERT_INDEX-1], False)

            APPEND_NODE = Node(data)
            APPEND_NODE.prev = PREV_TRACK
            APPEND_NODE.next = PREV_TRACK.next

            LAST_NODE_LAYER_0 = False
            if PREV_TRACK.next:
                PREV_TRACK.next.prev = APPEND_NODE
            else:
                LAST_NODE_LAYER_0 = True
                        
            PREV_TRACK.next = APPEND_NODE
            
            if LAST_NODE_LAYER_0:
                self.last0 = self.last0.next
                

            randomSkip = random.randint(1, 2)

            current = PREV_TRACK.next
            LAYER_COUNTER = 1

            while randomSkip != 2:
                while not PREV_TRACK.up:
                    PREV_TRACK = PREV_TRACK.prev

                PREV_TRACK = PREV_TRACK.up

                HEAD_ON_CURRENT_LAYER = eval("self.head{0}".format(LAYER_COUNTER))

                APPEND_NODE = Node(data)
                APPEND_NODE.next = PREV_TRACK.next
                APPEND_NODE.prev = PREV_TRACK
                APPEND_NODE.down = current
                current.up = APPEND_NODE

                if not HEAD_ON_CURRENT_LAYER.next:
                    exec("self.last{0} = APPEND_NODE\nself.last{0}.prev = self.head{0}\nself.head{0}.next = self.last{0}".format(LAYER_COUNTER))
                else:
                    if PREV_TRACK.next:
                        PREV_TRACK.next.prev = APPEND_NODE
                        PREV_TRACK.next = APPEND_NODE
                    else:
                        PREV_TRACK.next = APPEND_NODE
                        exec("self.last{0} = self.last{0}.next".format(LAYER_COUNTER))

                randomSkip = random.randint(1, 2) 

                LAYER_COUNTER += 1
                if LAYER_COUNTER == 5: break

                current = current.up

SL = SkipList()

for i in range(1, 21):
    SL.append(i)

for i in range(5):
    print()

for LAYER_COUNTER in range(5):
    print("last{0} -- > {1}".format(LAYER_COUNTER, eval("SL.last{0}.data".format(LAYER_COUNTER))))

for i in range(5):
    print()

SL.display()
