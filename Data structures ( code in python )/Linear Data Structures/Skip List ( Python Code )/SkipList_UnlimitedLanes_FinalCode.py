import math
import random
import itertools

class Node(object):
    def __init__(self, data):
        self.data = data
        
        self.next = None 
        self.prev = None
        self.down = None
        self.up = None 

class SkipList(object):
    def __init__(self, NUMBER_OF_LANES):
        '''

        ( ~ Description ( how the method looks ) -> return value [ done(x) / undone(empty) ]

        ##################### GENERAL METHODS ####################
        
        ~ Get length                                                                        ( self.getLength(lane) )                                                -> integer                  [x]
        ~ Create __len__(self) method                                                       ( len(self) )                                                           -> integer                  [x]

        ~ Node at index                                                                     ( self.atIndex(index, lane) )                                           -> Node object              [x]

        ~ Get index of                                                                      ( self.indexOf(node, lane) )                                            -> integer                  [x]
        ~ Get node data list                                                                ( self.getNodeData() )                                                  -> list                     [x]

        ##################### GENERAL METHODS #####################
        ##################### INSERTION / DELETION / SEARCH #####################

        ~ Search                                                                            ( self.search(data, DIRECT_RETURN = True, LAST = False) )               -> None                     [x]

        ~ Append                                                                            ( self.append(data) )                                                   -> None                     []

        ~ Delete node                                                                       ( self.deleteNode(node) )                                               -> None                     []
        ~ Delete at index                                                                   ( self.deleteAtIndex(index, lane) )                                     -> None                     []
        ~ Delete node with data                                                             ( self.deleteNodeWithData(data) )                                       -> None                     []

        ##################### INSERTION / DELETION / SEARCH #####################
        ##################### OTHERS #####################

        ~ Merge                                                                             ( self.merge(MERGE_SKIP_LIST ) )                                        -> None                     []

        ~ Remove duplicates                                                                 ( self.removeDuplicates() )                                             -> None                     []
        ~ Is palindrome                                                                     ( self.isPalindrome(lane) )                                             -> None                     []
        ~ Sum with another skip list                                                        ( self.sumWith(SUM_SKIP_LIST, lanes_MAIN, lanes_SUM) )                  -> None                     []

        ~ Split skip list in half                                                           ( self.splitInHalf(lane) )                                              -> [ list_1, list_2 ]       []
        ~ Split skip list after node                                                        ( self.splitAfterNode(lane, node ) )                                    -> [ list_1, list_2 ]       []
        ~ Split skip list at index                                                          ( self.slitAtIndex(lane, index) )                                       -> [ list_1, list_2 ]       []

        ~ Pairs with sum                                                                    ( self.pairsWithSum(target_sum, lane) )                                 -> None                     []
    
        ##################### OTHERS #####################

        '''

        '''
        Create the head & last nodes. By default they will all be the same, -math.inf 
        So, we will execute this string in range of the number of lanes, so that, for each lane that the user wants, by default we already create the 
        head & last nodes. The string will be:
        
        self.head{LAYER_LEVEL} = Node(-math.inf)
        self.last{LAYER_LEVLE} = Node(-math.inf)
        '''
        
        # *NOTE* --------- > LAYER & LANE are the same thing #

        # Check the given NUMBER_OF_LANES.
        if not NUMBER_OF_LANES >= 2:
            raise ValueError("The skip list must have at least 2 lanes. The NUMBER_OF_LANES argument that you gave was : {0}. Please check that.".format(NUMBER_OF_LANES))
        else:
            self.NUMBER_OF_LANES = NUMBER_OF_LANES

        # Create the head & last nodes
        for LAYER_LEVEL in range(NUMBER_OF_LANES):
            exec("self.head{0} = Node(-math.inf)\nself.last{0} = Node(-math.inf)".format(LAYER_LEVEL))
        
        # Create the connections between the head & last nodes ( .down & .up )
        for LAYER_LEVEL in range(NUMBER_OF_LANES):
            if LAYER_LEVEL == 0:
                self.head0.up = self.head1
                self.last0.up = self.last1
            elif LAYER_LEVEL == NUMBER_OF_LANES - 1:
                exec("self.head{0}.down = self.head{1}\nself.last{0}.down = self.last{1}".format(LAYER_LEVEL, LAYER_LEVEL-1))
            else:
                '''
                STRING TO EXECUTE:
    
                self.head{LAYER_LEVEL}.down = self.head{LAYER_LEVEL-1}
                self.head{LAYER_LEVEL}.up = self.head{LAYER_LEVEL+1}

                self.last{LAYER_LEVEL}.down = self.last{LAYER_LEVEL-1}
                self.last{LAYER_LEVEL}.up = self.last{LAYER_LEVEL+1}
                '''
                
                exec("self.head{0}.down = self.head{1}\nself.head{0}.up = self.head{2}\nself.last{0}.down = self.last{1}\nself.last{0}.up = self.last{2}".format(LAYER_LEVEL, LAYER_LEVEL-1, LAYER_LEVEL+1))
        
        '''
        Store all the layers node data & length + height in a self.LAYERS_DATA list
        
        We will create a self.LAYERS_DATA, where, the first lane ( 0'th lane ) will look like this :

        0 : [ [NODE_DATA_1, NODE_DATA_2, ...], [NODE_HEIGHT_1, NODE_HEIGHT_2, ...], LENGTH_OF_THE_LAYER ]

        The other lanes will look like this:

        1, 2, ... : [ [NODE_DATA_1, NODE_DATA_2, ... ], LENGTH_OF_THE_LAYER ]

        ** - > by default they all have the length 1 & the node data -math.inf in the node data list. On layer 0, the first length if the NUMBER_OF_LANES, as this is how high the head nodes go up
        '''
        
        self.LAYERS_DATA = {
            0 : [ [-math.inf], [NUMBER_OF_LANES], 1 ]
        }

        # Iterate till we reach the maximum number of nodes while adding to the self.LAYERS_DATA
        for LAYER_LEVEL in range(1, NUMBER_OF_LANES):
            self.LAYERS_DATA[LAYER_LEVEL] = [ [-math.inf], 1 ]
        
    ##################### GENERAL METHODS ####################

    def getLength(self, lane):
        ''' Return the number of nodes on the given lane '''
        # Check the given lane
        if not 0 <= lane < self.NUMBER_OF_LANES:
            raise ValueError("The given lane must be between 0 and {0}. You gave : {1}".format(self.NUMBER_OF_LANES, lane))

        return self.LAYERS_DATA[lane][-1]
    
    def __len__(self):
        ''' Returns the number of nodes in the entire skip list ( on all the lanes ) '''
        COUNTER = 0
        for LAYER_DATA in self.LAYERS_DATA:
            COUNTER += LAYER_DATA[-1]

        return COUNTER

    def atIndex(self, index, lane):
        ''' Return the given node at the given index on the given lane '''
        # Check the given lane
        if not 0 <= lane < self.NUMBER_OF_LANES:
            raise ValueError("The given lane must be between 0 and {0}. The lane that you gave was : {1}".format(self.NUMBER_OF_LANES-1, lane))
        
        # Check the given index
        if not 0 <= index < self.LAYERS_DATA[lane][-1]:
            raise IndexError("The given index was either too big or too small for the given lane. It must be something between 0 and {0}. The given index was {1}".format(self.LAYERS_DATA[lane][-1]-1,index))

        # Return the node data at the given index on the given lane
        return self.LAYERS_DATA[lane][0][index]
    
    def indexOf(self, node, lane):
        ''' Return the index of the given node on the given lane '''
        # Check the given lane
        if not 0 <= lane < self.NUMBER_OF_LANES:
            raise ValueError("The given lane must be between 0 and {0}. The lane that you gave was : {1}".format(self.NUMBER_OF_LANES-1, lane))

        # Check the given node
        if type(node) != Node:
            raise ValueError("The given node must be of type node. The given 'node' was {0} which has a type of {1}".format(node, str(type(node))))

        # Keep track of the current index while iterating through the given lane.
        current = eval("self.head{0}".format(lane))
        index = 0

        while current:
            if current == node:
                return index

            current = current.next
            index += 1

        # If we passed the while loop, that means that we didn't return the index, so, that means that the given node couldn't be found on the given lane. We will raise a value error because of that
        raise ValueError("The given node couldn't be found on the given lane. The node data was {0} and the given lane was {1}".format(node.data, lane))

    def getNodeData(self):
        ''' Return a nested list. Each list in the nested list represents all the node data on a specific layer. The first list has the node data of the first layer ( the 0'th layer ) and, while we go through the list we increment the layer level '''

        LAYER_DATA = list()

        for LAYER_LEVEL in range(self.NUMBER_OF_LANES):
            LAYER_DATA.append(self.LAYERS_DATA[LAYER_LEVEL][0])

        return LAYER_DATA

    ##################### GENERAL METHODS ####################
    ##################### INSERTION / DELETION / SEARCH #####################
    
    def search(self, data, DIRECT_RETURN = True, LAST = False):
        ''' Return a node with the given data. For more information about the DIRECT_RETURN & LAST argument read the their description in the method '''
        '''
        DESCRIPTION : ~ DIRECT_RETURN ~
        When we found a node with the given data, if DIRECT_RETURN is True we will return a node on the layer with the same DATA
        If DIRECT_RETURN is False, we will 'dig down' and return a node on the *FIRST LAYER* with the given data
        '''
        '''
        DESCRIPTION : ~ LAST ~
        When we find a node, while the next node in front of it has the same data ( example -math.inf <-> 1 <-> 2 <-> 2 <-> 2 ), we will iterate in front, till we find a node that doesn't have the same data or we reach the end
        '''
        
        # Start at the head on the last layer
        prev = None
        current = eval("self.head{0}".format(self.NUMBER_OF_LANES - 1))

        while current:
            if current.data == data:
                if DIRECT_RETURN:
                    if LAST:
                        while current.next:
                            if current.next == data:
                                current = current.next
                            else:
                                break

                        return current
                    else:
                        return current
                else:
                    # Dig down to the first layer
                    while current.down:
                        current = current.down

                    if LAST:
                        while current.next:
                            if current.next == data:
                                current = current.next
                            else:
                                break

                    return current
            elif current.data < data and current.next:
                prev = current
                current = current.next
            elif ( current.data < data and not current.next ) or ( current.data > data and not prev ):
                current = current.down
                prev = None
            elif current.data > data and prev:
                current = prev.down
                prev = None
    
    def append(self, data):
        ''' Append a node with the given data. It is sorted automatically '''
        # Check if the skip list have last nodes. They are normally -math.inf, but that means that they don't have any connection with the head nodes, so we will have to rebuild them 
        if not self.head0.next:
            # Rebuild the last node on the first layer and change it's connections with the head
            self.last0 = Node(data)

            self.last0.prev = self.head0
            self.head0.next = self.last0
            
            # Update the self.LAYERS_DATA dict
            self.LAYERS_DATA[0][0].append(data) # NODE DATA LIST
            self.LAYERS_DATA[0][1].append(1)    # HEIGHT OF THE NODE ( by default is 1 because we didn't go up on the other lanes with it yet )
            self.LAYERS_DATA[0][-1] += 1        # INCREMENT THE LENGTH OF THE LIST

            current = self.last0
            LAYER_LEVEL = 1
            randomSkip = random.randint(1, 2)

            while randomSkip != 2:
                # GET THE HEAD & LAST NODES -- > set up their pointers after creating a new last node
                '''
                STRING TO EXEC :

                self.last{LAYER_LEVEL} = Node(data)

                self.last{LAYER_LEVEL}.prev = self.head{LAYER_LEVEL}
                self.last{LAYER_LEVEL}.down = current
                current.up = self.last{LAYER_LEVEL}

                self.head{LAYER_LEVEL}.next = self.last{LAYER_LEVEL}
                '''

                exec("self.last{0} = Node(data)\nself.last{0}.prev = self.head{0}\nself.last{0}.down = current\ncurrent.up = self.last{0}\nself.head{0}.next = self.last{0}".format(LAYER_LEVEL))
                
                # Update self.LAYERS_DATA
                self.LAYERS_DATA[0][1][-1] += 1                 # Increment the length of the node on layer 0
                self.LAYERS_DATA[LAYER_LEVEL][0].append(data)   # NODE DATA LIST 
                self.LAYERS_DATA[LAYER_LEVEL][-1] += 1          # Length of the lane

                # Update the current node ( to go up ) & the randomSkip value
                current = current.up
                randomSkip = random.randint(1, 2)

                LAYER_LEVEL += 1
                if LAYER_LEVEL == self.NUMBER_OF_LANES:
                    break

    ##################### INSERTION / DELETION / SEARCH #####################

