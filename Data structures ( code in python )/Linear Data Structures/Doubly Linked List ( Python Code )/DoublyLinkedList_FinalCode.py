import pprint

class Node(object):
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self):
        # Create the head node of the dllist, set it by default to none
        self.head = None

        # Keep track of the length of the dllist. Default is 0
        self.length = 0

        '''
        ( ~ Description ( how the method looks ) -> return value [ done (x) / undone ( empty ) ] )

        ############################### GENERAL METHODS ###############################
        
        ~ Get length                                         ( self.getLength )                                                                             -> number                   [x]
        ~ Create __len__(self) method                        ( len(self) )                                                                                  -> number                   [x]
    
        ~ Node at index                                      ( self.atIndex(index) )                                                                        -> number                   [x]
        ~ Get node data list                                 ( self.getNodeData() )                                                                         -> list                     [x]

        ~ Get last node                                      ( self.getLastNode() )                                                                         -> Node                     [x]
        ~ Check the dllist ( check .prev & .next )           ( self.check() )                                                                               -> True / False             []

        ############################### GENERAL METHODS ###############################

        ############################### INSERTION / DELETION ###############################

        ~ Append                                             ( self.append(data) )                                                                          -> None                     [x]
        ~ Prepend                                            ( self.prepend(data) )                                                                         -> None                     [x]

        ~ Insert after node                                  ( self.insertAfterNode(node, data) )                                                           -> None                     [x]
        ~ Insert after node data                             ( self.insertAfterNodeData(key, data) )                                                        -> None                     []
        ~ Insert at index                                    ( self.insertAtIndex(index, data) )                                                            -> None                     []

        ~ Delete node                                        ( self.deleteNode(node) )                                                                      -> None                     []
        ~ Delete at index                                    ( self.deleteAtIndex(index) )                                                                  -> None                     []

        ############################### INSERTION / DELETION  ###############################

        ############################### OTHERS  ###############################

        ~ Node swap  ( input : nodes to be swaped )                                     ( self.swapNodes(node1, node2) )                                    -> None                     []
        ~ Node swap  ( input : indexes of the nodes that need to be swapped )           ( self.swapNodesAtIndexes(index1, index2) )                         -> None                     []

        ~ Reverse                                                                       ( self.reverse() )                                                  -> None                     []

        ~ Merge ( both sorted )                                                         ( self.mergeBothSorted(cllist) )                                    -> None                     []
        ~ Merge ( both unsorted )                                                       ( self.mergeBothUnsorted(cllist) )                                  -> None                     []

        ~ Remove duplicates                                                             ( self.removeDuplicates() )                                         -> None                     []
        ~ Rotate                                                                        ( self.rotate(rotationValue) )                                      -> None                     []

        ~ Is palindrome                                                                 ( self.isPalindrome() )                                             -> True / False             []

        ~ Move tail to head                                                             ( self.moveTailToHead() )                                           -> None                     []
        ~ Sum with another dllist                                                       ( self.sumWithDLLIST() )                                            -> number                   []

        ~ Split list in half                                                            ( self.splitInHalf() )                                              -> [ dllist1, dllist2 ]     []
        ~ Split list after node                                                         ( self.splitAfterNode(node) )                                       -> [ dllist1, dllist2 ]     []
        ~ Split list at index                                                           ( self.splitAtIndex(index) )                                        -> [ dllist1, dllist2 ]     [] 

        ~ Pairs with sum                                                                ( self.pairsWithSum(sum_value) )                                    -> [ (), () .. () ]         []

        ############################### OTHERS  ###############################
        '''
        
    ############################### GENERAL METHODS ###############################
    
    def getLength(self):
        return self.length

    def __len__(self):
        return self.length

    def atIndex(self, index):
        # Check the index
        if index < 0 or index >= self.length:
            raise IndexError("The given index is too big for the dllist or is less than 0.")

        # Iterate over the entire dllist while keeping track of the index of each node. When the index that we keep track of hits the index of the dllist, return the current node
        current = self.head
        indexTrack = 0

        while current:
            if indexTrack == index:
                return current
        
            current = current.next
            indexTrack += 1
    
    def getNodeData(self):
        # Iterate over each node in the dllist and add it's data value in the nodeDataList list and after that, return the nodeDataList
        nodeDataList = list()
        current = self.head

        while current:
            nodeDataList.append(current.data)
            current = current.next
        
        return nodeDataList

    def getLastNode(self):
        # Iterate over all the nodes in the dllist while the next node in front of the current node is not None. So like that, at the end we know that the next node is 'None', so that means that we will have 'current', the last node in the dllist
        current = self.head

        while current.next:
            current = current.next

        return current

    def check(self):
        # Check the .prev & .next node
        prev = None
        current = self.head

        while current:
            if current.prev != prev:
                return False

            prev = current
            current = current.next

        return True

    ############################### GENERAL METHODS ###############################
        
    ############################### INSERTION / DELETION ###############################
    
    def append(self, data):
        # Check the 'data' argument
        if not data:
            raise ValueError("The 'data' argument must be valid") 
        
        # Check if there is a head node in the dllist. If there is not, then create one and then return 
        if not self.head:
            self.head = Node(data)
            return

        # Iterate over all the nodes in the list till we get to the last node
        current = self.head

        while current.next:
            current = current.next

        # Create the node that needs to be appended in the dllist and set its values
        appendNode = Node(data)

        appendNode.prev = current
        current.next = appendNode
        
    def prepend(self, data):
        # Check the 'data' argument
        if not data:
            raise ValueError("The 'data' argument must be valid")

        # Check if there is a head node in the dllist. If there is not, then create one and then return
        if not self.head:
            self.head = Node(data)
            return

        # Create the prepend node and set its values, set new values for the current head as well and then update the head node of the dllist
        prependNode = Node(data)

        prependNode.next = self.head
        self.head.prev = prependNode

        self.head = prependNode

    def insertAfterNode(self, node, data):
        # Check the node & data argument
        if not data:
            raise ValueError("The 'data' argument must be valid")
        
        if type(node) != Node:
            raise ValueError("The given 'node' argument must be a node type value")

        # Iterate over all the nodes in the list, once it hits the node, insert the new node
        current = self.head

        while current != node and current:
            current = current.next

        # Create the insert node
        insertNode = Node(data)

        if current.next:
            nextNode = current.next
            nextNode.prev = insertNode

            insertNode.next = nextNode

        insertNode.prev = current

        current.next = insertNode 


    ############################### INSERTION / DELETION ###############################

dllist = DoublyLinkedList()

for i in list(range(1, 5)):
    dllist.append(i)

print(" START :" )
pprint.pprint(dllist.getNodeData(), indent = 50)

for i in range(3):
    print()

dllist.insertAfterNode(dllist.head.next.next.next, "A")

for i in range(3):
    print()

print(" END: ")
pprint.pprint(dllist.getNodeData(), indent = 50)
print("CHECK : {0}".format(dllist.check()))
