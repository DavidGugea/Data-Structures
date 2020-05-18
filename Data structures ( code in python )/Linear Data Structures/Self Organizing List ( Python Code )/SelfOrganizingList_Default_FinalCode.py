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
        
        ~ Get node data of the list                                                                 ( self.getNodeData() )                                                  -> list                         [x]
        ~ Get the counter of each node in the list                                                  ( self.getNodeCounter() )                                               -> dict                         [x]

        ########################### GENERAL METHODS ###########################
        ########################### DEFAULT SelfOrganizingList METHODS ###########################
    
        ~ Append a new node to the list                                                             ( self.append(data) )                                                   -> None                         [x]
        ~ Delete a node from the list                                                               ( self.delete(node) )                                                   -> None                         [x]

        ~ Move a node to front (MFT)                                                                ( self.MFT(node) )                                                      -> None                         [x]
        ~ Transpose ( swap the given node with it's previous node ) Method (TM)                     ( self.TM(node) )                                                       -> None                         [x]

        ~ Search a node with the given data, after the node is found organize the list              ( self.search(data) )                                                   -> Node object                  [x]

        ########################### DEFAULT SelfOrganizingList METHODS ###########################

        '''

    ########################### GENERAL METHODS ###########################

    def getNodeData(self):
        ''' Returns a list with all the node data '''
        # Create the NODE_DATA_LIST
        NODE_DATA_LIST = list()

        # Start from the head and iterate to the end with the 'current' variable while appendning the node data in the NODE_DATA_LIST. In the end return the NODE_DATA_LIST
        current = self.head

        while current:
            NODE_DATA_LIST.append(current.data)
            current = current.next

        return NODE_DATA_LIST

    def getNodeCounter(self):
        ''' Return a dict with the .counter property for all the node data in the self organizing list ( NODE DATA ( key ) -> COUNTER PROPERTY ( value ) ) '''
        NODE_COUNTER = dict()
        current = self.head

        while current:
            NODE_COUNTER[current.data] = current.counter
            current = current.next

        return NODE_COUNTER

    ########################### GENERAL METHODS ###########################
    ########################### DEFAULT SelfOrganizingList METHODS ###########################

    def append(self, data):
        ''' Append a node with the given data '''
        if not self.head:
            # If the self organizing list doesn't have a head node, create one
            self.head = Node(data)
        else:
            # If it has a head node, start at the head node with a variable called 'current' and iterate to the end of the self organizing list
            current = self.head

            while current.next:
                current = current.next

            # After reaching the end of the self organizing list, create an APPEND_NODE and set up the .prev pointer of this node to point (.prev) at the last node of the self organizing list, and change the last pointer to point (.next) at the APPEND_NODE, and in that way we have the APPEND_NODE at the end 
            APPEND_NODE = Node(data)

            APPEND_NODE.prev = current
            current.next = APPEND_NODE

    def delete(self, node):
        ''' Delete the given node '''
        # Check if the given node is the head node ( if that is the case then just simply move the self.head value to the self.head.next node )
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            PREV_NODE = node.prev
            NEXT_NODE = node.next

            PREV_NODE.next = NEXT_NODE
            NEXT_NODE.prev = PREV_NODE

    def MFT(self, node):
        ''' MFT means "MoveToFront", and it moves the given node to the front, so it will become the head node '''
        # Check the given node
        if type(node) != Node:
            raise ValueError("The given node argument must be of type 'node'. You gave {0} at the node argument which is of type {1}.".format(node, type(node)))

        # Check if there is a head node, if there is not then we can't move anything to the front, so raise an error
        if not self.head:
            raise Exception("The self organizing list is empty. Make sure you append nodes in it ( at least 2 ) before trying to use this function.")

        # If the given node is already the head node then we don't have to move anything at the front since the head node is already at the front, so return
        if node is self.head:
            return

        # Change the properties of the prev & next nodes of the given node to point at each other so that the node won't stay in between them anymore
        PREV_NODE = node.prev
        NEXT_NODE = node.next

        PREV_NODE.next = NEXT_NODE
        if NEXT_NODE:
            NEXT_NODE.prev = PREV_NODE

        # Change the pointers of the given node and of the current head node so that the given node becomes the head node
        node.next = self.head
        node.prev = None 

        self.head.prev = node
        self.head = node

    def TM(self, node):
        ''' TM means "Transpose Method", and it will swap the given node with the node before him'''
        # Check the given node
        if type(node) != Node:
            raise ValueError("The given node must be of type node. You gave {0} at the node argument which is of type {1}".format(node, type(node)))

        # Check if the given node is the head node. If it is the head node then just simply return since the head node can't be swapped with what is behind him because what is behind the head node is "None", so nothing can be swapped
        if node is self.head:
            return
        else:
            node.data, node.counter, node.prev.data, node.prev.counter = node.prev.data, node.prev.counter, node.data, node.counter

    def search(self, data):
        ''' Search the node with the given data and organize it.'''
        # Start searching at the head node and iterate through the self organizing ist
        current = self.head 

        while current:
            if current.data == data:
                break

            current = current.next

        # Check if the given data could be found in the list, if not raise an error, if it was found in the list then increase the counter of the node and organize the list using the MFT and/or TF
        if not current:
            raise ValueError("The given data couldn't be found in the self organizing list.")
        else:
            #
            current.counter += 1

            # If the head counter is smaller than the current counter then use MFT, otherwise, iterate through the list backwards ( using .prev ) and use TM when the counter of the found node is bigger than the counter of the current node
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
        
    ########################### DEFAULT SelfOrganizingList METHODS ###########################
