class Node(object):
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None
        
        self.counter = 0

class SelfOrganizingList(object):
    def __init__(self):
        # Keep track of the head & last nodes + the length of the self organizing list throughout the methods
        self.head = None
        self.last = None

        self.length = 0

        '''

        ( ~ Description ( how the method looks ) -> return value [ done(x) / undone(empty) ] )
        
        ########################### GENERAL METHODS ###########################
   
        ~ Get length                                                                                    ( self.getLength() )                                -> integer                                      [x]
        ~ Create __len__(self) method                                                                   ( len(self) )                                       -> integer                                      [x]

        ~ Get the node data of the list                                                                 ( self.getNodeData() )                              -> list                                         [x]
        ~ Get the counter of each node in the list                                                      ( self.getNodeCounter() )                           -> dict                                         [x]
        
        ########################### GENERAL METHODS ###########################
        ########################### DEFAULT SelfOrganizingList METHODS + MORE ###########################

        ~ Append                                                                                        ( self.append(data) )                               -> None                                         [x]
        
        ~ Delete node                                                                                   ( self.deleteNode(node) )                           -> None                                         [x]
        ~ Delete at index                                                                               ( self.deleteAtIndex(index) )                       -> None                                         [x]
        ~ Delete node with data                                                                         ( self.deleteNodeWithData(data) )                   -> None                                         [x]

        ~ Move a node to front (MFT)                                                                    ( self.MFT(node) )                                  -> None                                         [x]
        ~ Transpose ( swap a node with it's previous node ) Method (TM)                                 ( self.TM(node) )                                   -> None                                         [x]

        ~ Search a node with the given data, after the node is found organize the list                  ( self.search(data) )                               -> Node object                                  [x] 
        ~ Search the node at the given index                                                            ( self.searchAtIndex(index) )                       -> Node object                                  [x]

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
        return self.length

    def __len__(self):
        ''' Return the length of the self organizing list '''
        return self.length

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
    ########################### DEFAULT SelfOrganizingList METHODS + MORE ###########################
    
    def append(self, data):
        ''' Append a node with the given data to the self organizing list '''
        if not self.head and not self.last:
            # If the self organizing list doesn't have a head node and doesn't have a last node as well, create one and create the 'last' node too, since it's the single node in the list, it is the start and also the end of it.
            self.head = Node(data)
            self.last = Node(data)
        else:
            # Create the append node and set it's properties and the properties of the current node ( which reached the end ) in such a way that the APPEND_NODE is the last node ( .prev & .next )
            APPEND_NODE = Node(data)
        
            if not self.head.next:
                # If the self.head.next is None then that means that it doesn't have a connection ( .next ) with the last node, so we will have to recreate the last node
                self.last = Node(data)

                self.last.prev = self.head
                self.head.next = self.last
            else:
                APPEND_NODE.prev = self.last 
                self.last.next = APPEND_NODE

                self.last = self.last.next

        # Increment the length of the self organizing list
        self.length += 1

    def deleteNode(self, node):
        ''' Delete the given node '''
        # Check the given node
        if type(node) != Node:
            raise ValueError("The given node argument must be of type node. You gave {0} which is of type {1}".format(node, type(node)))
        else:
            # Check if the given node was the last or head node
            if node == self.head:
                # Update the head node by getting the next node in front of it and changing it's .prev pointer
                NEXT_NODE = self.head.next
                if NEXT_NODE:
                    NEXT_NODE.prev = None
                
                # Update the head node by setting it to be the node in front of the current head node
                self.head = NEXT_NODE
            elif node == self.last:
                # Update the last node by getting the previous node behind it and changing it's .next pointer
                PREV_NODE = self.last.prev
                if PREV_NODE:
                    PREV_NODE.next = None

                # Update the last node by setting it to be node behind the current last node
                self.last = PREV_NODE
            else:
                # Change the pointers of the nodes in front and behind the node that we have to delete
                PREV_NODE = node.prev
                NEXT_NODE = node.next
                
                PREV_NODE.next, NEXT_NODE.prev = NEXT_NODE, PREV_NODE
        
        # Decrement the length of the self organizing list
        self.length -= 1

    def deleteAtIndex(self, index):
        ''' Delete the node at the given index '''
        # Check the given index
        if not 0 <= index < self.length:
            raise IndexError("The given index was either too big or too small ( < 0 ). It must be a number between 0 and {0}. You gave as index : {1}".format(self.length - 1, index))

        # Get the node at the given index and delete it by starting at the head node and iterating to the end and keeping track of the index
        current = self.head
        indexTrack = 0

        while indexTrack < index:
            current = current.next
            indexTrack += 1

        self.deleteNode(current)

    def deleteNodeWithData(self, data): 
        ''' Delete the node with the given data '''
        # Iterate over the entire self organizing list starting with the head until we find the first node that starts with the given data
        current = self.head
        
        while current:
            if current.data == data:
                break
            
            current = current.next

        # Check if the current node has been found or not
        if not current:
            raise ValueError("The given data couldn't be found in the self organizing list.")
        else:
            self.deleteNode(current)

    def MFT(self, node):
        ''' MFT = Move To Front | Move the given node to the front of the self organizing list '''
        # Check the given node
        if type(node) != Node:
            raise ValueError("The given node argument must be of type node. The value that you gave at the node argument was {0} which is of type {1}".format(node, type(node)))

        # Check if the given node is the head node
        if node == self.head:
            return
        
        # Delete the given node out of his current position
        PREV_NODE = node.prev
        NEXT_NODE = node.next

        if NEXT_NODE:
            NEXT_NODE.prev = PREV_NODE
        PREV_NODE.next = NEXT_NODE

        # Update the pointers of the given node
        node.prev = None
        node.next = self.head

        # Update the head .prev pointer
        self.head.prev = node
        
        # Update the head
        self.head = node

    def TM(self, node):
        ''' TM = Transpose Method | Swap the given node with the node behind him '''
        # Check the given node
        if type(node) != Node:
            raise ValueError("The given node must be of type node. The value that you gave at the node argument was {0} which is of type {1}".format(node, type(node)))
        
        # Swap 
        node.prev.data, node.prev.counter, node.data, node.counter = node.data, node.counter, node.prev.data, node.prev.counter

    def search(self, data):
        ''' Return the first node with the given data '''
        # Start at the head node and iterate through the entire self organizing list until we get find the first node that will have the given data
        current = self.head
        
        while current:
            if current.data == data:
                break

            current = current.next

        # Check if the current node is None. If it is None then that means that we couldn't find any node that will have the given data. Hence we will raise a value error
        if not current:
            raise ValueError("The given data couldn't be found in the self organizing list")
        else:
            # Increment the counter of the found node
            current.counter += 1

            # If the counter of the current node is smaller than the counter of the head node, then we can directly move the node to the front of the self organizing list. There is no need to iterate backwards through the list and always check if the nodes that we found have a smaller counter or not than the current node because we already node that the self organizing list is sorted from the biggest 'counter' node to the smallest one, and if the biggest one which is the head node has a smaller 'counter' value than the current node, then it is clear that the current node will have a bigger counter than all the nodes that are in front of the head node. Hence we can simply just move in front of the self organizing list using the self.MFT method ( MFT = Move To Front )
            if self.head.counter < current.counter:
                self.MFT(current)
            else:
                while current.prev:
                    if current.prev.counter < current.counter:
                        self.TM(current)
                    else:
                        break

                    current = current.prev

        # Return the found node
        return current
    
    def searchAtIndex(self, index):
        ''' Return the node at the given index ''' 
        # Check the given index
        if not 0 <= index < self.length:
            raise IndexError("The given index was either too big or too small ( < 0 ). The given node must be a number between 0 and {0}. You gave : {1}".format(self.length - 1, lane))
        
        # Start at the head node and keep track of the current node and of the index while iterating through the self organizing list and stop when the indexTrack has reached the given index
        current = self.head
        indexTrack = 0

        while indexTrack < index:
            current = current.next
            indexTrack += 1
        
        # Increment the counter of the found node
        current.counter += 1

        # Same as at the other search
        if self.head.counter < current.counter:
            self.MFT(current)
        else:
            while current.prev:
                if current.prev.counter < current.counter:
                    self.TM(current)
                else:
                    break

                current = current.prev

        # Return the found node
        return current

    ########################### DEFAULT SelfOrganizingList METHODS + MORE ###########################

x = SelfOrganizingList()

def present():
    print("----------------------------")
    print(x.getNodeData())
    print(x.getNodeCounter())
    print("-")
    y = x.last
    if y:
        print("LAST NODE -- > {0}".format(y.data))
    else:
        print("LAST NODE -- > {0}".format(y))
    print("Length -- > {0}".format(len(x)))
    print("----------------------------")

    for i in range(2):
        print()

present()

for i in range(1, 6):
    x.append(i)

present()

for i in range(3):
    x.searchAtIndex(2)
for i in range(2):
    x.searchAtIndex(4)
for i in range(45):
    x.searchAtIndex(1)

present()
