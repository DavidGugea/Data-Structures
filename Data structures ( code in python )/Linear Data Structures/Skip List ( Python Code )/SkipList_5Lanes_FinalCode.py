import random
import math

class Node(object):
    '''
    Every node in normal linked lists have one pointer, that being .next
    In SkipLists we have a specific structure where each node has 4 pointers ( .prev, .next, .up & .down )


    '''
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None
        self.down = None
        self.up = None

class SkipList(object):
    '''
    The skip list that we are going to build, has 5 lanes.
    Every lane has a HEAD & a LAST node.
    The HEAD nodes are created in the __init__ method. All the heads remain unchanged, they will always be -infintity ( -math.inf ). So, that when we want to append something in the skip list, everything that we will ever want to append will be bigger than the head, so we keep all ouf our HEAD nodes not empty, not None and we can randomly scale the node that we wont to append up on the 5 layers that we will create. 

    A skip list with 2 lanes would look something like this:
    
    NONE <- -math.inf ( HEAD 1 ) <-> Node(DATA:2) ( LAST 1 ) -> NONE 
             |    |                    |    |
            DOWN  UP                 DOWN  UP
    NONE <- -math.inf ( HEAD 0 ) <-> Node(DATA:2) <-> Node(DATA:3) ( LAST 0 ) -> NONE

    '''
    def __init__(self):

        '''
        ( ~ Description ( how the method looks ) -> return value [ done(x) / undone (empty) ] )
            
        ############### GENERAL METHODS ###############

        ~ Get length on layer / full length on all layers ( self.getLength(self, LAYER_LEVEL=[0...4], FULL_SL_LENGTH = True/False)              -> integer ( length )                   [x]
        ~ Create __len__(self) method | Returns the full length on all layers ( len(self) )                                                     -> integer (length)                     [x] 

        ~ Node at index ( self.atIndex(index, LAYER_HEIGHT) )                                                                                   -> 'Node' data type                     [x]
        ~ Get node data on layer ( self.getNodeData(LAYER_LEVEL [from 0 to 5])                                                                  -> node data (string/int/float, etc...) [x]
        
        ############### GENERAL METHODS ###############

        ############### INSERTION / DELETION ###############
        
        ~ Append ( self.append(data) )                                                                                                          -> None                                 []

        ~ Delete node ( self.deleteNode(node) )                                                                                                 -> None                                 []
        ~ Delete at index ( self.deleteAtIndex(index) )                                                                                         -> None                                 []
        ~ Delete node with data ( self.deleteNodeWithData(data) )                                                                               -> None                                 []

        ############### INSERTION / DELETION ###############

        ############### OTHERS ###############
        
        ~ Search -> iteration from top layer head down to bottom till node is found ( self.search_ITERATIVE(data, DIRECT_RETURN ) )             -> Node                                 [x]
        ~ Search -> direct search in self.LAYERS_DATA                               ( self.search_FAST_RETURN(data, DIRECT_RETURN ) )           -> Node                                 [x]
        ~ Display all the data from all the layers                                  ( self.display() )                                          -> None                                 []
    
        ~ Merge ( self.merge() )                                                                                                                -> None                                 []

        ~ Remove duplicates ( self.removeDuplicates(self, defaultRemove, removeByHeightOnLayerLevel ) )                                         -> None                                 []
        ~ Is Palindrome ( self.isPalindrome() )                                                                                                 -> True/False                           []
        ~ Sum with another skip list ( self.sumWith(SUM_SKIP_LIST) )                                                                            -> integer                              []

        ~ Pairs with sum on layer ( self.pairsWithSumOnLayer(LAYER_LEVEL[from 0 to 4], TARGET_SUM) )                                            -> [ (num, num), (num, num) ... ]       []

        ~ Split layer data in half ( self.splitLayerDataInHalf(LAYER_LEVEL[from 0 to 4]) )                                                      -> [LIST1, LIST2]                       []
        ~ Split layer after node ( self.splitLayerAfterNode(LAYER_LEVEL[from 0 to 4], NODE ) )                                                  -> [LIST1, LIST2]                       []
        ~ Split list at index ( self.splitLayerAtIndex(LAYER_LEVEL[from 0 to 4], INDEX ) )                                                      -> [LIST1, LIST2]                       []

        ############### OTHERS ###############
        '''

        # Create the HEAD & LAST nodes ( both have -math.inf data, the LAST nodes data might change, but the HEADS will never change )
        for LAYER_LEVEL in range(5):
            exec("self.head{0} = Node(-math.inf)\nself.last{0} = Node(-math.inf)".format(LAYER_LEVEL))
        
        # Create the .down & .up pointers for the HEAD & LAST NODES
        for LAYER_LEVEL in range(5):
            if LAYER_LEVEL == 0:
                self.head0.up = self.head1
                self.last0.up = self.last1
            elif LAYER_LEVEL == 4:
                self.head4.down = self.last3
                self.last4.down = self.last3
            else:
                ''' The string that we are trying to exec is:
                self.head(X).down = self.head(X-1) => example : self.head3.down = self.head2
                self.head(X).up = self.head(X+1)   => example : self.head3.up   = self.head4
                self.last(X).down = self.last(X-1) => example : self.last3.down = self.last2
                self.last(X).up = self.last(X+1)   => example : self.last3.up   = self.last4

                X => LAYER_LEVEL
                '''
                exec("self.head{0}.down = self.head{1}\nself.head{0}.up = self.head{2}\nself.last{0}.down = self.last{1}\nself.last{0}.up = self.last{2}".format(LAYER_LEVEL, LAYER_LEVEL-1,LAYER_LEVEL+1))

        '''
        -> We will create now a dictionary for the skip list. 
        Every key, besides the first layer, in the dictionary will look like this:
        = >  { LAYER LEVEL NUMBER : [ [DATA_0_ON_LAYER, DATA_1_ON_LAYER, ETC..], [NODE_0_ON_LAYER, NODE_1_ON_LAYER, ETC...], LAYER_LENGTH ] }
        = >  EXAMPLE : { 1 : [ [-math.inf, 1, 2], [<__main__.Node object at 0x..>, <__main__.Node object at 0x..>, <__main__.Node object at 0x..> ], 3 ] }

        The first layer will have a difference. Besides a list with node data and a list with the nodes, and the number of nodes on the layer, it will also have a list, with the height of the nodes.

        = > { 0 : [ [DATA_0_ON_LAYER, DATA_1_ON_LAYER, ETC...], [HEIGHT_OF_FIRST_NODE, HEIGHT_OF_SECOND_NODE], [NODE_0_ON_LAYER, NODE_1_ON_LAYER, ETC...], LAYER_LENGTH ] }
        = > EXAMPLE : { 0 : [ [-math.inf, 1], [5, 2], [<__main__.Node object at 0x..>, <__main__.Node object at 0x...>], 2 ] }
    
        We already know that every layer will start with the  -math.inf HEAD and will also remain the same. So by default we create that in our dict.
        '''
        self.LAYERS_DATA = {
            0 : [ [self.head0.data], [5], [self.head0], 1 ], # LAYER 0  
            1 : [ [self.head1.data], [self.head1], 1 ], # LAYER 1
            2 : [ [self.head2.data], [self.head2], 1 ], # LAYER 2
            3 : [ [self.head3.data], [self.head3], 1 ], # LAYER 3
            4 : [ [self.head4.data], [self.head4], 1 ]  # LAYER 4
        }

    ############### GENERAL METHODS ###############
    
    def getLength(self, LAYER_LEVEL=0, FULL_SL_LENGTH=False):
        '''
        There are 2 ways to use this method.
        Either you give the LAYER_LEVEL, something from 0 to 4 because we have 5 layers and set the FULL_SL_LENGTH to False, so that you get the number of nodes on a specifc LAYER 
        OR
        You write at the LAYER_LEVEL, None and set the FULL_SL_LENGTH to True, so you get the number of total nodes in the skip list.
        '''

        if FULL_SL_LENGTH and LAYER_LEVEL != None:
            raise ValueError("The FULL_SL_LENGTH indicates that you want the full length of the skip list. Hence you can't set it to True and then give a LAYER_LEVEL.")
        elif not FULL_SL_LENGTH and LAYER_LEVEL == None:
            raise ValueError("You must chose something between LAYER_LEVEL & FULL_SL_LENGTH. Read the docstring of the method for more information.")
        
        if FULL_SL_LENGTH:
            # Calculate the number of nodes in the entire skip list.
            FULL_LENGTH = 0
            for LAYER_LEVEL in self.LAYERS_DATA.keys():
                FULL_LENGTH += self.LAYERS_DATA[LAYER_LEVEL][-1]

            return FULL_LENGTH
        else:
            # Check the LAYER_LEVEL
            if not 0 <= LAYER_LEVEL <= 4: 
                raise ValueError("The layer level can be 0, 1, 2, 3 or 4. Not bigger, not smaller.")

            return self.LAYERS_DATA[LAYER_LEVEL][-1]

    def __len__(self):
        return self.getLength(None, True)

    def atIndex(self, index, LAYER_LEVEL):
        # Check the given layer level
        if not 0 <= LAYER_LEVEL <= 4:
            raise ValueError("The given LAYER_LEVEL is too big or too small. It must be 0, 1, 2, 3 or 4.")
        
        # Check the given index
        if not 0 <= index < self.LAYERS_DATA[LAYER_LEVEL][-1]:
            raise ValueError("The given index is too big for the given layer level.")
        else:
            if LAYER_LEVEL == 0:
                return self.LAYER_DATA[0][2][index]

            return self.LAYERS_DATA[LAYER_LEVEL][1][index]

    def getNodeData(self, LAYER_LEVEL):
        # Check the given layer level
        if not 0 <= LAYER_LEVEL <= 4:
            raise ValueError("The given layer level is either too big or too small. It must be 0, 1, 2, 3 or 4.")

        return self.LAYERS_DATA[LAYER_LEVEL][0]

    ############### GENERAL METHODS ###############

    ############### INSERTION / DELETION ###############

    def append(self, data, FAST_SEARCH = True):
        '''
        In order to append something to the list we must first find the closest node data to the node with the data that we want to append. In order for us to do that we must first search for the data and then get the node. FAST_SEARCH means that, when we will try to look for the node, we will use the self.FAST_RETURN method if FAST_SEARCH is True, otherwise, we will use the ITERATIVE method to search for something, that being the self.search_ITEARTIVE method

        FAST_SEARCH True    == > self.search_FAST_RETURN
        FAST_SEARCH False   == > self.search_ITERATIVE
        '''

        # Check if the head doesn't have a next node. If it doesn't have a next node then that means that the skip list is 'empty', it only has the -math.inf HEADS & LASTS without any binding between them ( no .prev & .next values set between them ). 
        if not self.head0.next:
            # 'Rebuild' the last node on layer0 and change it's .prev property to point to the head on layer0
            self.last0 = Node(data)

            self.last0.prev = self.head0
            self.head0.next = self.last0

            # Increment the number of nodes on layer 0 in the self.LAYERS_DATA
            self.LAYERS_DATA[0][-1] += 1

            # Append the new node data in on layer 0 in the self.LAYERS_DATA +++++ Append the new self.last0 node in the node list on layer 0 in self.LAYERS_DATA +++++ Set the height of the first node by default to be 1 on layer 0 in self.LAYERS_DATA
            self.LAYERS_DATA[0][0].append(data)
            self.LAYERS_DATA[0][-2].append(self.last0)
            self.LAYERS_DATA[0][1].append(1)

            # Move up with the node randomly.
            randomSkip = random.randint(1, 2) # As far as the randomSkip variable is not 2, we can move up with it on the 5 different layers
            LAYER_LEVEL = 1 # We will set the LAYER_LEVEL at 1, because in case we will move up with the node ( only as far as randomSkip is not 2 ), we are already on layer 0, so moving up will mean that we will start moving up on layer 1
            current = self.last0 # Keep track of the current last node
             
            while randomSkip != 2:
                '''
                The string that we will try to exec:

                self.last{LAYER_LEVEL} = Node(data)

                self.last{LAYER_LEVEL}.prev = self.head{LAYER_LEVEL}
                self.last{LAYER_LEVEL}.down = current
                self.head{LAYER_LEVEL}.next = self.last{LAYER_LEVEL}

                current.up = self.last{LAYER_LEVEL}
                '''
                exec("self.last{0} = Node(data)\nself.last{0}.prev = self.head{0}\nself.last{0}.down = current\nself.head{0}.next = self.last{0}\ncurrent.up = self.last{0}".format(LAYER_LEVEL))
               
                current = current.up

                # Update the list current node on LAYERS_DATA
                self.LAYERS_DATA[LAYER_LEVEL][-1] += 1 # Increase the length
                self.LAYERS_DATA[LAYER_LEVEL][0].append(data) # Append the new added data
                self.LAYERS_DATA[LAYER_LEVEL][-2].append(current) # Append the node
                
                # Increment the height of the node
                self.LAYERS_DATA[0][1][1] += 1
    
                LAYER_LEVEL += 1
                # See if the layer level has exceeded the limit of 5 layers, if that is the case then stop
                if LAYER_LEVEL == 5: break

                randomSkip = random.randint(1, 2)
        else:
            # Search for the closest node data that is still smaller than the data that we want to add on layer 0 ( looking for it on self.LAYERS_DATA )
            INDEX_TRACK = 0
            IS_LAST_NODE = False
            for LAYER_DATA in self.LAYERS_DATA[0][0]:
                if LAYER_DATA > data:
                    self.LAYERS_DATA[0][0].insert(INDEX_TRACK, data)
                    break

                INDEX_TRACK += 1

            if INDEX_TRACK == self.LAYERS_DATA[0][-1]:
                self.LAYERS_DATA[0][0].append(data)
                IS_LAST_NODE = True

            # Get the previous node, 'the closest node data that is still smaller than the data that we want to add on layer 0'
            PREV_TRACK = None
            PREV_DATA_SEARCH = self.LAYERS_DATA[0][0][INDEX_TRACK-1]

            # It doesn't matter if we will use search_FAST_RETURN or search_ITERATIVE, both arguments DIRECT_RETURN at both methods must be set to False because we need the node on the first layer, on layer0
            if FAST_SEARCH:
                PREV_TRACK = self.search_FAST_RETURN(PREV_DATA_SEARCH, False)
            else:
                PREV_TRACK = self.search_ITERATIVE(PREV_DATA_SEARCH, False) 

            # 'Rebuild' the PREV_TRACK and the next node after the PREV_TRACK properties, so we can fit the new APPEND_NODE in. Set the new properties for the APPEND_NODE too
            APPEND_NODE = Node(data)
            APPEND_NODE.next = PREV_TRACK.next
            APPEND_NODE.prev = PREV_TRACK

            if PREV_TRACK.next:
                PREV_TRACK.next.prev = APPEND_NODE

            PREV_TRACK.next = APPEND_NODE

            if IS_LAST_NODE:
                self.last0 = self.last0.next
            
            # Change the layer 0 on the self.LAYERS_DATA dictionary
            self.LAYERS_DATA[0][1].insert(INDEX_TRACK, 1)
            self.LAYERS_DATA[0][-2].insert(INDEX_TRACK, APPEND_NODE)
            self.LAYERS_DATA[0][-1] += 1

            # Move the node up on the layers
            randomSkip = random.randint(1, 2)

            current = PREV_TRACK.next

            LAYER_LEVEL = 1

            while randomSkip != 2:
                current_index = self.LAYERS_DATA[LAYER_LEVEL-1][-2].index(PREV_TRACK) + 1

                # Update the PREV_TRACK node to be the last closest node on the new layer
                while not PREV_TRACK.up:
                    PREV_TRACK = PREV_TRACK.prev

                PREV_TRACK = PREV_TRACK.up
                PREV_TRACK_INDEX = self.LAYERS_DATA[LAYER_LEVEL][-2].index(PREV_TRACK)

                CURRENT_HEAD_ON_LAYER = eval("self.head{0}".format(LAYER_LEVEL))
                
                APPEND_NODE = Node(data)
                APPEND_NODE.prev = PREV_TRACK
                APPEND_NODE.next = PREV_TRACK.next
                APPEND_NODE.down = current

                # current_index_track = self.LAYERS_DATA[LAYER_LEVEL][-2].index(current)
                current.up = APPEND_NODE
                
                # Check if the layer has a new last node ( if the head node has a .next node element or not )
                if not CURRENT_HEAD_ON_LAYER.next:
                    # Create the new last node
                    exec("self.last{0} = APPEND_NODE\nself.last{0}.prev = self.head{0}\nself.head{0}.next = self.last{0}".format(LAYER_LEVEL))
                else:
                    if not PREV_TRACK.next:
                        PREV_TRACK.next = APPEND_NODE
                        exec("self.last{0} = self.last{0}.next".format(LAYER_LEVEL))
                    else:
                        PREV_TRACK.next.prev = APPEND_NODE
                        PREV_TRACK.next = APPEND_NODE
                
                        self.LAYERS_DATA[LAYER_LEVEL][-2][PREV_TRACK_INDEX+1] = PREV_TRACK.next # Update the next node

                # Update the LAYERS_DATA for the new APPEND_NODE 
                self.LAYERS_DATA[LAYER_LEVEL][0].insert(PREV_TRACK_INDEX+1, data)           # ADD IT'S DATA TO THE DATA LIST
                self.LAYERS_DATA[LAYER_LEVEL][-2].insert(PREV_TRACK_INDEX+1, APPEND_NODE)   # ADD IT TO THE NODES LIST
                self.LAYERS_DATA[LAYER_LEVEL][-1] += 1                                      # INCREMENT THE NUMBER OF NODES ON THE LAYER
                self.LAYERS_DATA[0][1][INDEX_TRACK] += 1                                    # INCREMENT THE HEIGHT OF THE MAIN NODE ON LAYER 0
                
                self.LAYERS_DATA[LAYER_LEVEL-1][-2][current_index] = current                # Update the current node

                # Update the current node
                current = current.up

                # Check the layer level. If it has reached the maximum number of layers, of 5, then stop the loop
                LAYER_LEVEL += 1
                if LAYER_LEVEL == 5: break

                randomSkip = random.randint(1, 2)

    def deleteNode(self, node, FAST_SEARCH = True):
        '''
        In order to delete the given node, we must be sure that it is on layer 0,  so the first thing that we will do, after we check that the given ndoe is of type Node, is to 'dig down' to layer 0. After we do that, we must search the closest node on layer 0 that has the data smaller than the given node. 
        The argument 'FAST_SEARCH' works the same as at the self.append method. We will need to SEARCH for the given node. Hence we can use the self.search_ITERATIVE and self.search_FAST_RETURN.
        '''
        # Check the given node
        if not type(node) == Node:
            raise ValueError("The given node must be of node type.")
        
        # Dig down till we get to layer 0 with the node
        while node.down:
            node = node.down
    
        PREV_NODE_DATA = None
        DELETE_NODE_DATA = node.data

        INDEX_TRACK = 0
        
        for LAYER_DATA in self.LAYERS_DATA[0][0]:
            if LAYER_DATA > DELETE_NODE_DATA:
                PREV_NODE_DATA = self.LAYERS_DATA[0][0][INDEX_TRACK-2]
                del self.LAYERS_DATA[0][0][INDEX_TRACK-1]
                break

            INDEX_TRACK += 1

        if INDEX_TRACK == self.LAYERS_DATA[0][-1]:
            PREV_NODE_DATA = self.LAYERS_DATA[0][0][INDEX_TRACK-2]
            del self.LAYERS_DATA[0][0][-1]
        
        if FAST_SEARCH:
            PREV_TRACK = self.search_FAST_RETURN(PREV_NODE_DATA, False)
        else:
            PREV_TRACK = self.search_ITEARTIVE(PREV_NODE_DATA, False)

        # Decrement the length of the layer 0 in the self.LAYERS_DATA
        self.LAYERS_DATA[0][-1] -= 1
        
        # Delete the node data from the node data list in the self.LAYERS_DATA
        del self.LAYERS_DATA[0][-2][INDEX_TRACK-1] 

        # Delete the node height from the layer 0 in the self.LAYERS_DATA
        del self.LAYERS_DATA[0][1][INDEX_TRACK-1]

        print("PREV_TRACK -- > {0}".format(PREV_TRACK.data))
        print("node -- > {0}".format(node))

    ############### INSERTION / DELETION ###############

    ############### OTHERS ###############

    def search_ITERATIVE(self, data, DIRECT_RETURN):
        # Start at the top layer at the head. (HEAD4)
        current = self.head4
        START_CURRENT = current
        prev = None
        
        while current:
            if current.data == data:
                if DIRECT_RETURN: return current
                else:
                    # Dig down
                    while current.down:
                        current = current.down
                    
                    return current
            elif current.data < data and current.next:
                prev = current
                current = current.next
            elif current.data < data and not current.next:
                current = current.down
               
                # ~ Reset START_CURRENT & prev ~ #
                START_CURRENT = current
                prev = None
            elif current.data > data and prev:
                current = prev.down

                # ~ Reset START_CURRENT & prev ~ #
                START_CURRENT = current
                prev = None
            elif current.data > data and not prev:
                current = START_CURRENT.down

                # ~ Reset START_CURRENT & prev ~ #
                START_CURRENT = current
                prev = None
        
        # If we passed the while loop, that means that we didn't return the current data. Hence the data couldn't be found, therefore we must raise an error
        raise ValueError("The given data couldn't be found in the list.") 

    def search_FAST_RETURN(self, data, DIRECT_RETURN):
        # It is the same as self.search_ITERATIVE, with the difference that we will look in self.LAYERS_DATA and not iterate anymore
        if not DIRECT_RETURN:
            try:
                return self.LAYERS_DATA[0][2][self.LAYERS_DATA[0][0].index(data)]
            except Exception:
                raise ValueError("The given data couldn't be found in the skip list.")

    def display(self):
        LAYERS = [ list() for i in range(5) ]

        for LAYER_LEVEL in range(5):
            exec("current = self.head{0}\nwhile current:\n\tLAYERS[{0}].append(current.data)\n\tcurrent = current.next".format(LAYER_LEVEL))

        for LAYER_LEVEL in range(4, -1, -1):
            print("LAYER {0} -- > {1}".format(LAYER_LEVEL, LAYERS[LAYER_LEVEL]))

    ############### OTHERS ###############

SL = SkipList()

SL.append(5)
SL.append(1)

SL.deleteNode(SL.last0)

for i in range(5):
    print()

for LAYER_LEVEL in range(4, -1, -1):
    print("LAYER {0} -- > {1} // {2}".format(LAYER_LEVEL, eval("SL.head{0}.data".format(LAYER_LEVEL)), eval("SL.last{0}.data".format(LAYER_LEVEL))))

for i in range(5):
    print()

SL.display()

for i in range(3):
    print()

for LAYER_LEVEL in range(4, -1, -1):
    print("{0} -- > {1}".format(LAYER_LEVEL, SL.LAYERS_DATA[LAYER_LEVEL]))

for i in range(3):
    print()

print(SL.LAYERS_DATA)

for i in range(3):
    print()
