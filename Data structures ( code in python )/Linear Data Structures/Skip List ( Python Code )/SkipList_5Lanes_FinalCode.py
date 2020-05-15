import math
import random

class Node(object):
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None
        self.down = None
        self.up = None

class SkipList(object):
    def __init__(self):
        '''

        ( ~ Description ( how the method looks ) -> return value [ done(x) / undone(empty) ]

        ##################### GENERAL METHODS #####################

        ~ Get length                                                                        ( self.getLength(lane) )                                                -> integer                  [x]
        ~ Create __len__(self) method                                                       ( len(self) )                                                           -> integer                  [x]

        ~ Node at index                                                                     ( self.atIndex(index, lane) )                                           -> Node object              [x]
        ~ Get index of                                                                      ( self.indexOf(node, lane) )                                            -> Node object              [x]

        ~ Get node data list                                                                ( self.getNodeData() )                                                  -> list                     [x]

        ##################### GENERAL METHODS #####################
        ##################### INSERTION / DELETION / SEARCH #####################

        ~ Search                                                                            ( self.search(data, DIRECT_RETURN = True) )                             -> None                     [x]

        ~ Append                                                                            ( self.append(data) )                                                   -> None                     [x]

        ~ Delete node                                                                       ( self.deleteNode(node) )                                               -> None                     [x]
        ~ Delete at index                                                                   ( self.deleteAtIndex(index, lane) )                                     -> None                     [x]
        ~ Delete node with data                                                             ( self.deleteNodeWithData(data) )                                       -> None                     [x]

        ##################### INSERTION / DELETION / SEARCH #####################
        ##################### OTHERS #####################

        ~ Node Swap ( input : nodes to be swaped )                                          ( self.swapNodes(NODE_1, NODE_2) )                                      -> None                     []
        ~ Node Swap ( input : indexes of the nodes that need to be swaped )                 ( self.swapNodesAtIndex(INDEX_1, INDEX_2) )                             -> None                     [] 
        # The indexes must be on the lane 0 at the second node swap 

        ~ Reverse                                                                           ( self.reverse() )                                                      -> None                     []
        
        ~ Merge                                                                             ( self.merge(MERGE_SKIP_LIST ) )                                        -> None                     []
        ~ Sort                                                                              ( self.sort() )                                                         -> None                     []

        ~ Remove duplicates                                                                 ( self.removeDuplicates() )                                             -> None                     []
        ~ Rotate                                                                            ( self.rotate() )                                                       -> None                     []

        ~ Is palindrome                                                                     ( self.isPalindrome(lane) )                                             -> None                     []

        ~ Move tail to head                                                                 ( self.moveTailToHead() )                                               -> None                     []
        ~ Sum with another skip list                                                        ( self.sumWith(lane_1, lane_2) )                                        -> None                     []

        ~ Split skip list in half                                                           ( self.splitInHalf(lane) )                                              -> [ list_1, list_2 ]       []
        ~ Split skip list after node                                                        ( self.splitInHalf(lane, node ) )                                       -> [ list_1, list_2 ]       []
        ~ Split skip list at index                                                          ( self.slitAtIndex(lane, index) )                                       -> [ list_1, list_2 ]       []

        ~ Pairs with sum                                                                    ( self.pairsWithSum(target_sum, lane) )                                 -> None                     []
    
        ##################### OTHERS #####################

        '''

        ''' 
        Create the head & last nodes. By default they are all going to be -math.inf ( - Infinity )
        The head nodes never change, they will always be -math.inf, the last nodes will change ot the nodes that are appended on the 5 lanes.

        So we will have 5 head & 5 last nodes :

        self.head0 / self.head1 / self.head2 / self.head3 / self.head4
                                      &
        self.last0 / self.last1/ self.last2 / self.last3 / self.last4

        So, by default they are all -math.inf.
        We don't have to write all the code, we can use the built-in exec function:

        self.head{LAYER_LEVEL} = Node(-math.inf)
        self.last{LAYER_LEVEL} = Node(-math.inf)
        '''

        for LAYER_LEVEL in list(range(0, 5)):
            exec("self.head{0} = Node(-math.inf)\nself.last{0} = Node(-math.inf)".format(LAYER_LEVEL))

        # Create the connections ( .down & .up between the head & last nodes )
        for LAYER_LEVEL in list(range(0, 5)):
            if LAYER_LEVEL == 0:
                self.head0.up = self.head1
                self.last0.up = self.last1
            elif LAYER_LEVEL == 4:
                self.head4.down = self.head3
                self.last4.down = self.last3
            else:
                '''
                EXEC:
                
                self.head{LAYER_LEVEL}.down = self.head{LAYER_LEVEL-1}
                self.head{LAYER_LEVEL}.up = self.head{LAYER_LEVEL+1}

                self.last{LAYER_LEVEL}.down = self.last{LAYER_LEVEL-1}
                self.last{LAYER_LEVEL}.up = self.last{LAYER_LEVEL+1}

                '''

                exec("self.head{0}.down = self.head{1}\nself.head{0}.up = self.head{2}\nself.last{0}.down = self.last{1}\nself.last{0}.up = self.last{2}".format(LAYER_LEVEL, LAYER_LEVEL-1, LAYER_LEVEL+1))

        '''
        self.LAYERS_DATA will be a dictionary that will store various information about the node data in the skip list.
        For the first lane, the '0' lane the k-v-p will look like this:

        0 : [ [ NODE_DATA_1, NODE_DATA_2, ... ], [ HEIGHT_FOR_FIRST_NODE_1, HEIGHT_FOR_SECOND_NODE_2 ], NUMER_OF_NODES_ON_FIRST_LANE ]

        For the other lanes, we won't have the height list, the list that represents how further up does each node go from the first lane ( inclusive ).
        So it will look something like this :

        1 / 2 / 3 / 4 : [ [ NODE_DATA_1, NODE_DATA_2 ... ] , NUMBER_OF_NODES_ON_THE_LANE ]
        '''
        self.LAYERS_DATA = {
            0 : [ [-math.inf], [5], 1 ],
            1 : [ [-math.inf], 1 ],
            2 : [ [-math.inf], 1 ],
            3 : [ [-math.inf], 1 ],
            4 : [ [-math.inf], 1 ]
        }

        # *NOTE* : lane & layer are the same thing #

    ##################### GENERAL METHODS #####################

    def getLength(self, lane):
        ''' Returns the number of nodes on the given lane '''
        # Check the lane argument
        if not 0 <= lane < 5:
            raise ValueError("The given lane must be between 0 and 4")
        
        # Look in the self.LAYERS_DATA on the given lane ( 0 / 1 / 2 / 3 / 4 ) and return the last element of the value, because, regardless of the lane key, all last values on each given lane on self.LAYERS_DATA represents the length of the lane.
        return eval("self.LAYERS_DATA[{0}][-1]".format(lane))

    def __len__(self):
        ''' Returns the number of nodes in the entire skip list '''
        NUMBER_OF_NODES = 0
        
        '''
        Code to execute:

        NUMBER_OF_NODES += self.LAYERS_DATA[{LAYER_LEVEL}][-1]
        '''
        for LAYER_LEVEL in list(range(0, 5)):
            NUMBER_OF_NODES += eval("self.LAYERS_DATA[{0}][-1]".format(LAYER_LEVEL))

        return NUMBER_OF_NODES

    def atIndex(self, index, lane):
        ''' Return the node *DATA* on the given lane at the given index. If you want to get the node, and not it's data, you have to look for the search method '''
        # Check the lane argument
        if not 0 <= lane < 5:
            raise ValueError("The given lane argument must be between 0 and 4 ")

        # Check the index argument ( first get the length on the given lane )
        LENGTH_OF_GIVEN_LANE = eval("self.LAYERS_DATA[{0}][-1]".format(lane))
        
        if not 0 <= index < LENGTH_OF_GIVEN_LANE:
            raise ValueError("The given index is either too small ( < 0 ) or too big for the given lane. The index was {0} and the length of the lane is {1}".format(index, LENGTH_OF_GIVEN_LANE))
    
        return self.LAYERS_DATA[lane][0][index]

    def indexOf(self, node, lane):
        # Check the given node & the given lane
        if type(node) != Node:
            raise ValueError("The given node argument must be of type Node. Its type is : {0}".format(type(node)))
        
        if not 0 <= lane < 5:
            raise ValueError("The given lane is either too big or too small. It must be something between 0 and 4. The given lane argument is : {0}".format(lane))

        # Iterate from the head of the given lane till we find the node while keeping track of the index
        current = eval("self.head{0}".format(lane))
        index = 0

        while current:
            if current == node:
                return index 

            index += 1
            current = current.next

        # If we passed the while loop that means that we didn't return any index. Hence we couldn't find any node on the given lane that was the same as the given node argument. Therefore we must raise a ValueError
        raise ValueError("The given node couldn't be found on the given lane.")

    def getNodeData(self):
        ''' Return a list that contains more lists inside of it, each list represents the node data of a lane. The first list will contain the data of the first lane ( lane number 0 ) and the last list will contain the data of teh last lane ( lane number 4 ) '''

        NODE_DATA_LIST = list()

        for LAYER_LEVEL in list(range(0, 5)):
            NODE_DATA_LIST.append(self.LAYERS_DATA[LAYER_LEVEL])

        return NODE_DATA_LIST

    ##################### GENERAL METHODS #####################
    ##################### INSERTION / DELETION / SEARCH #####################

    def search(self, data, DIRECT_RETURN = True):
        ''' Return the first node found with the given data '''
        # When the DIRECT_RETURN argument is True we will return the node the first time we find it, if it is False, we will 'dig' down till we get the node on the layer 0 and then return it, when it is on the layer 0
        # Start at the head node on the last layer
        prev = None
        current = self.head4
        START_CURRENT = current 
        
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
            elif current.data > data and prev:
                current = prev.down
                prev = None
                START_CURRENT = current
            elif current.data > data and not prev:
                current = START_CURRENT.down
                prev = None
                START_CURRENT = current

        # If we passed the 'while' loop, that means that we didn't return the node, so, we will have to raise a value error because that means that we didn't find any node with the given data
        raise ValueError("The given data couldn't be found in the skip list.")

    def append(self, data):
        ''' Append a new node with the given data. It is automatically sorted in the skip list '''

        # Check if the skip list has a last node on the first layer. By default the last nodes are all -math.inf and they have no connections with the head nodes. So check if that is the case. If that is the case, create the new last nodes
        if not self.head0.next:
            self.last0 = Node(data)

            self.last0.prev = self.head0
            self.head0.next = self.last0

            # Modify the self.LAYERS_DATA for the first lane
            self.LAYERS_DATA[0][0].append(data) # NODE DATA
            self.LAYERS_DATA[0][1].append(1)    # HEIGHT
            self.LAYERS_DATA[0][-1] += 1        # NUMBER OF NODES 
                
            # Go up with the node on the others layers
            current = self.last0 # We created a new last node and we want to go up with it, so we will set a current variable to start at the last node 
            LAYER_LEVEL = 1 # We will start to append new nodes on the first layer ( the 1'th layer ) not on the 0'th layer, so we will have to set the LAYER_LEVEL to be 1
            randomSkip = random.randint(1, 2)

            while randomSkip != 2:
                '''
                EXEC STRING:

                self.last{LAYER_LEVEL} = Node(data)

                self.last{LAYER_LEVEL}.prev =  self.head{LAYER_LEVEL}
                self.head{LAYER_LEVEL}.next = self.last{LAYER_LEVEL}

                self.last{LAYER_LEVEL}.down = current
                current.up = self.last{LAYER_LEVEL}
                '''

                exec("self.last{0} = Node(data)\nself.last{0}.prev = self.head{0}\nself.head{0}.next = self.last{0}\nself.last{0}.down = current\ncurrent.up = self.last{0}".format(LAYER_LEVEL))

                # Update self.LAYERS_DATA
                self.LAYERS_DATA[0][1][-1] += 1 # Update the height of the last node on layer 0
                self.LAYERS_DATA[LAYER_LEVEL][0].append(data) # NODE DATA
                self.LAYERS_DATA[LAYER_LEVEL][-1] += 1      # Number of nodes on the first lane

                # Update current & layer level ( + check if it reached the limit ) & create new random skip
                current = current.up
                randomSkip = random.randint(1, 2)

                LAYER_LEVEL += 1
                if LAYER_LEVEL == 5: 
                    # We will break it at 5 and not at 6 because we have self.head0 / self.head1 / self.head 2 / self.head3 / self.head4 & the same for the last nodes. We start with 0 and end with 4, so we have 5 lanes so break if it has reached the limit
                    break
        else:
            # Search for the first node data on layer 0 that has a bigger value than the node data that we want to append
            PREV_NODE_DATA = str()   # By default it is an empty string. If after the first iteration, it is still an empty string, that means that we couldn't find a node that is bigger than the node data that we want to append. That would mean that the node data that we want to append, has to be appended at the end.
            INDEX_TRACK = 0          # Keep track of the index while iterating through the node data
            IS_NEW_LAST_NODE = False # If the node data that we want to append is the biggest in the skip list, set the boolean value for this variable to True

            # When a place for the append node data is found, insert in on layer 0 on the self.LAYERS_DATA
            for NODE_DATA in self.LAYERS_DATA[0][0]:
                if NODE_DATA > data:
                    PREV_NODE_DATA = self.LAYERS_DATA[0][0][INDEX_TRACK - 1]

                    # Insert the new node data on layer 0 in the self.LAYERS_DATA
                    self.LAYERS_DATA[0][0].insert(INDEX_TRACK, data)

                    # Insert the new node height on layer 0 in the self.LAYERS_DATA
                    self.LAYERS_DATA[0][1].insert(INDEX_TRACK, 1)

                    break

                INDEX_TRACK += 1

            if not PREV_NODE_DATA:
                PREV_NODE_DATA = self.last0.data

                # Append the node data on layer 0 in the self.LAYERS_DATA
                self.LAYERS_DATA[0][0].append(data)

                # Append a new height for the node on layer 0 in the self.LAYERS_DATA
                self.LAYERS_DATA[0][1].append(1)

                # It is a new last node, since we had to append it and we couldn't find a bigger node data in the first iteration
                IS_NEW_LAST_NODE = True

            # Increment the number of nodes on the first lane
            self.LAYERS_DATA[0][-1] += 1

            # Get the previous node using the PREV_NODE_DATA string, DIRECT_RETURN has to be set to False because we need the node on the first lane ( 0'th lane )
            PREV_NODE = self.search(PREV_NODE_DATA, False)

            # Create the append node
            APPEND_NODE = Node(data)

            APPEND_NODE.prev = PREV_NODE
            APPEND_NODE.next = PREV_NODE.next

            if PREV_NODE.next:
                PREV_NODE.next.prev = APPEND_NODE

            PREV_NODE.next = APPEND_NODE

            if IS_NEW_LAST_NODE:
                self.last0 = self.last0.next
            
            # Go up with the node
            current = APPEND_NODE
            LAYER_LEVEL = 1
            randomSkip = random.randint(1, 2)
            
            while randomSkip != 2:
                # Find the prev node that still has an .up value and update it 
                while not PREV_NODE.up:
                    PREV_NODE = PREV_NODE.prev

                PREV_NODE = PREV_NODE.up

                # Check if the current head node has a next value, so if there is a last node on the layer that is not -math.inf
                HEAD_NODE = eval("self.head{0}".format(LAYER_LEVEL))

                if not HEAD_NODE.next:
                    LAST_NODE = eval("self.last{0}".format(LAYER_LEVEL))
                    LAST_NODE.data = data

                    LAST_NODE.prev = HEAD_NODE
                    LAST_NODE.down = current
                    LAST_NODE.up = None

                    HEAD_NODE.next = LAST_NODE
            
                    current.up = LAST_NODE
                else:
                    APPEND_NODE = Node(data)

                    APPEND_NODE.prev = PREV_NODE
                    APPEND_NODE.next = PREV_NODE.next
                    APPEND_NODE.down = current

                    current.up = APPEND_NODE

                    IS_NEW_LAST_NODE = False

                    if PREV_NODE.next:
                        PREV_NODE.next.prev = APPEND_NODE
                    else:
                        IS_NEW_LAST_NODE = True

                    PREV_NODE.next = APPEND_NODE
                
                    if IS_NEW_LAST_NODE:
                        exec("self.last{0} = self.last{0}.next".format(LAYER_LEVEL))

                # Update layers data
                self.LAYERS_DATA[0][1][INDEX_TRACK] += 1 # UPDATE HEIGHT OF THE NODE ON LAYER 0
                self.LAYERS_DATA[LAYER_LEVEL][0].insert(INDEX_TRACK, data) # Node data
                self.LAYERS_DATA[LAYER_LEVEL][-1] += 1 # INCREMENT LENGTH OF LANE

                randomSkip = random.randint(1, 2) 
                current = current.up
                
                LAYER_LEVEL += 1
                if LAYER_LEVEL == 5: break
                
    def deleteNode(self, node):
        ''' Delete the given node '''
        # Check the given node
        if type(node) != Node:
            raise ValueError("The given node must be of type node. The type of the node that you gave was : {0}".format(str(type(node))))

        # Make sure that the node is on layer 0
        while node.down:
            node = node.down
        
        LAYER_LEVEL = 0
        current = node
        PREV_NODE = node.prev
        
        # Delete the height of the node on layer 0
        del self.LAYERS_DATA[0][1][self.indexOf(node, 0)]
    
        while current:
            # Update self.LAYERS_DATA
            del self.LAYERS_DATA[LAYER_LEVEL][0][self.indexOf(current, LAYER_LEVEL)] # Update the node data list
            self.LAYERS_DATA[LAYER_LEVEL][-1] -= 1 # Decrement the length of the lane
            
        
            # Find out if the node that we want to delete is the last node. If it is the last node then, after we will delete it, the last node will remain the previous node before the node that we wanted to delete, that is in our case PREV_NODE
            IS_LAST_NODE = False
            
            # Find out if we have the last node, if we don't have the last node then update the .prev pointer of the node after the node that we want to delete to be the previous node of the node that we want to delete, so PREV_NODE
            if current.next:
                current.next.prev = PREV_NODE
            else:
                IS_LAST_NODE = True
            
            # Update the .next pointer of the previous node 
            PREV_NODE.next = current.next
            
            # Update the last node to be PREV_NODE in case of IS_LAST_NODE
            if IS_LAST_NODE:
                exec("self.last{0} = PREV_NODE".format(LAYER_LEVEL))
            
            # Update the current & the previous node
            current = current.up
            if current:
                PREV_NODE = current.prev
            
            # Increment the layer level
            LAYER_LEVEL += 1

    def deleteAtIndex(self, index, lane):
        # Check the lane
        if not 0 <= lane < 5:
            raise ValueError("The given lane must be something between 0 & 4. You gave : {0}".format(lane))
        
        # Check the index
        if not 0 <= index < self.LAYERS_DATA[lane][-1]:
            raise ValueError("The given index is either too big or too small for the given lane. The given index was {0} and the length of the lane was {1}".format(index, self.LAYERS_DATA[lane][-1]))

        # Get the node at the given index on the given lane
        NODE_TO_DELETE = self.atIndex(index, lane)

        # Delete it 
        self.deleteNode(NODE_TO_DELETE)

    def deleteNodeWithData(self, data):
        # Look on the first lane ( 0'th lane ) for the first node that has this data
        current = self.head0
        while current:
            if current.data == data:
                # Delete the node
                self.deleteNode(current)
                return

            current.next
            
        # If we passed the while loop, that means that we didn't delete any node because we didn't find any node to match the given data. So we can raise a value error
        raise ValueError("The given data couldn't be found in the skip list.")

    ##################### INSERTION / DELETION / SEARCH #####################

