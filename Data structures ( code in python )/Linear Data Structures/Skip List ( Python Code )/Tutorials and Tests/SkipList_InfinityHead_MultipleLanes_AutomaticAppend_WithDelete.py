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
                exec("self.head{0}.down = self.head{1}\nself.head{0}.up = self.head{2}\nself.last{0}.down = self.last{1}\nself.last{0}.up = self.last{2}".format(i, i-1,i+1))

        self.LAYER_0_NODE_DATA = [-math.inf] 

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
                prev = None
                START_CURRENT = current
            elif current.data > data and not prev:
                current = START_CURRENT.down
                START_CURRENT = current
                prev = None
            elif current.data > data and prev:
                current = prev.down
                START_CURRENT = current 
                prev = None

        raise ValueError("The given data couldn't be found in the skip list.")

    def display(self):
        LAYERS_NODE_DATA = self.getNodeData()

        for i in range(4, -1, -1):
            print("LAYER {0} -- > {1}".format(i, LAYERS_NODE_DATA[i]))

    def getNodeData(self):
        LAYERS_NODE_DATA = [ list() for i in range(5) ]

        for LAYER_COUNTER in range(5):
            exec("current = self.head{0}\nwhile current:\n\tLAYERS_NODE_DATA[{0}].append(current.data)\n\tcurrent = current.next".format(LAYER_COUNTER))

        return LAYERS_NODE_DATA

    def append(self, data):
        if not self.head0.next:
            # APPEND FIRST ON LAYER 0 ( FIRST LAYER )
            self.last0 = Node(data)

            self.last0.prev = self.head0
            self.head0.next = self.last0

            # GO UP
            randomSkip = random.randint(1, 2)
            current = self.last0
            LAYER_COUNTER = 1

            while randomSkip != 2:
                exec("self.last{0} = Node(data)\nself.last{0}.prev = self.head{0}\nself.head{0}.next = self.last{0}\nself.last{0}.down = current\ncurrent.up = self.last{0}".format(LAYER_COUNTER))

                LAYER_COUNTER += 1
                if LAYER_COUNTER == 5:
                    break

                current = current.up
                randomSkip = random.randint(1, 2)

            self.LAYER_0_NODE_DATA.append(data)
        else:
            NODE_INDEX_COUNTER = 0
            for i in self.LAYER_0_NODE_DATA:
                if i > data:
                    self.LAYER_0_NODE_DATA.insert(NODE_INDEX_COUNTER, data)
                    break

                NODE_INDEX_COUNTER += 1
            
            NEW_LAST_NODE = False
            if NODE_INDEX_COUNTER == len(self.LAYER_0_NODE_DATA):
                NEW_LAST_NODE = True
                self.LAYER_0_NODE_DATA.append(data)

            PREV_TRACK = self.search(self.LAYER_0_NODE_DATA[NODE_INDEX_COUNTER - 1], False)

            APPEND_NODE = Node(data)
            APPEND_NODE.prev = PREV_TRACK
            APPEND_NODE.next = PREV_TRACK.next

            if PREV_TRACK.next:
                PREV_TRACK.next.prev = APPEND_NODE
            PREV_TRACK.next = APPEND_NODE

            randomSkip = random.randint(1, 2)
            LAYER_COUNTER = 1
            current = PREV_TRACK.next

            if NEW_LAST_NODE:
                self.last0 = self.last0.next

            while randomSkip != 2:
                while not PREV_TRACK.up:
                    PREV_TRACK = PREV_TRACK.prev

                PREV_TRACK = PREV_TRACK.up

                if NEW_LAST_NODE:
                    exec("if not self.head{0}.next:\n\tAPPEND_NODE = self.last{0}".format(LAYER_COUNTER))
                else: 
                    APPEND_NODE = Node(data)

                APPEND_NODE.prev = PREV_TRACK
                APPEND_NODE.next = PREV_TRACK.next
                APPEND_NODE.down = current
                current.up = APPEND_NODE

                if PREV_TRACK.next:
                    PREV_TRACK.next.prev = APPEND_NODE
                
                PREV_TRACK.next = APPEND_NODE

                LAYER_COUNTER += 1
                if LAYER_COUNTER == 5:
                    break
                
                randomSkip = random.randint(1, 2) 
                current = current.up
    def delete(self, data):
        current = self.search(data, False)
        PREV_TRACK = self.search(self.LAYER_0_NODE_DATA[self.LAYER_0_NODE_DATA.index(data)-1], False)

        print(current.data)
        print(PREV_TRACK.data)

        if current.next:
            current.next.prev = PREV_TRACK

        PREV_TRACK.next = current.next
        
        while current.up:
            current = current.up

            while not PREV_TRACK.up:
                PREV_TRACK = PREV_TRACK.prev
            
            PREV_TRACK = PREV_TRACK.up

            if current.next:
                current.next.prev = PREV_TRACK
            
            PREV_TRACK.next = current.next

SL = SkipList()


for i in range(1, 21):
    SL.append(i)

print(SL.last0.data)

for i in range(5):
    print() 

SL.display()
