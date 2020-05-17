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

        ~ Append                                                                            ( self.append(data) )                                                   -> None                     [x]

        ~ Delete node                                                                       ( self.deleteNode(node) )                                               -> None                     [x]
        ~ Delete at index                                                                   ( self.deleteAtIndex(index, lane) )                                     -> None                     [x]
        ~ Delete node with data                                                             ( self.deleteNodeWithData(data) )                                       -> None                     [x]

        ##################### INSERTION / DELETION / SEARCH #####################
        ##################### OTHERS #####################

        ~ Merge                                                                             ( self.merge(MERGE_SKIP_LIST ) )                                        -> None                     [x]

        ~ Remove duplicates                                                                 ( self.removeDuplicates() )                                             -> None                     [x]
        ~ Sum with another skip list                                                        ( self.sumWith(SUM_SKIP_LIST, lanes_MAIN, lanes_SUM) )                  -> None                     [x]

        ~ Split skip list in half                                                           ( self.splitInHalf(lane) )                                              -> [ list_1, list_2 ]       [x]
        ~ Split skip list after node                                                        ( self.splitAfterNode(lane, node ) )                                    -> [ list_1, list_2 ]       [x]
        ~ Split skip list at index                                                          ( self.split(lane, index) )                                             -> [ list_1, list_2 ]       [x]

        ~ Pairs with sum                                                                    ( self.pairsWithSum(target_sum, lane) )                                 -> None                     [x]
    
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
                            if current.next.data == data:
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
   
        # If we passed the loop without returning anything, then raise a value error
        raise ValueError("The given node data couldn't be found in the skip list.")

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
        else:
            # Search for the first node data that is bigger than or equal to the node data that we want to append on layer 0.
            PREV_NODE_DATA = None
            index = 0
            IS_LAST_NODE = False 

            for LAYER_DATA in self.LAYERS_DATA[0][0]:
                if LAYER_DATA >= data:
                    PREV_NODE_DATA = self.LAYERS_DATA[0][0][index - 1]
                    break

                index += 1
            
            # If we passed the for loop and we still couldn't find a node data that is bigger than the node data that we want to append, that means that the node data that we want to append is the biggest, so the PREV_NODE_DATA will be the data of the last node
            if not PREV_NODE_DATA: PREV_NODE_DATA = self.last0.data

            # Update self.LAYERS_DATA
            self.LAYERS_DATA[0][0].insert(index, data)  # NODE DATA LIST
            self.LAYERS_DATA[0][1].insert(index, 1)     # Height of the node ( defaults to 1 because we didn't go up on the layers with it yet )
            self.LAYERS_DATA[0][-1] += 1                # Increment the length of the lane

            # Get the prev node using the found PREV_NODE_DATA
            PREV_NODE = self.search(PREV_NODE_DATA, DIRECT_RETURN = False, LAST = True) # We will set the DIRECT_RETURN to be False because we need the node to be on layer 0
        
            # Create the append node and set its properties and the other properties of the needed nodes (PREV_NODE & PREV_NODE.next), in order to insert it at the right place
            APPEND_NODE = Node(data)

            APPEND_NODE.prev = PREV_NODE
            APPEND_NODE.next = PREV_NODE.next
    
            if PREV_NODE.next:
                PREV_NODE.next.prev = APPEND_NODE 
            else:
                IS_LAST_NODE = True
            
            PREV_NODE.next = APPEND_NODE

            if IS_LAST_NODE:
                self.last0 = self.last0.next

            # Go up with the node on the other layers
            current = PREV_NODE.next
            LAYER_LEVEL = 1
            randomSkip = random.randint(1, 2)
            START_INDEX = index # Keep the current index of the APPEND_NODE stored in a variable so we will be able to increase the update the height of the node on layer 0 on self.LAYERS_DATA when it goes up

            while randomSkip != 2:
                # Update the PREV_NODE
                while not PREV_NODE.up:
                    # Since the we can't update the prev node to go up with it on the other lanes, that means that we have to move backwards with the PREV_NODE, so we will also have to decrement the index of the node that we want to append

                    index -= 1
                    PREV_NODE = PREV_NODE.prev

                PREV_NODE = PREV_NODE.up

                # Get the HEAD NODE on the current lane and see if it has a .next property. If it doesn't have a .next property then, that means that there is no last node, rather than the default one with -math.inf data
                HEAD_NODE = eval("self.head{0}".format(LAYER_LEVEL))

                if not HEAD_NODE.next:
                    '''
                    EXEC STRING:
                    
                    self.last{LAYER_LEVEL} = Node(data)

                    self.last{LAYER_LEVEL}.prev = self.head{LAYER_LEVEL}
                    self.last{LAYER_LEVEL}.down = current
                    current.up = self.last{LAYER_LEVEL}

                    self.head{LAYER_LEVEL}.next = self.last{LAYER_LEVEL}

                    '''
                    
                    exec("self.last{0} = Node(data)\nself.last{0}.prev = self.head{0}\nself.last{0}.down = current\nself.head{0}.next = self.last{0}\ncurrent.up = self.last{0}".format(LAYER_LEVEL))
                else:
                    # Create the append node and set up its properties + the properties of the needed nodes in order to insert it ( PREV_NODE & PREV_NODE.next 
                    IS_NEW_LAST_NODE_ON_CURRENT_LANE = False

                    APPEND_NODE = Node(data)
                    APPEND_NODE.prev = PREV_NODE
                    APPEND_NODE.next = PREV_NODE.next
                    APPEND_NODE.down = current
                    current.up = APPEND_NODE

                    if PREV_NODE.next:
                        PREV_NODE.next.prev = APPEND_NODE
                    else:
                        IS_NEW_LAST_NODE_ON_CURRENT_LANE = True

                    PREV_NODE.next = APPEND_NODE

                    if IS_NEW_LAST_NODE_ON_CURRENT_LANE:
                        exec("self.last{0} = self.last{0}.next".format(LAYER_LEVEL))

                # UPDATE self.LAYERS_DATA
                self.LAYERS_DATA[LAYER_LEVEL][0].insert(index, data) # NODE DATA LIST
                self.LAYERS_DATA[LAYER_LEVEL][-1] += 1               # Increment the length of the lane
    
                self.LAYERS_DATA[0][1][START_INDEX] += 1             # Increment the height of the node on lane 0        

                # Update the current node & randomSkip & LAYER_LEVEL ( check if it has reached the limit )
                current = current.up
                randomSkip = random.randint(1, 2) # !!!!!!!!!!!! change to random.randint(1, 2) after testing it !!!!!!!!!!!!
                
                LAYER_LEVEL += 1
                if LAYER_LEVEL == self.NUMBER_OF_LANES - 1:
                    # We write self.NUMBER_OF_LANES - 1 and not just self.NUMBER_OF_LANES because we start with the head & last nodes from 0 ( example : self.head0 & self.last0 ) and if we have for example 5 lanes, then we will end with : self.head4 & self.last4, so we will have self.head{self.NUMBER_OF_LANES-1} & self.last{self.NUMBER_OF_LANES-1}. So that's why we write self.NUMBER_OF_LANES - 1
                    break

    def deleteNode(self, node):
        ''' Delete the given node '''

        # Check the given node 
        if type(node) != Node:
            raise ValueError("The given node must be of type node. The node argument that you gave was {0} which is of type {1}".format(node, str(type(node))))

        # Make sure that the given node is on lane 0
        while node.down:
            node = node.down

        LAYER_LEVEL = 0
        current = node

        # Update self.LAYERS_DATA
        del self.LAYERS_DATA[0][1][self.indexOf(node, LAYER_LEVEL)] # Delete the height of the node on the first layer

        while current:
            INDEX_OF_DELETE_NODE = self.indexOf(current, LAYER_LEVEL)
            
            # Update self.LAYERS_DATA
            del self.LAYERS_DATA[LAYER_LEVEL][0][INDEX_OF_DELETE_NODE]   # Delete from node data list, the first list on the layer in self.LAYERS_DATA ( [0] )
            self.LAYERS_DATA[LAYER_LEVEL][-1] -= 1                       # Decrement the length of the lane
            
            PREV_NODE = current.prev

            PREV_NODE.next = current.next
            if current.next:
                current.next.prev = PREV_NODE

            current = current.up
    
            LAYER_LEVEL += 1

    def deleteAtIndex(self, index, lane):
        ''' Delete the given node at the given index. '''

        # Check the given lane 
        if not 0 <= lane < self.NUMBER_OF_LANES:
            raise ValueError("The given lane must be between 0 and {0}. The given lane was : {1}".format(self.NUMBER_OF_LANES - 1, lane))

        # Check the given index
        if not 0 <= index < self.LAYERS_DATA[lane][-1]:
            raise IndexError("The given index must be between 0 and {0}. The given index was : {1}".format(self.LAYERS_DATA[lane][-1], index))

        # Get the node at the given lane by starting at the head node of the given lane and keeping track of the current index
        current = eval("self.head{0}".format(lane))
        currentIndex = 0

        while currentIndex < index:
            current = current.next
            currentIndex += 1
        
        # Delete the node
        self.deleteNode(current)
        
    def deleteNodeWithData(self, data):
        ''' Delete the first node found with the given data '''

        self.deleteNode(self.search(data, True, False)) 


    ##################### INSERTION / DELETION / SEARCH #####################
    ##################### OTHERS #####################

    def merge(self, MERGE_SKIP_LIST):
        ''' Append all the node data that is in the MERGE_SKIP_LIST on layer 0 '''
        # Check the given MERGE_SKIP_LIST
        if type(MERGE_SKIP_LIST) != SkipList:
            raise ValueError("The given MERGE_SKIP_LIST argument must be of type Skip List. The value that you gave at the argument was {0} which is of type {1}".format(MERGE_SKIP_LIST, type(MERGE_SKIP_LIST)))
        
        # *NOTE* : Since the skip list is a randomized data structure, keep in mind that the appended nodes won't keep the same height once they are merge in the main skip list ( self )
        for NODE_DATA in MERGE_SKIP_LIST.LAYERS_DATA[0][0][1:]: # We write [1:] because we don't need the -math.inf
            self.append(NODE_DATA)
    
    def removeDuplicates(self):
        ''' Remove all the duplicate nodes in the skip list '''
        # Make a dictionary with all the node data from the skip list ( that is on layer 0 ) as keys and store how many times they duplicate as values 
        REPEAT_DICT = dict()

        for NODE_DATA in self.LAYERS_DATA[0][0]:
            REPEAT_DICT.setdefault(NODE_DATA, self.LAYERS_DATA[0][0].count(NODE_DATA) - 1)

        for REPETITION_KEY in REPEAT_DICT.keys():
            for timesDuplicated in range(REPEAT_DICT[REPETITION_KEY]):
                self.deleteNodeWithData(REPETITION_KEY)

    def sumWith(self, SUM_SKIP_LIST, lanes_MAIN, lanes_SUM):
        ''' Return the sum between the main skip list ( self ) and the SUM_SKIP_LIST on the given lanes. '''
        '''
        *NOTE* :
        the lanes_MAIN represents the lanes numbers that you want to add on the first lane.

        So if we want to add the integers&floats on the lanes 1, 3 and 4, the lanes_MAIN should look like this : [1, 3, 4]
        It works the same for the lanes_SUM

        Example:

        We have the main skip list with the name 'SL' and the skip list with the name 'mySkipList', and we want to add
        all the numbers from the main skip list on the lanes 1, 2 and 4 with all the numbers from 
        the 'mySkipList' skip list on the lane 2, 3 and 4, so we will write this:
        
        ###########################################################
        #                                                         #
        #    SUM = SL.sumWith(mySkipList, [1, 2, 4], [2, 3, 4])   #
        #                                                         #
        ###########################################################
        '''

        # Check the given SUM_SKIP_LIST
        if type(SUM_SKIP_LIST) != SkipList:
            raise ValueError("The given SUM_SKIP_LIST argument must be a SkipList. You gave {0} which is of type {1}".format(SUM_SKIP_LIST, type(SUM_SKIP_LIST)))

        # Check the given lanes
        CHECK_FUNCTION = lambda node_data : exec("raise ValueError('The given lanes must be something between 0 and {0}') if not 0 <= node_data < {1}".format(self.NUMBER_OF_LANES, self.NUMBER_OF_LANES - 1)) 
        
        map(CHECK_FUNCTION, lanes_MAIN)
        map(CHECK_FUNCTION, lanes_SUM)

        # Get all the node data from all the given lanes
        NodeData_MAIN = list()
        NodeData_SUM  = list()

        for LAYER_LEVEL in lanes_MAIN:
            NodeData_MAIN.extend(self.LAYERS_DATA[LAYER_LEVEL][0])
        
        for LAYER_LEVEL in lanes_SUM:
            NodeData_SUM.extend(SUM_SKIP_LIST.LAYERS_DATA[LAYER_LEVEL][0])

        # Filter out all the numbers from both node data lists
        FILTER_FUNCTION = lambda node_data: type(node_data) == int or type(node_data) == float and node_data != -math.inf

        NodeData_MAIN = list(filter(FILTER_FUNCTION, NodeData_MAIN))
        NodeData_SUM  = list(filter(FILTER_FUNCTION, NodeData_SUM))

        # Return the sum between both lists
        return sum(NodeData_MAIN) + sum(NodeData_SUM)

    def splitInHalf(self, lane):
        ''' Return a list that contains two other lists with the data split in half on the given lane '''
        # Check the given lane
        if not 0 <= lane < self.NUMBER_OF_LANES:
            raise ValueError("The given lane must be between 0 and {0}. You gave : {1}".format(self.NUMBER_OF_LANES - 1, lane))

        LANE_TO_SPLIT = self.LAYERS_DATA[lane][0]
        LENGTH = self.LAYERS_DATA[lane][-1]

        return [ LANE_TO_SPLIT[:LENGTH // 2], LANE_TO_SPLIT[LENGTH // 2:] ]

    def splitAfterNode(self, lane, node):
        ''' Return a list that contains two other lists with the data split after the given node on the given lane '''
        # Check the given lane
        if not 0 <= lane < self.NUMBER_OF_LANES:
            raise ValueError("The given lane must be between 0 and {0}. You gave : {1}".format(self.NUMBER_OF_LANES - 1, lane))

        # Check the given node
        if type(node) != Node:
            raise ValueError("The given node must be of type node. The value that you gave at the 'node' argument was {0} which is of type {1}".format(node, type(node)))

        # Get the index of the given node on the given lane
        indexToSplitAt = self.indexOf(node, lane)

        # Return the split data after the found index
        LANE_TO_SPLIT = self.LAYERS_DATA[lane][0]

        return [ LANE_TO_SPLIT[:indexToSplitAt + 1], LANE_TO_SPLIT[indexToSplitAt + 1:] ]

    def splitAtIndex(self, lane, index):
        ''' Split the given lane data at the given index '''
        # Check the given lane
        if not 0 <= lane < self.NUMBER_OF_LANES:
            raise ValueError("The given lane must be between 0 and {0}. You gave : {1}".format(self.NUMBER_OF_LANES - 1, lane))

        # Check the given index
        if not 0 <= index < self.LAYERS_DATA[lane][-1]:
            raise IndexError("The given index must be between 0 and {0}. You gave : {1}".format(self.LAYERS_DATA[lane][-1] - 1, index))

        # Return the split data at the found index
        LANE_TO_SPLIT = self.LAYERS_DATA[lane][0]

        return [ LANE_TO_SPLIT[:index], LANE_TO_SPLIT[index:] ]

    def pairsWithSum(self, target_sum, lane):
        ''' Return all the pairs ( two-number pairs ) of numbers on the given lane that match sum to the given target_sum '''
        # Check the given lane
        if not 0 <= lane < self.NUMBER_OF_LANES:
            raise ValueError("The given lane must be between 0 and {0}. You gave : {1}".format(self.NUMBER_OF_LANES - 1, lane))

        # Check the given target_sum
        try:
            target_sum = eval(str(target_sum))
        except Exception:
            raise ValueError("The given target_sum must be a number. You gave : {0}, which is of type {1}".format(target_sum, type(target_sum)))
        
        # Set up the PAIRS list and get all the node data from the given lane
        PAIRS = list()
        NODE_DATA = self.LAYERS_DATA[lane][0]

        # Filter out everything that is not a number or that is (-math.inf) from the given lane
        FILTER_FUNCTION = lambda node_value : type(node_value) == int or type(node_value) == float and node_value != -math.inf

        NODE_DATA = list(filter(FILTER_FUNCTION, NODE_DATA))

        for permutation in itertools.permutations(NODE_DATA, 2):
            if sum(permutation) == target_sum and permutation not in PAIRS and permutation[::-1] not in PAIRS:
                PAIRS.append(tuple(permutation))
        
        # Return the pairs of numbers which summed are the target_sum on the given lane
        return PAIRS

    ##################### OTHERS #####################