SL = SkipList(5)

##################################### TEST CODE #####################################

SL.append(5)

##################################### TEST CODE #####################################

for i in range(3):
    print()

##################################### HEAD & LAST NODES #####################################

print("HEAD & LAST NODES -- > ")
print()
for LAYER_LEVEL in range(SL.NUMBER_OF_LANES-1, -1, -1):
    print("{0} -- > {1} // {2}".format(LAYER_LEVEL, eval("SL.head{0}.data".format(LAYER_LEVEL)), eval("SL.last{0}.data".format(LAYER_LEVEL))))
print()
print("< -- HEAD & LAST NODES ")

##################################### HEAD & LAST NODES #####################################

for i in range(5):
    print()

##################################### AUTOMATIC ITERATION #####################################

print("AUTOMATIC ITERATION -- > ")
print()
for LAYER_LEVEL in range(SL.NUMBER_OF_LANES-1, -1, -1):
    NODE_DATA_LIST = list()
    exec("current = SL.head{0}\nwhile current:\n\tNODE_DATA_LIST.append(current.data)\n\tcurrent = current.next".format(LAYER_LEVEL))
    print("{0} -- > {1}".format(LAYER_LEVEL, NODE_DATA_LIST))
print()
print("< -- AUTOMATIC ITEARTION ")

##################################### AUTOMATIC ITERATION #####################################

for i in range(5):
    print()

##################################### LAYERS DATA #####################################

print("LAYERS DATA -- > ")
print()
for LAYER_LEVEL in list(SL.LAYERS_DATA.keys())[::-1]:
    print("{0} -- > {1}".format(LAYER_LEVEL, SL.LAYERS_DATA[LAYER_LEVEL]))
print()
print("< -- LAYERS DATA ")

##################################### LAYERS DATA #####################################

for i in range(3):
    print()
