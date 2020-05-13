import itertools

class Node(object):
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None
        self.up = None
        self.down = None

class SkipList(object):
    '''
    * NOTE * : In this particular kind of skip list you must append object in sorted order manually.
    Example:
    You can write: skipList.append(1)\nskipList.append(2) but you can't write skipList.append(2)\nskipList.append(1).
    That is because we won't be able to search through the nodes if they are not in a sorted order.
    
    When we append a node in the skip list, if it goes on the express lane and after that we will try to append some other node to it
    that doesn't go on the exress lane and let's say, it's in the middle of the skip list, then we would
    have to change the data of all the express lane nodes and the data of all the normal lane nodes after it, which would cost a lot of time for big inputs. The same happens for deletion.

    ***** DIFFERENCES BETWEEN THE *IMPROVED* and the *DEFAULT* Skip List with normal & express lanes *****
    PROS : -> You can get the last node instantly because the class always keeps track of it, so it's O(1) in Time Complexity, you get it instantly, you don't have to transverse the entire skip list to get to the last node, because that would be O(n) in Time Complexity
           -> You can get immidiate access to the data from the first lane ( the normal lane ) and from the second lane ( the express lane ) which is O(1) in Time Complexity, rather than having to transverse the entire skip list, because that would be, again O(n) in Time Complexity
           -> You can get immdiate access to how many nodes are on the first lane ( the normal lane ) and how many there are on the second lane ( the express lane ) which is O(1) in Time Complexity, rather than having to transverse the entire skip list, counting each node, because that would be, again O(n) in Time Complexity
            
    CONS : -> By storing the nodes in lists and variables, we need more space. So the space complexity is bigger.

    ***** DIFFERENCES BETWEEN THE *IMPROVED* and the *DEFAULT* Skip List with normal & express lanes *****
    '''

    '''
    ( ~ Description ( how the method looks ) -> return value [ done(x) / undone(empty) ] )

    ###################### GENERAL METHODS ######################
    
    ~ Get length ( self.getLength(LANE) )                                                                           -> integer                          [x]
    ~ Create __len__(self) __method__   ( len(self) )                                                               -> integer                          [x] 

    ~ Node *data* at index ( self.atIndex(index, lane) )                                                            -> node data                        [x]
    ~ Get node data list ( self.getNodeData() )                                                                     -> [ list(), list() ]               [x]
    
    ~ Get last node ( self.getLastNode(self, lane) )                                                                -> 'Node' object                    [x] 

    ###################### GENERAL METHODS ######################
    ###################### INSERTION / SEARCH ######################

    ~ Append ( self.append(data) )                                                                                  -> None                             [x]
    ~ Search ( self.search(data, DIRECT_RETURN = True) )                                                            -> 'Node' object                    [x]

    ###################### INSERTION / SEARCH ######################
    ###################### OTHERS ######################

    ~ Merge with skip list ( self.merge(MERGE_SKIP_LIST) )                                                          -> None                             [x]
    ~ Is Palindrome ( self.isPalindrome() )                                                                         -> True/False                       [x]
    ~ Sum with skip list ( self.sumWith(SUM_SKIP_LIST, LANE_1, LANE_2) )                                            -> integer                          [x]

    ~ Split list in half ( self.splitInHalf(LANE) )                                                                 -> [ list(), list() ]               [x]
    ~ Split list after node ( self.splitListAfterNode(splitNode, LANE) )                                            -> [ list(), list() ]               [x]
    ~ Split list at index ( self.splitListAtIndex(splitIndex, LANE) )                                               -> [ list(), list() ]               [x]

    ~ Pairs with sum ( self.pairsWithSum(target_sum, LANE) )                                                        -> [ tuple(), tuple(), .. tuple() ] [x]

    ###################### OTHERS ######################
    '''

    def __init__(self, EXPRESS_STEP, CHECK_FOR_APPEND=True):
        # We will use the 'EXPRESS_STEP' to find out when there is time for a new node to be added on the express lane
        self.EXPRESS_STEP = EXPRESS_STEP
        
        '''
        When CHECK_FOR_APPNEND is True, in case you try to append a number that is not bigger than the last element, you will get a value error, if it's False
        then you won't get a value error but it still won't be appended anyways. ( read class docstring )
        '''
        self.CHECK_FOR_APPEND = CHECK_FOR_APPEND

        
        self.normalLane_HeadNode = None
        self.normalLane_LastNode = None
        self.normalLane_NODE_DATA = list() # Store all the node data from the normal lane 
        self.normalLane_NODE_COUNTER = 0 # Keep track of how many nodes are on the normal lane 

        self.expressLane_HeadNode = None
        self.expressLane_LastNode = None
        self.expressLane_NODE_DATA = list() # Store all the node data from the express
        self.expressLane_NODE_COUNTER = 0 # Keep track of how many nodes are on the express lane
 
    ###################### GENERAL METHODS ######################

    def getLength(self, LANE):
        ''' Return the number of nodes on the given LANE. The "LANE" argument must be either 'normal' or 'express' '''
        if LANE == "normal":
            return self.normalLane_NODE_COUNTER
        elif LANE == "express":
            return self.expressLane_NODE_COUNTER
        else:
            raise ValueError("The given 'LANE' argument must be either 'normal' or 'express'. The given LANE argument was : {0}".format(LANE))
    
    def __len__(self):
        ''' Return the sum between the number of nodes between both lanes '''
        return self.normalLane_NODE_COUNTER + self.expressLane_NODE_COUNTER

    def atIndex(self, index, lane):
        ''' Return the node data on the given lane at the given index '''
        if lane == "normal" and 0 <= index < len(self.normalLane_NODE_DATA):
            return self.normalLane_NODE_DATA[index]
        elif lane == "express" and 0 <= index < len(self.expressLane_NODE_DATA):
            return self.expressLane_NODE_DATA[index]
        else:
            raise ValueError("The index must be between 0 (inclusive) and the length of the given lane and the \"lane\" argument must be either 'normal' or 'express'. The given index was : {0} | The given lane was : {1}".format(index, lane))

    def getNodeData(self):
        ''' Return a list that contains all the node data from both lanes. The first list contains the node data from the first lane ( the normal lane ) . The second list contains the node data from the second lane ( the express lane ) '''
        return [ self.normalLane_NODE_DATA, self.expressLane_NODE_DATA ]

    def getLastNode(self, lane):
        ''' Return the last node on the given lane '''
        if lane == "normal":
            return self.normalLane_LastNode
        elif lane == "express":
            return self.expressLane_LastNode
        else:
            raise ValueError("The given lane must be either 'normal' or 'express'")
    

    ###################### GENERAL METHODS ######################
    ###################### INSERTION / SEARCH ######################

    def append(self, data):
        # Increment the number of nodes on the normal lane
        self.normalLane_NODE_COUNTER += 1

        # Append the data in the node data list on the normal lane
        self.normalLane_NODE_DATA.append(data)

        # Check if the skip list is empty or not
        if not self.normalLane_HeadNode and not self.expressLane_HeadNode:
            self.normalLane_HeadNode = Node(data)
            self.normalLane_LastNode = Node(data)
           
            self.normalLane_HeadNode.up = self.normalLane_LastNode
            self.normalLane_LastNode.down = self.normalLane_HeadNode
            
            self.expressLane_HeadNode = Node(data)
            self.expressLane_LastNode = Node(data)

            self.expressLane_HeadNode.up = self.expressLane_LastNode
            self.expressLane_LastNode.down = self.expressLane_HeadNode

            # Increment the number of nodes on the express lane
            self.expressLane_NODE_COUNTER += 1

            self.expressLane_NODE_DATA.append(data)
        else:
            # Check if the data is bigger than the last node or not. If it is not bigger return or raise ValueError
            if data < self.normalLane_LastNode.data:
                if self.CHECK_FOR_APPEND:
                    raise ValueError("The given data was smaller than the last node. Last node data : {0} | Given data : {1}".format(self.normalLane_LastNode.data, data))
                else:
                    return

            APPEND_NODE = Node(data)

            # Check if there is a last node and that the last node is not the same as the head node so, the head node has a .next node and head.next is not None
            if not self.normalLane_HeadNode.next:
                self.normalLane_LastNode = APPEND_NODE 

                self.normalLane_LastNode.prev = self.normalLane_HeadNode
                self.normalLane_HeadNode.next = self.normalLane_LastNode
            else:
                self.normalLane_LastNode.next = APPEND_NODE
                APPEND_NODE.prev = self.normalLane_LastNode
                
                self.normalLane_LastNode = self.normalLane_LastNode.next

            # Check if the node has to go up
            if self.normalLane_NODE_DATA.index(self.expressLane_LastNode.data) + self.EXPRESS_STEP + 2 == self.normalLane_NODE_COUNTER:
                EXPRESS_NODE = Node(data)

                EXPRESS_NODE.down = APPEND_NODE
                APPEND_NODE.up = EXPRESS_NODE
                
                # Check if the express lane head node is empty and if there is a last node, and that the last node is not the same as the head node, as it is by default, so check if the hhead node on the express lane has a .next property
                if not self.expressLane_HeadNode.next:
                    self.expressLane_LastNode = EXPRESS_NODE

                    self.expressLane_LastNode.prev = self.expressLane_HeadNode
                    self.expressLane_HeadNode.next = self.expressLane_LastNode
                else:
                    EXPRESS_NODE.prev = self.expressLane_LastNode
                    self.expressLane_LastNode.next = EXPRESS_NODE

                    self.expressLane_LastNode = self.expressLane_LastNode.next 

                # Increment the number of nodes on the express lane
                self.expressLane_NODE_COUNTER += 1

                # Append the data in the node data list on the express lane
                self.expressLane_NODE_DATA.append(data)

    def search(self, data, DIRECT_RETURN = True):
        ''' Search the node with the given data. For more information about the DIRECT_RETURN argument, read the secondary docstring of the method. '''
        '''
        The DIRECT_RETURN indicates that, if we find the node with the data that you are looking for on the express node, we are going to return the node on the express node if DIRECT_RETURN is True, otherwise we can return the node on the normal lane.

        Example:

        EXPRESS LANE -- > None <-> 1(EXPRESS) <-> 4(EXPRESS) <-> 7(EXPRESS)
        NORMAL LANE  -- > None <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7

        skipList.search(4, DIRECT_RETURN = True) will return 4(EXPRESS)
        skipList.search(4, DIRECT_RETURN = False) will return 4 on the normal lane

        But if the node data that you are searching for couldn't be found on the express lane it will be returned on the normal lane, if found on the normal lane. If it wouldn't be found on the normal lane, the method will raise a value error.

        skipList.search(2, .. ) will return 2 on the normal lane
        skipList.search(1234, .. ) regardless what DIRECT_RETURN is, the method will raise a value error
        '''
        
        prev = None
        current = self.expressLane_HeadNode
        current_N = None # The current node on the normal lane ( will be found in the while loop )

        thereIsABorder = True

        # Find the last closest node on the express lane that is still smaller than the data we are searching for
        while current:
            if current.data == data:
                if DIRECT_RETURN: return current
                else: return current.down
            elif current.data < data and current.next:
                prev = current
                current = current.next
            elif current.data < data and not current.next:
                current_N = current.down
                thereIsABorder = False
                break
            elif current.data > data:
                current_N = prev.down
                break
        
        while current_N:
            if current_N.data == data:
                return current_N
            elif ( current_N.data < data ) or ( current_N.data > data and not thereIsABorder ):
                current_N = current_N.next
            elif current_N.data  > data and thereIsABorder:
                raise ValueError("The given data couldn't be found in the list.")
        
    ###################### INSERTION / SEARCH ######################
    ###################### OTHERS ######################

    def merge(self, MERGE_SKIP_LIST):
        ''' Merge the data of the main skip list ( self ) with the data of the MERGE_SKIP_LIST'''
        for nodeData in MERGE_SKIP_LIST.normalLane_NODE_DATA:
            self.append(nodeData)

    def isPalindrome(self):
        ''' Return the boolean value of the node data string being equal to it upside down ( [::-1] )'''
        nodeDataString = "".join(map(str, self.normalLane_NODE_DATA))
        return nodeDataString == nodeDataString[::-1]
    
    def sumWith(self, SUM_SKIP_LIST, LANE_1, LANE_2):
        ''' Return the sum between all the nodes between the main skip list and the SUM_SKIP_LIST on the given lanes. A lane argument can be either 'normal', 'express' or None. None indicates that we must add the node data on both lanes, on the normal and on the express one. '''
        # Check the lanes & the SUM_SKIP_LIST argument
        if not type(SUM_SKIP_LIST) == SkipList:
            raise ValueError("The given SUM_SKIP_LIST argument must be of type SkipList. It's type is : {0}".format(type(SUM_SKIP_LIST)))

        ALLOWED_LANE_ARGUMENT_VALUES = ['normal', 'express', None]
        if not LANE_1 in ALLOWED_LANE_ARGUMENT_VALUES and not LANE_2 in ALLOWED_LANE_ARGUMENT_VALUES:
            raise ValueError("The given lane argument must be either 'normal', 'express' or None. The given values are : LANE_1 -> {0} | LANE_2 -> {1}".format(LANE_1, LANE_2)) 

        LANE_1_SEARCH_SUM = 0
        LANE_2_SEARCH_SUM = 0

        FILTER_FUNCTION = lambda nodeData : type(nodeData) == int or type(nodeData) == float
        
        SUM_FIRST = 0  # The sum that the user wants for the first skip list ( self )
        SUM_SECOND = 0 # The sum that the user wants for the second skip list ( SUM_SKIP_LIST )

        if LANE_1 == "normal": SUM_FIRST = sum(list(filter(FILTER_FUNCTION, self.normalLane_NODE_DATA)))
        elif LANE_1 == "express": SUM_FIRST = sum(list(filter(FILTER_FUNCTION, self.expressLane_NODE_DATA)))
        elif LANE_1 == None: SUM_FIRST = sum(list(filter(FILTER_FUNCTION, self.normalLane_NODE_DATA))) + sum(list(filter(FILTER_FUNCTION, self.expressLane_NODE_DATA)))

        if LANE_2 == "normal" : SUM_SECOND = sum(list(filter(FILTER_FUNCTION, SUM_SKIP_LIST.normalLane_NODE_DATA)))
        elif LANE_2 == "express" : SUM_SECOND = sum(list(filter(FILTER_FUNCTION, SUM_SKIP_LIST.expressLane_NODE_DATA)))
        elif LANE_2 == None: SUM_SECOND = sum(list(filter(FILTER_FUNCTION, SUM_SKIP_LIST.normalLane_NODE_DATA))) + sum(list(filter(FILTER_FUNCTION, self.expressLane_NODE_DATA))) 

        return SUM_FIRST + SUM_SECOND

    def splitInHalf(self, LANE):
        ''' Return a list with the split data at the given lanes. The 'LANE' argument must be 'normal' or 'express' '''
        if LANE == "normal": return [ self.normalLane_NODE_DATA[:len(self.normalLane_NODE_DATA) // 2], self.normalLane_NODE_DATA[len(self.normalLane_NODE_DATA) // 2:] ]
        elif LANE == "express": return [ self.expressLane_NODE_DATA[:len(self.expressLane_NODE_DATA) // 2], self.expressLane_NODE_DATA[len(self.expressLane_NODE_DATA) // 2:] ]
        else:
            raise ValueError("The given LANE argument must be either 'normal' or 'express'. The given one was : {0}".format(LANE))

    def splitListAfterNode(self, splitNode, LANE):
        ''' Return a list with the split data after the given node. The 'LANE' argument must be 'normal' or 'express' '''
        list_1 = list() # In this list we will store all the node data before the given node
        list_2 = list() # In this list we will store all the node data after the given node
        
        if LANE == "normal":
            current = self.normalLane_HeadNode
        elif LANE == "express":
            current = self.expressLane_HeadNode
        else:
            raise ValueError("The given 'LANE' argument must be either 'normal' or 'express'. The given ones was : {0}".format(LANE))
    
        passedAfterSplitNode = False
        while current:
            if not passedAfterSplitNode:
                list_1.append(current.data)
            else:
                list_2.append(current.data)
                
            if current == splitNode:
                passedAfterSplitNode = True
        
            current = current.next
        
        return [ list_1, list_2 ]

    def splitListAtIndex(self, splitIndex, LANE):
        if LANE == "normal" and splitIndex < len(self.normalLane_NODE_DATA) :
            return [ self.normalLane_NODE_DATA[:splitIndex], self.normalLane_NODE_DATA[splitIndex:] ]
        elif LANE == "express" and splitIndex < len(self.expressLane_NODE_DATA):
            return [ self.expressLane_NODE_DATA[:splitIndex], self.expressLane_NODE_DATA[splitIndex:] ]
        else:
            raise ValueError("The given LANE argument must be 'normal' or 'express' and the index must be valid for the given lane.")

    def pairsWithSum(self, target_sum, LANE):
        PAIRS = list()
    
        if LANE == "normal":
            LANE_TARGET = self.normalLane_NODE_DATA
        elif LANE == "express":
            LANE_TARGET = self.expressLane_NODE_DATA

        for permutation in itertools.permutations(LANE_TARGET, 2):
            if sum(permutation) == target_sum and permutation not in PAIRS and permutation[::-1] not in PAIRS:
                PAIRS.append(permutation)
    
        return PAIRS

    ###################### OTHERS ######################
