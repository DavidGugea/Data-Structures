import itertools

class Node(object):
    def __init__(self, data):
        self.data = data

        self.next = None
        self.prev = None
        self.up = None
        self.down = None

class SkipList(object):
    def __init__(self, EXPRESS_SKIP):
        '''

        ( ~ Description ( how the method looks ) -> return value [ done(x) / undone(empty) ] )

        ###################### GENERAL METHODS ######################
        
        ~ Get length ( self.getLength(LANE) )                                                                           -> integer                          [x]
        ~ Create __len__(self) __method__   ( len(self) )                                                               -> integer                          [x] 

        ~ Node *data* at index ( self.atIndex(index, lane) )                                                            -> node data                        [x]
        ~ Get node data list ( self.getNodeData() )                                                                     -> [ list(), list() ]               [x]
        
        ~ Get last node ( self.getLastNode(self, lane) )                                                                -> 'Node' object                    [x] 

        ###################### GENERAL METHODS ######################
        ###################### INSERTION / DELETION / SEARCH ######################

        ~ Append ( self.append(data) )                                                                                  -> None                             [x]
        ~ Delete last node ( self.deleteLast() )                                                                        -> None                             [x]
        ~ Search ( self.search(data, DIRECT_RETURN = True) )                                                            -> 'Node' object                    [x]

        ###################### INSERTION / DELETION / SEARCH ######################
        ###################### OTHERS ######################

        ~ Merge with skip list ( self.merge(MERGE_SKIP_LIST) )                                                          -> None                             [x]
        ~ Sum with skip list ( self.sumWith(SUM_SKIP_LIST, LANE_1, LANE_2) )                                            -> integer                          [x]

        ~ Split list in half ( self.splitInHalf(LANE) )                                                                 -> [ list(), list() ]               [x]
        ~ Split list after node ( self.splitListAfterNode(splitNode, LANE) )                                            -> [ list(), list() ]               [x]
        ~ Split list at index ( self.splitListAtIndex(splitIndex, LANE) )                                               -> [ list(), list() ]               [x]

        ~ Pairs with sum ( self.pairsWithSum(target_sum, LANE) )                                                        -> [ tuple(), tuple(), .. tuple() ] [x]

        ###################### OTHERS ######################

        '''

        self.normalLane_HeadNode = None
        self.expressLane_HeadNode = None

        self.normalLane_Counter = 0
        self.expressLane_Counter = 0

        self.EXPRESS_SKIP = EXPRESS_SKIP

    ###################### GENERAL METHODS ######################

    def getLength(self, LANE):
        ''' Returns the number of nodes on the given LANE argument. The 'LANE' argument can be either 'normal' or 'express' ''' 
        if LANE == "normal" : return self.normalLane_Counter 
        elif LANE == "express" : return self.expressLane_Counter 
        else:
            raise ValueError("The given 'LANE' argument must be either 'normal' or 'express'")

    def __len__(self):
        ''' Returns the number of nodes on both lanes '''
        return self.normalLane_Counter + self.expressLane_Counter
            
    def atIndex(self, index, lane):
        ''' Return the node on the given lane at the given index '''
        current = None  # Keep track of the current node. Find out if the current node should start transversing the skip list on the normal or on the express lane
        index_Track = 0 # Keep track of the index while moving forward with the current node 

        # Check the lane & index argument and set up the current node
        if lane == "normal":
            if not 0 <= index < self.normalLane_Counter: 
                raise ValueError("The given index is either too big or too small for the given lane. INDEX : {0} | NUMBER OF NODES ON THE LANE : {1}".format(index, lane))
            
            current = self.normalLane_HeadNode
        elif lane == "express":
            if not 0 <= index < self.expressLane_Counter:
                raise ValueError("The given index is either too big or too small for the given lane. INDEX : {0} | NUMBER OF NODES ON THE LANE : {1}".format(index, lane))

            current = self.expressLane_HeadNode
        else:
            raise ValueError("The given 'lane' argument must be either 'normal' or 'express'")

        # Go through the list till we get to the given index
        while index_Track < index:
            current = current.next
            index_Track += 1

        # Return the node at the given index on the given lane
        return current
    
    def getNodeData(self):
        ''' Returns a list that contains two others lists. The first list contains all the elements on the first lane ( the normal lane ) and the second list contains all the elements on teh second lane ( the express lane ) '''

        NORMAL_LANE_NODE_DATA = list()
        EXPRESS_LANE_NODE_DATA = list()

        current = self.normalLane_HeadNode
        while current:
            NORMAL_LANE_NODE_DATA.append(current.data)
            current = current.next

        current = self.expressLane_HeadNode
        while current:
            EXPRESS_LANE_NODE_DATA.append(current.data)
            current = current.next

        return [ NORMAL_LANE_NODE_DATA, EXPRESS_LANE_NODE_DATA ]

    def getLastNode(self, lane):
        ''' Returns the last node on the given lane. The 'lane' argument must be either 'normal' or 'express' '''
        current = None

        # Check if the skip list is empty
        if not self.normalLane_HeadNode and not self.expressLane_HeadNode:
            return None

        # Check the lane argument and set up the current node 
        if lane == 'normal':
            current = self.normalLane_HeadNode
        elif lane == 'express':
            current = self.expressLane_HeadNode
        else:
            raise ValueError("The given 'lane' argument must be either 'normal' or 'express'")

        while current.next:
            current = current.next

        return current

    ###################### GENERAL METHODS ######################
    ###################### INSERTION / SEARCH ######################
    
    def append(self, data):
        ''' Append the node with the given data '''
        
        '''
        *NOTE* : In order to use the 'search' method properly you won't be allowed to add data that is smaller than the last node. That means that you must manually add sorted items. 
        Example:

        You can't write something like this:
        SL = SkipList()
        
        SL.append(5)
        SL.append(1)

        Because 1 is smaller than 5, so we won't be able to search nodes fast through the skip list.
        '''
        # Check if the skip list is empty or not 
        if not self.normalLane_HeadNode and not self.expressLane_HeadNode:
            # Create normal & express head nodes
            self.normalLane_HeadNode = Node(data)
            self.expressLane_HeadNode = Node(data)
            
            # Set up the pointers between them
            self.normalLane_HeadNode.up = self.expressLane_HeadNode
            self.expressLane_HeadNode.down = self.normalLane_HeadNode

            # Increment the counters for both lanes
            self.normalLane_Counter += 1
            self.expressLane_Counter += 1
        else:
            # Get the last node on the normal lane & check the given data 
            normalLane_LAST_NODE = self.getLastNode("normal")

            if data < normalLane_LAST_NODE.data:
                raise ValueError("The given data has a smaller value than the last node on the normal lane. DATA : {0} | LAST NODE ON THE NORMAL LANE : {1}".format(data, normalLane_LAST_NODE.data))

            # Append the node first on the normal lane 
            APPEND_NODE = Node(data)

            APPEND_NODE.prev = normalLane_LAST_NODE
            normalLane_LAST_NODE.next = APPEND_NODE

            # Increment the counter for the normal lane
            self.normalLane_Counter += 1

            # Find out if we have to go up with the node, on the express node or not.
            if self.getNodeData()[0].index(self.getLastNode("express").data) + self.EXPRESS_SKIP + 2 == self.normalLane_Counter:
                EXPRESS_NODE = Node(data)
                EXPRESS_LANE_LAST_NODE = self.getLastNode("express")

                EXPRESS_NODE.down = APPEND_NODE
                EXPRESS_NODE.prev = EXPRESS_LANE_LAST_NODE
                EXPRESS_LANE_LAST_NODE.next = EXPRESS_NODE

                APPEND_NODE.up = EXPRESS_NODE

                # Increment the counter for the express lane
                self.expressLane_Counter += 1

    def deleteLast(self):
        ''' Delete the last node '''
        EXPRESS_LANE_LAST = self.getLastNode('express')
        NORMAL_LANE_LAST  = self.getLastNode('normal')
        
        if NORMAL_LANE_LAST.up:
            EXPRESS_LANE_LAST.prev.next = None
            self.expressLane_Counter -= 1

        NORMAL_LANE_LAST.prev.next = None
        self.normalLane_Counter -= 1

    def search(self, data, DIRECT_RETURN = True):
        ''' Return a node with the given data if found. '''
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
        current_N = None # Find out where to start with the current_N node on the normal lane
    
        thereIsABorder = False

        while current:
            if current.data == data:
                if DIRECT_RETURN: return current
                else: return current.down
            elif current.data < data and current.next:
                prev = current
                current = current.next
            elif current.data < data and not current.next:
                current_N = current.down
                break
            elif current.data > data:
                current_N = prev.down
                thereIsABorder = True
                break

        while current_N:
            if current_N.data == data: 
                return current_N
            elif current_N.data > current.data and thereIsABorder:
                raise ValueError("The given node couldn't be found in the skip list")

            current_N = current_N.next 

        raise ValueError("The given node couldn't be found in the skip list")

    ###################### INSERTION / SEARCH ######################
    ###################### OTHERS ######################

    def merge(self, MERGE_SKIP_LIST):
        ''' Append every node data from the MERGE_SKIP_LIST to the main skip list ( self )'''
        for layerData in MERGE_SKIP_LIST.getNodeData()[0]:
            self.append(layerData)

    def sumWith(self, SUM_SKIP_LIST, LANE_1, LANE_2):
        ''' Return the sum between the main list and the SUM_SKIP_LIST on the given lanes '''
        
        # Check the given SUM_SKIP_LIST ( it must be of type SkipList )
        if type(SUM_SKIP_LIST) != SkipList:
            raise ValueError("The given SUM_SKIP_LIST argument must be of type 'SkipList'. Its type is : {0}".format(type(SUM_SKIP_LIST)))
         
        '''
        Check the given lanes. LANE_1 represents the lane for the first skip list, the main skip list ( self ). LANE_2 represents the lane for the second skip list, the SUM_SKIP_LIST. A lane can be "normal", "express" or None. If a lane is None that means that we will calculate the sum of all the nodes for both lanes, normal & express on one of the skip lists.

        Example:

        If LANE_1 is None the SUM_1, which will represent the sum between the nodes that need to be added for the main skip list ( self ), will be the sum of nodes on the first lane ( the normal lane ) + the sum of nodes on the second lane ( the express lane ). If it would only be for example 'normal', we would have to only add the number of nodes on the first lane
        '''

        ALLOWED_LANE_VALUES = ['normal', 'express', None]
        if ( not LANE_1 in ALLOWED_LANE_VALUES ) or ( not LANE_2 in ALLOWED_LANE_VALUES ):
            raise ValueError("The lane arguments must be 'normal', 'express' or None. For more information about it, read the docstring of the method. Given : LANE_1 : {0} | LANE_2 : {1}".format(LANE_1, LANE_2))

        SUM_1 = 0 # Represents the sum of the nodes that need to be added in the first skip list, the main skip list ( self )
        SUM_2 = 0 # Represents the sum of the nodes that need to be added in the second skip list, SUM_SKIP_LIST

        FILTER_FUNCTION = lambda node_data : type(node_data) == float or type(node_data) == int

        if LANE_1 == "normal":
            SUM_1 = sum(list(filter(FILTER_FUNCTION, self.getNodeData()[0])))
        elif LANE_1 == "express":
            SUM_1 = sum(list(filter(FILTER_FUNCTION, self.getNodeData()[1])))
        elif LANE_1 == None:
            SUM_1 = sum(list(filter(FILTER_FUNCTION, self.getNodeData()[0]))) + sum(list(filter(FILTER_FUNCTION, self.getNodeData()[1])))

        if LANE_2 == "normal":
            SUM_2 = sum(list(filter(FILTER_FUNCTION, SUM_SKIP_LIST.getNodeData()[0])))
        elif LANE_2 == "express":
            SUM_2 = sum(list(filter(FILTER_FUNCTION, SUM_SKIP_LIST.getNodeData()[1])))
        elif LANE_2 == None:
            SUM_2 = sum(list(filter(FILTER_FUNCTION, SUM_SKIP_LIST.getNodeData()[0]))) + sum(list(filter(FILTER_FUNCTION, SUM_SKIP_LIST.getNodeData()[1])))

        return SUM_1 + SUM_2

    def splitInHalf(self, LANE):
        ''' Return a list with two lists that contain the node data split on the given lane '''
        if LANE == "normal":
            return [ self.getNodeData()[0][:(self.normalLane_Counter // 2)], self.getNodeData()[0][(self.normalLane_Counter // 2):] ]
        elif LANE == "express":
            return [ self.getNodeData()[1][:(self.expressLane_Counter // 2)], self.getNodeData()[1][(self.expressLane_Counter // 2):] ]
        else:
            raise ValueError("The given LANE argument must be either 'normal' or 'express'. Given LANE argument was : {0}".format(LANE))

    def splitListAfterNode(self, splitNode, LANE):
        ''' Return a list with two lists that contain the node data split after the given splitNode argument '''
        
        # Check the splitNode & the LANE argument while establishing on what lane we have to start the iteration, so where to place the 'current' node value
        if not type(splitNode) == Node:
            raise ValueError("The given 'splitNode' value must be of type node. The given 'splitNode' values has a type of : {0}".format(type(splitNode)))
        
        current = None
        LIST_1 = list() # We will store all the node data in this list before we go pass the given 'splitNode' 
        LIST_2 = list() # We will store all the node data in this list after we went pass the given 'splitNode'
       
        afterSplitNode = False

        if LANE == "normal":
            current = self.normalLane_HeadNode
        elif LANE == "express":
            current = self.expressLane_HeadNode
        else:
            raise ValueError("The given 'LANE' argument must be either 'normal' or 'express'. You have as an argument for the 'LANE' value : {0}".format(LANE))

        while current:
            if not afterSplitNode:
                LIST_1.append(current.data)
            else:
                LIST_2.append(current.data)
            
            if current == splitNode:
                afterSplitNode = True
                
            current = current.next


        return [ LIST_1, LIST_2 ]

    def splitListAtIndex(self, splitIndex, LANE):
        ''' Return a list with two lists that contain the node data split after the given index on the given lane '''
        
        # Check the splitIndex & the LANE argument while establishing on what lane we have to start the iteration, so wher eto place the 'current' node value
        current = None
        LENGTH_OF_LANE = 0

        LIST_1 = list() # We will store all the node data in this list before we go pass the given index
        LIST_2 = list() # We will store all the node data in this list after we went pass the given index

        INDEX_TRACK = 0 # Keep track of the index as we move forward on the lane with the 'current' Node

        if LANE == "normal":
            current = self.normalLane_HeadNode
            LENGTH_OF_LANE = self.normalLane_Counter
        elif LANE == "express":
            current = self.expressLane_HeadNode
            LENGTH_OF_LANE = self.expressLane_Counter
        else:
            raise ValueError("The given 'LANE' argument must be either 'normal' or 'express'. You have as an argument for the 'LANE' value : {0}".format(LANE))

        if not 0 <= splitIndex < LENGTH_OF_LANE:
            raise ValueError("The given index is either too big or too small for the given lane. The length of the lane is {0} and the given index was {1}".format(LENGTH_OF_LANE, splitIndex))

        while current:
            if INDEX_TRACK < splitIndex:
                LIST_1.append(current.data)
            else:
                LIST_2.append(current.data)

            current = current.next
            INDEX_TRACK += 1

        return [ LIST_1, LIST_2 ]

    def pairsWithSum(self, target_sum, LANE):
        ''' Return the pairs of node's data that, summed, will return the target_sum on the given LANE '''
        
        LANE_DATA = list()
        PAIRS = list()

        # Check the 'LANE' argument
        if LANE == "normal":
            LANE_DATA = self.getNodeData()[0]
        elif LANE == "express":
            LANE_DATA = self.getNodeData()[1]
        else:
            raise ValueError("The given 'LANE' argument must be either 'normal' or 'express'. You have as an argument for the 'LANE' value : {0}".format(LANE))

        for permutation in itertools.permutations(LANE_DATA, 2):
            if sum(permutation) == target_sum and permutation not in PAIRS and permutation[::-1] not in PAIRS:
                PAIRS.append(tuple(permutation))

        return PAIRS

    ###################### OTHERS ######################
