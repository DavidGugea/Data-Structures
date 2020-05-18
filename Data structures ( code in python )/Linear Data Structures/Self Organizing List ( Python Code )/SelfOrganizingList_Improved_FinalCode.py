class Node(object):
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None
        
        self.counter = 0

class SelfOrganizingList(object):
    def __init__(self):
        self.head = None
        '''

        ( ~ Description ( how the method looks ) -> return value [ done(x) / undone(empty) ] )
        
        ########################### GENERAL METHODS ###########################
   
        ~ Get length                                                                                    ( self.getLength() )                                -> integer                                      []
        ~ Create __len__(self) method                                                                   ( len(self) )                                       -> integer                                      []

        ~ Get the node data of the list                                                                 ( self.getNodeData() )                              -> list                                         []
        ~ Get the counter of each node in the list                                                      ( self.getNodeCounter() )                           -> dict                                         []
        
        ########################### GENERAL METHODS ###########################
        ########################### DEFAULT SelfOrganizingList METHODS + MORE ###########################

        ~ Append                                                                                        ( self.append(data) )                               -> None                                         []
        
        ~ Delete node                                                                                   ( self.deleteNode(node) )                           -> None                                         []
        ~ Delete at index                                                                               ( self.deleteAtIndex(index) )                       -> None                                         []
        ~ Delete node with data                                                                         ( self.deleteNodeWithData(data) )                   -> None                                         []

        ~ Move a node to front (MFT)                                                                    ( self.MFT(node) )                                  -> None                                         []
        ~ Transpose ( swap a node with it's previous node ) Method (TM)                                 ( self.TM(node) )                                   -> None                                         []

        ~ Search a node with the given data, after the node is found organize the list                  ( self.search(data) )                               -> Node object                                  [] 

    
        ########################### DEFAULT SelfOrganizingList METHODS + MORE ###########################
        ########################### OTHERS ###########################
        
        ~ Merge data from another self organizing list                                                  ( self.merge(MERGE_SOL) )                           -> None                                         []
        
        ~ Remove duplicates                                                                             ( self.removeDuplicates() )                         -> None                                         []
        ~ Is palindrome                                                                                 ( self.isPalindrome() )                             -> True / False                                 []

        ~ Sum with another self organizing list                                                         ( self.SUM_WITH(SUM_SOL) )                          -> None                                         []
        
        ~ Split list in half                                                                            ( self.splitInHalf() )                              -> [ list_1, list_2 ]                           []
        ~ Split list after node                                                                         ( self.splitAfterNode(node) )                       -> [ list_1, list_2 ]                           []
        ~ Split list at index                                                                           ( self.splitAtIndex(index) )                        -> [ list_1, list_2 ]                           []

        ~ Pairs with sum                                                                                ( self.pairsWithSum(sum_value) )                    -> [ tuple_1, tuple_2 , ... tuple_x ]           []
    
        ########################### OTHERS ###########################

        '''

    ########################### GENERAL METHODS ###########################

    def getLength(self):
        ''' Return the length of the self organizing list '''
        length = 0
        current = self.head
        
        while current:
            length += 1
            current = current.next

        return current

    def __len__(self):
        ''' Return the length of the self organizing list '''
        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next

        return current

    def getNodeData(self):
        ''' Return a list that contains all the node data in the self organizing list '''
        NODE_DATA_LIST = list()
        current = self.head

        while current:
            NODE_DATA_LIST.append(current.data)
            current = current.next

        return NODE_DATA_LIST

    def getNodeCounter(self):
        ''' Return a dictionary that contains all the node counters from the self organizing list for all the nodes. ( NODE DATA ( key ) -> NODE COUNTER ( value ) ) '''
        NODE_COUNTER = dict()
        current = self.head

        while current:
            NODE_COUNTER[current.data] = current.counter
            current = current.next

        return NODE_COUNTER

    ########################### GENERAL METHODS ###########################
