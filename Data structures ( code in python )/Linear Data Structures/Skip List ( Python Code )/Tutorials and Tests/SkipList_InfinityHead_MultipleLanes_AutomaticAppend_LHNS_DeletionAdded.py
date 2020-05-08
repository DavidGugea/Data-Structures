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
        for LAYER_COUNTER in range(5):
            exec("self.head{0} = Node(-math.inf)\nself.last{0} = Node(-math.inf)".format(LAYER_COUNTER))
        for LAYER_COUNTER in range(5):
            if LAYER_COUNTER == 0:
                self.head0.down = None
                self.head0.up = self.head1

                self.last0.down = None
                self.last0.up = self.last1
            elif LAYER_COUNTER == 4:
                self.head4.down = self.head3
                self.head4.up = None
                
                self.last4.down = self.last3
                self.last4.up = None
            else:
                exec("self.head{0}.down = self.head{1}\nself.head{0}.up = self.head{2}\nself.last{0}.down = self.last{1}\nself.last{0} = self.last{2}".format(LAYER_COUNTER, LAYER_COUNTER-1, LAYER_COUNTER+1))

        self.LAYER_0_NODE_DATA = [-math.inf] 

    def display(self):
        LAYERS_NODE_DATA = self.getNodeData()

        for i in range(4, -1, -1):
            print("Layer {0} -- > {1}".format(i, LAYERS_NODE_DATA[i]))

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
                current = START_CURRENT.down
                START_CURRENT = current
                prev = None

    def append(self, data):
        NODE_DATA_INDEX = 0
        for i in self.LAYER_0_NODE_DATA:
            if i > data:
                self.LAYER_0_NODE_DATA.insert(NODE_DATA_INDEX, data)
                break
            
            NODE_DATA_INDEX += 1

        if NODE_DATA_INDEX == len(self.LAYER_0_NODE_DATA):
            self.LAYER_0_NODE_DATA.append(data)

        PREV_TRACK = self.search(self.LAYER_0_NODE_DATA[NODE_DATA_INDEX - 1], False)
        
        if not self.head0.next: # FIRST APPEND     
            self.last0 = Node(data)
            
            self.last0.prev = self.head0
            self.head0.next = self.last0
            
            randomSkip = random.randint(1, 2)
            current = self.head0.next
            LAYER_LEVEL = 1 

            while randomSkip != 2:
                exec("self.last{0} = Node(data)\nself.last{0}.prev = self.head{0}\nself.head{0}.next = self.last{0}\nself.last{0}.down = current\ncurrent.up = self.last{0}".format(LAYER_LEVEL))
                
                LAYER_LEVEL += 1
                if LAYER_LEVEL == 5: break

                randomSkip = random.randint(1, 2)
                current = current.up
        else: # NOT FIRST APPEND ANYMORE
            APPEND_NODE = Node(data)
            APPEND_NODE.prev = PREV_TRACK
            APPEND_NODE.next = PREV_TRACK.next 

            NEW_APPEND_NODE = False

            if PREV_TRACK.next:
                PREV_TRACK.next.prev = APPEND_NODE
            else:
                NEW_APPEND_NODE = True

            PREV_TRACK.next = APPEND_NODE

            if NEW_APPEND_NODE:
                self.last0 = self.last0.next

            # Move up
            randomSkip = random.randint(1, 2)
            current = PREV_TRACK.next
            LAYER_LEVEL = 1

            while randomSkip != 2:
                while not PREV_TRACK.up:
                    PREV_TRACK = PREV_TRACK.prev

                PREV_TRACK = PREV_TRACK.up

                APPEND_NODE = Node(data)
                APPEND_NODE.prev = PREV_TRACK
                APPEND_NODE.next = PREV_TRACK.next
                APPEND_NODE.down = current

                current.up = APPEND_NODE

                CURRENT_HEAD_NODE = eval("self.head{0}".format(LAYER_LEVEL))

                if not CURRENT_HEAD_NODE.next:
                    exec("self.last{0} = APPEND_NODE\nself.last{0}.prev = self.head{0}\nself.head{0}.next = self.last{0}".format(LAYER_LEVEL))
                else:
                    if PREV_TRACK.next:
                        PREV_TRACK.next.prev = APPEND_NODE
                        PREV_TRACK.next = APPEND_NODE
                    else:
                        PREV_TRACK.next = APPEND_NODE
                        exec("self.last{0} = self.last{0}.next".format(LAYER_LEVEL))

                LAYER_LEVEL += 1
                if LAYER_LEVEL == 5: break

                randomSkip = random.randint(1, 2) 
                current = current.up

    def delete(self, data):
        if data == -math.inf: raise ValueError("The data that you have to delete can't be the head node.")

        DELETE_INDEX = self.LAYER_0_NODE_DATA.index(data)

        NODE_TO_DELETE = self.search(self.LAYER_0_NODE_DATA[DELETE_INDEX], False)
        PREV_TRACK = NODE_TO_DELETE.prev

        del self.LAYER_0_NODE_DATA[DELETE_INDEX]

        if NODE_TO_DELETE is self.last0:
            for LAYER_LEVEL in range(5):
                if eval("self.head{0}.next".format(LAYER_LEVEL)):
                    exec("self.last{0}.prev.next = None\nself.last{0} = self.last{0}.prev".format(LAYER_LEVEL))
        else:
            PREV_TRACK.next, NODE_TO_DELETE.next.prev = NODE_TO_DELETE.next, PREV_TRACK            

            LAYER_LEVEL = 1
            while NODE_TO_DELETE:
                while not PREV_TRACK.up:
                    PREV_TRACK = PREV_TRACK.prev
                
                PREV_TRACK = PREV_TRACK.up

                if NODE_TO_DELETE.next:
                    PREV_TRACK.next = NODE_TO_DELETE.next
                    NODE_TO_DELETE.next.prev = PREV_TRACK
                else:
                    exec("self.last{0} = PREV_TRACK".format(LAYER_LEVEL))
                    PREV_TRACK.next = None

                NODE_TO_DELETE = NODE_TO_DELETE.up
                LAYER_LEVEL += 1


SL = SkipList()

for i in range(1, 11):
    SL.append(i)

SL.delete(2)

for i in range(5):
    print()

for LAYER_LEVEL in range(5):
    print("last{0} -- > {1}".format(LAYER_LEVEL, eval("SL.last{0}.data".format(LAYER_LEVEL))))

for i in range(5):
    print()

SL.display()
