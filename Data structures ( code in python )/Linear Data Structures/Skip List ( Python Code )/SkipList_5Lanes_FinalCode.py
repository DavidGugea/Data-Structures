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
        When we want to append a new node to the skip list, we must know the closest node to it that has a data smaller than the 'data' argument that we want our APPEND_NODE to have.
        We will have to search for the node that has that data so this is what FAST_SEARCH means. If FAST_SEARCH is True, we will use self.search_FAST_RETURN, if it is False, we will use self.search_ITERATIVE
        '''

        # Check if the head node on layer 0 has a next node. If it doesn't then that indicates that the skip list is empty. It only has the -infinity (-math.inf) heads and 'lasts' nodes
        if not self.head0.next:
            self.last0 = Node(data) 

            self.last0.prev = self.head0
            self.head0.next = self.last0
            
            # Go up with the node
            randomUp = random.randint(1, 2)
            current = self.last0
            LAYER_LEVEL = 1 # We will set the LAYER_LEVEL to be 1 because we already occupied the first layer, we already added self.last0, so the next node that we will go up with will be on layer 1.

            # Append the node on LAYERS_DATA
            self.LAYERS_DATA[0][0].append(data)         # Append the data in the nodes data list on layer 0
            self.LAYERS_DATA[0][1].append(1)            # Append a new height for the new made last node
            self.LAYERS_DATA[0][-2].append(self.last0)  # Append the new created last node in the nodes list in LAYERS_DATA on layer 0
            self.LAYERS_DATA[0][-1] += 1                # Increment the number of nodes on layer 0 in LAYERS_DATA

            while randomUp != 2:
                '''
                The string that we will execute is:
                
                self.last{LAYER_LEVEL} = Node(data)

                self.last{LAYER_LEVEL}.prev = self.head{LAYER_LEVEL}
                self.last{LAYER_LEVEL}.down = current

                self.head{LAYER_LEVEL}.next = self.last{LAYER_LEVEL}
                
                current.up = self.last{LAYER_LEVEL}
                '''

                exec("self.last{0} = Node(data)\nself.last{0}.prev = self.head{0}\nself.last{0}.down = current\nself.head{0}.next = self.last{0}\ncurrent.up = self.last{0}".format(LAYER_LEVEL))

                # Update the LAYERS_DATA
                self.LAYERS_DATA[LAYER_LEVEL][0].append(data)                                           # Append the node data in the node data list on the current layer level.
                self.LAYERS_DATA[0][1][-1] += 1                                                         # Update the height on layer 0 of the last node
                self.LAYERS_DATA[LAYER_LEVEL][-2].append(eval("self.last{0}".format(LAYER_LEVEL)))      # Append the node in the node list on the current layer level.
                self.LAYERS_DATA[LAYER_LEVEL][-1] += 1                                                  # Increment the number of nodes on the current layer level.

                # Increase the layer level because we want to move up
                LAYER_LEVEL += 1
                if LAYER_LEVEL == 5: break # Break because it has reached the limit. We only have ( self.head0/self.last0 | self.head1/self.last1 | self.head2/self.last2 | self.head3/self.last3 | self.head4/self.last4 )

                # Update the current last node
                current = current.up

                randomUp = random.randint(1, 2)
        else:
            # Search for the closest node data in the node data list on layer 0 in the self.LAYERS_DATA that still has a data smaller than the given 'data' argument & append the new data
            APPEND_NODE_INDEX = 0
            PREV_NODE_DATA = str()
            IS_APPEND_NODE_LAST_NODE = False 
            
            for LAYER_DATA in self.LAYERS_DATA[0][0]:
                # Search for the first node data that is bigger than the given 'data' argument and append the data before it
                if LAYER_DATA > data:
                    PREV_NODE_DATA = self.LAYERS_DATA[0][0][APPEND_NODE_INDEX-1]
                    self.LAYERS_DATA[0][0].insert(APPEND_NODE_INDEX, data)
                    break
                
                APPEND_NODE_INDEX += 1

            # If there was no bigger node data than the given 'data' argument that means that the given 'data' argument is the biggest one, so we can just append it to the list
            if APPEND_NODE_INDEX == self.LAYERS_DATA[0][-1]:
                self.LAYERS_DATA[0][0].append(data)
                IS_APPEND_NODE_LAST_NODE = True

            # Get the previous node data
            PREV_NODE_INDEX = APPEND_NODE_INDEX - 1
            PREV_NODE_DATA = self.LAYERS_DATA[0][0][PREV_NODE_INDEX]
            
            # Get the previous node --- > Regardless if the FAST_SEARCH argument is True or False we will set the DIRECT_RETURN to False for both methods, self.search_FAST_RETURN and for self.search_ITERATIVE to False because we need the node on LAYER 0 so we want the methods to 'dig down' after we gave them the data of the previous node< ---
            if FAST_SEARCH:
                PREV_NODE = self.search_FAST_RETURN(PREV_NODE_DATA, False)
            else:
                PREV_NODE = self.search_ITERATIVE(PREV_NODE_DATA, False)

            #################################################################################################
            # ~~~~~~ APPEND_NODE_INDEX IS THE INDEX OF THE NODE THAT WE WANT TO APPEND               ~~~~~~ #
            # ~~~~~~ PREV_NODE_INDEX IS THE INDEX OF THE NODE BEFORE THE NODE THAT WE WANT TO APPEND ~~~~~~ #
            #################################################################################################
            
            # Create the append node
            APPEND_NODE = Node(data)
            APPEND_NODE.prev = PREV_NODE
            APPEND_NODE.next = PREV_NODE.next

            if PREV_NODE.next:
                PREV_NODE.next.prev = APPEND_NODE

            PREV_NODE.next = APPEND_NODE
        
            if IS_APPEND_NODE_LAST_NODE:
                self.last0 = self.last0.next

            # Update the layer 0 on self.LAYERS_DATA
            self.LAYERS_DATA[0][1].insert(APPEND_NODE_INDEX, 1)             # Add the height of the node, it defaults to none because we didn't go up with the node yet
            self.LAYERS_DATA[0][-2].insert(APPEND_NODE_INDEX, APPEND_NODE)  # Insert the node in the nodes list on layer 0 in self.LAYERS_DATA
            self.LAYERS_DATA[0][-1] += 1                                    # Increment the length of layer 0 

            # Go up with the node
            current = APPEND_NODE
            prev_track = PREV_NODE
            LAYER_LEVEL = 1

            randomUp = random.randint(1, 2)
            START_APPEND_NODE_INDEX = APPEND_NODE_INDEX # Store the current append node index into a START_APPEND_NODE_INDEX variable. We will use this variable to increment the height of the node on layer 0 in self.LAYERS_DATA

            while randomUp == 3:
                # Move up with the previous node so that we can append a new node on the next layer ( prev_track starts on layer 0 so we have to move it on layer 1 )
                while not prev_track.up:
                    prev_track = prev_track.prev
                    PREV_NODE_INDEX-= 1

                APPEND_NODE_INDEX = PREV_NODE_INDEX + 1
                prev_track = prev_track.up

                # Create the new append node & set its properties and the prev & prev.next node properties
                APPEND_NODE = Node(data)

                APPEND_NODE.prev = prev_track
                APPEND_NODE.next = prev_track.next
                APPEND_NODE.down = current

                current.up = APPEND_NODE
            
                # Update the self.LAYERS_DATA
                self.LAYERS_DATA[LAYER_LEVEL][-1] += 1 # Increment the length of the layer
                self.LAYERS_DATA[LAYER_LEVEL][-2].insert(APPEND_NODE_INDEX, APPEND_NODE) # Insert the append node in the node list on the current layer level
                self.LAYERS_DATA[LAYER_LEVEL][0].insert(APPEND_NODE_INDEX, data) # Insert the append node data in the node data list on the current layer level
                self.LAYERS_DATA[0][1][START_APPEND_NODE_INDEX] += 1 # Increment the height of the node on layer 0 in self.LAYERS_DATA

                # Check if the layer has a new last node, not the default one, so check if the head node on the layer has a .next property
                HEAD_ON_CURRENT_LAYER = eval("self.head{0}".format(LAYER_LEVEL))

                if not HEAD_ON_CURRENT_LAYER.next:
                    '''
                    Create the new last node on that layer
                    String to exec:

                    self.last{LAYER_LEVEL} = APPEND_NODE
                    self.last{LAYER_LEVEL}.down = self.head{LAYER_LEVEL}
                    self.head{LAYER_LEVEL}.next = self.last{LAYER_LEVEL}
                    '''

                    exec("self.last{0} = APPEND_NODE\nself.last{0}.down = self.head{0}\nself.head{0}.next = self.last{0}".format(LAYER_LEVEL))
                    print("NEW LAST NODE -- > {0} // self.last{1}.down.data -- > {2}".format(eval("self.last{0}".format(LAYER_LEVEL)), LAYER_LEVEL, eval("self.last{0}.down.data".format(LAYER_LEVEL))))
                else:
                    if not prev_track.next:
                        # NEW LAST NODE ( currently, prev_track is self.last{LAYER_LEVEL} and its .next property is None and we will change it to be APPEND_NODE and then update the last node on the current layer )
                        prev_track.next = APPEND_NODE

                        # UPDATE THE LAST NODE ON THE CURRENT LAYER 
                        exec("self.last{0} = self.last{0}.next".format(LAYER_LEVEL))

                        self.LAYERS_DATA[LAYER_LEVEL][-2][APPEND_NODE_INDEX-1] = prev_track 
                    else:
                        prev_track.next.prev = APPEND_NODE
                        prev_track.next = APPEND_NODE
               
                        self.LAYERS_DATA[LAYER_LEVEL][-2][APPEND_NODE_INDEX+1] = APPEND_NODE.next 

                # Update the current append node
                current = current.up
                
                # Increment the layer level and make sure that it doesn't go pass the limit
                LAYER_LEVEL += 1
                if LAYER_LEVEL == 5: break

                randomUp = random.randint(1, 2) 
                    
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

for i in range(2):
    print()

print("SL.LAYERS_DATA[2][-2][-1].data -- > {0}".format(SL.LAYERS_DATA[2][-2][-1].data))
print("SL.LAYERS_DATA[2][-2][-1].up.data -- > {0}".format(SL.LAYERS_DATA[2][-2][-1].up.data))
print("SL.LAYERS_DATA[2][-2][-1].prev.data -- > {0}".format(SL.LAYERS_DATA[0][-2][-1].prev.data))
print("SL.LAYERS_DATA[2][-2][-1].down.data -- > {0}".format(SL.LAYERS_DATA[2][-2][-1].down.data))

for i in range(2):
    print()

print("SL.last2.data -- > {0}".format(SL.last2.data))
print("SL.last2.up.data -- > {0}".format(SL.last2.up.data))
print("SL.last2.prev.data -- > {0}".format(SL.last2.prev.data))
print("SL.last2.down.data -- > {0}".format(SL.last2.down.data))

for i in range(2):
    print()

'''
print("SL.LAYERS_DATA[2][-2][3].prev.data   -- > {0}".format(SL.LAYERS_DATA[2][-2][3].prev.data))
print("SL.head2.next.next.prev.data         -- > {0}".format(SL.head2.next.next.prev.data))
'''
