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
        ~ Check the dllist ( check .prev & .next )           ( self.check() )                                                                               -> True / False             [x]

        ############################### GENERAL METHODS ###############################

        ############################### INSERTION / DELETION ###############################

        ~ Append                                             ( self.append(data) )                                                                          -> None                     [x]
        ~ Prepend                                            ( self.prepend(data) )                                                                         -> None                     [x]

        ~ Insert after node                                  ( self.insertAfterNode(node, data) )                                                           -> None                     [x]
        ~ Insert after node data                             ( self.insertAfterNodeData(key, data) )                                                        -> None                     [x]
        ~ Insert at index                                    ( self.insertAtIndex(index, data) )                                                            -> None                     [x]

        ~ Delete node                                        ( self.deleteNode(node) )                                                                      -> None                     [x]
        ~ Delete at index                                    ( self.deleteAtIndex(index) )                                                                  -> None                     [x]
        ~ Delete node with data                              ( self.deleteNodeWithData(data) )                                                              -> None                     [x]

        ############################### INSERTION / DELETION  ###############################

        ############################### OTHERS ###############################

        ~ Node swap  ( input : nodes to be swaped )                                     ( self.swapNodes(node1, node2) )                                    -> None                     [x]
        ~ Node swap  ( input : indexes of the nodes that need to be swapped )           ( self.swapNodesAtIndexes(index1, index2) )                         -> None                     []
        ~ Instant Node Swap ( input : nodes to be swaped )                              ( self.instantNodeSwap(node1, nod2) )                               -> None                     []
        ~ Instant Node Swap ( input : indexes of the node that need to be swaped )      ( self.instantNodesSwapAtIndexes(index1, index2) )                  -> None                     []

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

        ############################### OTHERS ###############################
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

            # Increment the length of the dllist
            self.length += 1

            return

        # Iterate over all the nodes in the list till we get to the last node
        current = self.head

        while current.next:
            current = current.next

        # Create the node that needs to be appended in the dllist and set its values
        appendNode = Node(data)

        appendNode.prev = current
        current.next = appendNode

        # Increment the length of the dllist
        self.length += 1
        
    def prepend(self, data):
        # Check the 'data' argument
        if not data:
            raise ValueError("The 'data' argument must be valid")

        # Check if there is a head node in the dllist. If there is not, then create one and then return
        if not self.head:
            self.head = Node(data)

            # Increment the length of the dllist
            self.length += 1

            return

        # Create the prepend node and set its values, set new values for the current head as well and then update the head node of the dllist
        prependNode = Node(data)

        prependNode.next = self.head
        self.head.prev = prependNode

        self.head = prependNode

        # Increment the length of the dllist
        self.length += 1

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

        # Increment the length of the dllist
        self.length += 1
    
    def insertAfterNodeData(self, key, data):
        # Check the key & data
        if not key or not data:
            raise ValueError("The key & the passed in data arguments are not valid.")

        # Iterate over the dllist and try to get the node with the specified 'key'
        current = self.head

        while current:
            if current.data == key:
                break
            
            current = current.next

        if not current:
            raise ValueError("The given 'key' argument couldn't be found in the dllist.")

        # Create the insert node
        insertNode = Node(data)

        if current.next:
            nextNode = current.next
            nextNode.prev = insertNode 

            insertNode.next = nextNode

        insertNode.prev = current
        current.next = insertNode

        # Increment the length of the dllist
        self.length += 1

    def insertAtIndex(self, index, data):
        # Check the index & the data
        if index > self.length or index < 0:
            raise IndexError("The given index is either too big for the dllist or it's too small ( < 0 )")

        if not data:
            raise ValueError("The given data value must be valid.")

        # In case the index is the length of the dllist, append a new node to the dllist with the given data
        if index == self.length:
            self.append(data)
            
            # Increment the length of the dllist
            self.length += 1

            return

        # Iterate over the dllist and get to the given index by keeping track of the current index and of the current node
        current = self.head
        indexTrack = 0

        while indexTrack < index:
            current = current.next
            indexTrack += 1
        
        # Create the insert node
        insertNode = Node(data)

        if current.next:
            nextNode = current.next

            nextNode.prev = insertNode
            insertNode.next = nextNode

        insertNode.prev = current
        current.next = insertNode

        # Increment the length of the dllist
        self.length += 1

    def deleteNode(self, node):
        # Check the node
        if type(node) != Node:
            raise ValueError("The passed in 'node' argument must be of type 'Node'")

        # Iterate over the dllist till we find the given node ( keep track of the current & previous node )
        current = self.head

        while current:
            if current == node:
                break

            prev = current 
            current = current.next

        # Check if the current node is the node that we got in the args, if not raise ValueError
        if not current:
            raise ValueError("The passed in node couldn't be found in the dllist.")

        # Check if the node that must be deleted is a the head node 
        if current == self.head:
            if current.next:
                nextNode = current.next

                nextNode.prev = None
            
            self.head = current.next
            current = None
        
            # Decrement length of the dllist
            self.length -= 1

            return

        # The node that must be deleted is not the head node, so modify the changes of the previous & next node without making any changes to self.head
        prev = current.prev

        if current.next:
            nextNode = current.next

            nextNode.prev = prev
        
        prev.next = current.next
        current = None

        # Decrement the length of the dllist
        self.length -= 1

    def deleteNodeAtIndex(self, index):
        # Check the given index
        if index >= self.length or index < 0:
            raise IndexError("The given index either too big for the dllist or it's too small ( < 0 ).")

        # Iterate over the dllist while keeping track of the current node and of the index
        current = self.head
        indexTrack = 0

        while indexTrack < index:
            current = current.next
            indexTrack += 1

        # Check if the node that must be deleted is the head node
        if index == 0:
            if self.head.next:
                nextNode = self.head.next

                nextNode.prev = None

            self.head = self.head.next

            # Decrement the length of the dllist
            self.length -= 1
        
        # The current node is not the head node
        prev = current.prev

        if current.next:
            nextNode = current.next

            nextNode.prev = prev
            
        prev.next = current.next

        # Decrement the length of the list
        self.length -= 1

    def deleteNodeWithData(self, data):
        # Check the passed in 'data' value
        if not data:
            raise ValueError("The passed in data value is not valid.")

        # Iterate over the dllist and keep track of the current node. If the current node will have the same value as the 'data' arg, break the loop
        current = self.head

        while current:
            if current.data == data:
                break

            current = current.next

        # Check the current node
        if not current:
            raise ValueError("The passed in 'data' value couldn't be found in the dllist.")

        # Check if the current node is the head node
        if current == self.head:
            if current.next:
                nextNode = current.next

                nextNode.prev = None

            self.head = current.next
            current = None

            # Decrement the length of the dllist
            self.length -= 1

            return

        # The current node is not the head node - >
        prev = current.prev
        if current.next:
            nextNode = current.next

            nextNode.prev = prev

        prev.next = current.next

        # Decrement the length of the dllist
        self.length -= 1

    ############################### INSERTION / DELETION ###############################
        
    ############################### OTHERS ###############################

    def swapNodes(self, node1, node2):
        # Check the nodes 
        if type(node1) != Node and type(node2) != Node:
            raise ValueError("The given nodes must have a 'Node' type")

        if node1.data == node2.data:
            return
        
        # Get the prev & next nodes
        node1_prev = node1.prev
        node1_next = node1.next

        node2_prev = node2.prev
        node2_next = node2.next

        # Swap .prev & .next values
        if node1_prev and node2_prev and node1_next and node2_next:
            node1.next, node1.prev, node2.next, node2.prev, node1_prev.next, node2_prev.next, node1_next.prev, node2_next.prev = node2_next, node2_prev, node1_next, node1_prev, node2, node1, node2, node1
        elif node1 == self.head and node2_next:
            node1.next, node1.prev, node2.next, node2.prev, node2_prev.next, node1_next.prev, node2_next.prev = node2_next, node2_prev, node1_next, node1_prev, node1, node2, node1
            self.head = node2
        elif node2 == self.head and node1_next:
            node1.next, node1.prev, node2.next, node2.prev, node1_prev.next, node1_next.prev, node2_next.prev = node2_next, node2_prev, node1_next, node1_prev, node2, node2, node1
            self.head = node1
        elif not node1_next and node2 != self.head:
            node1.next, node1.prev, node2.next, node2.prev, node1_prev.next, node2_prev.next, node2_next.prev = node2_next, node2_prev, node1_next, node1_prev, node2, node1, node1
        elif not node2_next and node1 != self.head:
            node1.next, node1.prev, node2.next, node2.prev, node1_prev.next, node2_prev.next, node1_next.prev = node2_next, node2_prev, node1_next, node1_prev, node2, node1, node2
        elif node1 == self.head and not node2_next:
            node1.next, node1.prev, node2.next, node2.prev, node2_prev.next, node1_next.prev = node2_next, node2_prev, node1_next, node1_prev, node1, node2
            self.head = node2
        elif node2 == self.head and not node1_next:
            node1.next, node1.prev, node2.next, node2.prev, node1_prev.next,  node2_next.prev = node2_next, node2_prev, node1_next, node1_prev, node2, node1
            self.head = node1

    def swapNodesAtIndexes(self, index1, index2):
        # Check the indexes
        if index1 >= self.length or index2 >= self.length or index1 < 0 or index2 < 0:
            raise IndexError("The given indexes are either too big for the dllist or too small ( < 0 ).")

        # If both indexes are the same than, there is nothing to swap
        if index1 == index2:
            return

        # Iterate over the dllist and get the nodes
        current = self.head
        indexTrack = 0
    
        # Create the nodes
        node1_prev = None
        node1 = None
        node1_next = None

        node2_prev = None
        node2 = None
        node2_next = None

        while indexTrack <= max([index1, index2]):
            if indexTrack == index1:
                node1 = current
                node1_prev = node1.prev
                node1_next = node1.next
            if indexTrack == index2:
                node2 = current
                node2_prev = node2.prev
                node2_next = node2.next

            indexTrack += 1 
            current = current.next
       
        print("node1 : {0}".format(node1.data))
        print("node2 : {0}".format(node2.data))

        # Swap .prev & .next values
        if node1_prev and node2_prev and node1_next and node2_next:
            node1.next, node1.prev, node2.next, node2.prev, node1_prev.next, node2_prev.next, node1_next.prev, node2_next.prev = node2_next, node2_prev, node1_next, node1_prev, node2, node1, node2, node1
        elif node1 == self.head and node2_next:
            node1.next, node1.prev, node2.next, node2.prev, node2_prev.next, node1_next.prev, node2_next.prev = node2_next, node2_prev, node1_next, node1_prev, node1, node2, node1
            self.head = node2
        elif node2 == self.head and node1_next:
            node1.next, node1.prev, node2.next, node2.prev, node1_prev.next, node1_next.prev, node2_next.prev = node2_next, node2_prev, node1_next, node1_prev, node2, node2, node1
            self.head = node1
        elif not node1_next and node2 != self.head:
            node1.next, node1.prev, node2.next, node2.prev, node1_prev.next, node2_prev.next, node2_next.prev = node2_next, node2_prev, node1_next, node1_prev, node2, node1, node1
        elif not node2_next and node1 != self.head:
            node1.next, node1.prev, node2.next, node2.prev, node1_prev.next, node2_prev.next, node1_next.prev = node2_next, node2_prev, node1_next, node1_prev, node2, node1, node2
        elif node1 == self.head and not node2_next:
            node1.next, node1.prev, node2.next, node2.prev, node2_prev.next, node1_next.prev = node2_next, node2_prev, node1_next, node1_prev, node1, node2
            self.head = node2
        elif node2 == self.head and not node1_next:
            node1.next, node1.prev, node2.next, node2.prev, node1_prev.next,  node2_next.prev = node2_next, node2_prev, node1_next, node1_prev, node2, node1
            self.head = node1

    def instantNodeSwap(self, node1, node2):
        # Check the nodes
        if not node1 or not node2:
            raise ValueError("The given nodes are not valid.")

        if node1 == node2:
            return

        # Swap only the data
        node1.data, node2.data = node2.data, node1.data

    def instantNodeSwapAtIndexes(self, index1, index2):
        # Check the indexes
        if index1 > self.length or index2 > self.length or index1 < 0 or index2 < 0:
            raise IndexError("The given indexes are either too big for the dllist or too small ( < 0 ).")

        if index1 == index2:
            return

        # Get the nodes at the given indexes by keeping track of the current node & of the index
        current = self.head
        indexTrack = 0

        # Create the nodes
        node1 = None
        node2 = None

        while indexTrack <= max([index1, index2]):
            if indexTrack == index1:
                node1 = current
            if indexTrack == index2:
                node2 = current

            indexTrack += 1
            current = current.next

        # Swap the data of the nodes
        node1.data, node2.data = node2.data, node1.data

    ############################### OTHERS ###############################

dllist = DoublyLinkedList()

for i in list(range(1, 6)):
    dllist.append(i)

print(" START ( length : {0} ) : ".format(len(dllist)))
pprint.pprint(dllist.getNodeData(), indent = 50)

for i in range(3):
    print()

# 0 1 2 3 4
dllist.instantNodeSwap(dllist.head, dllist.head.next.next.next)

for i in range(3):
    print()

print(" END ( length : {0} ) : ".format(len(dllist)))
pprint.pprint(dllist.getNodeData(), indent = 50)
print("CHECK: {0}".format(dllist.check()))