SL = SkipList()

SL.append(1)
SL.append(2)


for i in range(3):
    print()

for LAYER_LEVEL in list(range(4, -1, -1)):
    HEAD = eval("SL.head{0}".format(LAYER_LEVEL))
    LAST = eval("SL.last{0}".format(LAYER_LEVEL))

    print("LAYER LEVEL {0} -- > {1} // {2}".format(LAYER_LEVEL, HEAD.data, LAST.data))

for i in range(2):
    print()

for LAYER_LEVEL in list(range(4, -1, -1)): 
    NODE_DATA = list()

    exec("current = SL.head{0}\nwhile current:\n\tNODE_DATA.append(current.data)\n\tcurrent = current.next".format(LAYER_LEVEL))

    print("{0} -- > {1}".format(LAYER_LEVEL, NODE_DATA))

for i in range(2):
    print()

COUNTER = 4
for VALUE in SL.getNodeData()[::-1]:
    print("{0} -- > {1}".format(COUNTER, VALUE))
    COUNTER -= 1

for i in range(5):
    print()

SL.deleteNode(SL.last0)

for i in range(5):
    print()

for LAYER_LEVEL in list(range(4, -1, -1)):
    HEAD = eval("SL.head{0}".format(LAYER_LEVEL))
    LAST = eval("SL.last{0}".format(LAYER_LEVEL))

    print("LAYER LEVEL {0} -- > {1} // {2}".format(LAYER_LEVEL, HEAD.data, LAST.data))

for i in range(2):
    print()


for LAYER_LEVEL in list(range(4, -1, -1)): 
    NODE_DATA = list()

    exec("current = SL.head{0}\nwhile current:\n\tNODE_DATA.append(current.data)\n\tcurrent = current.next".format(LAYER_LEVEL))

    print("{0} -- > {1}".format(LAYER_LEVEL, NODE_DATA))

for i in range(2):
    print()

COUNTER = 4
for VALUE in SL.getNodeData()[::-1]:
    print("{0} -- > {1}".format(COUNTER, VALUE))
    COUNTER -= 1
