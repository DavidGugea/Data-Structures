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

for i in range(1, 21):
    SL.append(i)

# SL.deleteNode(SL.head0.next)

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

print("SL.LAYERS_DATA[2][-2][-1].data -- > {0}".format(SL.LAYERS_DATA[2][-2][-1].data))
print("SL.LAYERS_DATA[2][-2][-1].up.data -- > {0}".format(SL.LAYERS_DATA[2][-2][-1].up.data))
print("SL.LAYERS_DATA[2][-2][-1].prev.data -- > {0}".format(SL.LAYERS_DATA[0][-2][-1].prev.data))
print("SL.last2.data -- > {0}".format(SL.last2.data))
print("SL.last2.up.data -- > {0}".format(SL.last2.data))
print("SL.last2.prev.data -- > {0}".format(SL.last2.data))
