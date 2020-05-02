# Create an "IDS" dict. We will keep all the ids ( as keys ) & nodes ( as values ) in it when we will use the method 'setNearNodes' for each node. We create this because we will need to search through all the id's when we want to get the next / previous node. Why we have to KVP 0 < - > None by default in it will be exaplained later 
IDS = { 0 : None }

'''
THE XOR Linked List is a memory efficient Doubly Linked List.
Before we explain how it works here are some XOR ( ^ ) operation rules:

x ^ x = 0 
x ^ 0 = x
x ^ y ^ y = x ^ 0 = x

How a XOR Linked List works:
Each node has a store_address. The store_address represents the XOR value between it's previous & it's next node
We will take as an example a node with the data X

So we will have the node X

Let's set it's near nodes to be None & another Node with data value Y
When we will set the near nodes, we will insert them & their ids in the IDS dict too 

Let's say that the node with the data value X has the ID of 1234
And the node with the data value Y has the ID of 5678
We suppose that every None value is treated with the ID of 0

So, our IDS dict will look like this : { 0 : None, 1234 : <main.__Node__ ... > ( node with data value x ), 5678 : < main.__Node__ ... > ( node with data value y ) } 

Then, if we set the near nodes of the X node to be None & the node with data value Y, the node with the data value X will have a store_address:
    None ID ^ node with data value Y ID = 0 ^ 5678 = 5678

So, the X Node has the store address 5678

Now, if we will try to get to the next node, looking back at the XOR operation rules ( x ^ y ^ y ) we will need the previous node
so, if we will get the next node using the None value we will have to make this operation:
    next_node_address = self.store_address ^ prev_node of X Node = self.store_address ^ None = 0 ^ 5678 ^ 0 = 5678 ^ 0 ^ 0 = 5678 ^ 0 = 5678

so, we have now the next_node_address which is 5678 ( the ID of the second node )
Now, in order to return the next node we will search for all the ID'S in the IDS dict made on line 1 and see which node has the ID of 5678, and we will find the second node ( node with data value Y )

'''

def getByAddress(SEARCH_ID):
    # Check if the id is in the IDS dict's keys, if there is, return it's value from the dict, otherwise raise a value error
    if SEARCH_ID in IDS.keys(): return IDS[SEARCH_ID]
    else: raise ValueError("The search id couldn't be found in the IDS dict. Try again.") 

class Node(object):
    def __init__(self, data):
        self.data = data

        # self.store_address defaults to None. Represents the XOR ( ^ )  between prev & next node addresses ( address == id(...) )
        self.store_address = None

    def getAddress(self):
        # Return the id of the main class node ( self )
        return id(self)

    def setNearNodes(self, prev_node, next_node):
        # Add both node's ids if they are not None. The 'None' value will always be treated as ID 0 
        if prev_node != None:
            IDS[id(prev_node)] = prev_node 
        if next_node != None:
            IDS[id(next_node)] = next_node

        # Get the addresses ( ids ) of both nodes again using variables ( if they are None, set their addresses to 0 ! )
        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.getAddress()

        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.getAddress()

        # Set the store address using the xor operation
        self.store_address = prev_address ^ next_address

    def getNextNode(self, prev_node):
        # Check if the node has a store_address ( if it doesn't raise an exception )
        if self.store_address == None:
            raise Exception("The node doesn't have a store address. Hence it can't find the next node. Make sure you set the near nodes first.")

        # Get the address of the prev_node ( remember that None is treated with ID ( address ) of 0 )
        if prev_node == None:
            prev_address = 0 
        else:
            prev_address = prev_node.getAddress()
        
        # Get the next_node_address by 'xoring' the store_address with the prev_node address
        # next_node_address = self.store_address ^ prev_address = prev_address ^ next_address ^ prev_address = next_address ^ prev_address ^ prev_address = next_address ^ 0 = next_address
        next_node_address = self.store_address ^ prev_address
        
        # Return the next_node by using the getByAddress function that will look through all the id's and return the one that has the matched ID with the next_node_address
        return getByAddress(next_node_address)

    def getPrevNode(self, next_node):
        # Same as the next node, but look for the prev_node_address. Begin again by checking the store_address
        if self.store_address == None:
            raise Exception("The node doesn't have a store address. Hence it can't find the previous node. Make sure you set the near nodes first.")

        # Get the address of the next_node ( remember that None is treated with ID ( address ) of 0 )
        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.getAddress()

        # Get the prev_node_address by 'xoring' the store_address with the next_node address
        # prev_node_address = self.store_address ^ next_address = prev_address ^ next_address ^ next_address = prev_address ^ 0 = prev_address
        prev_node_address = self.store_address ^ next_address

        # Return the prev_noed by ussing the getByAddress function that will look through all the id's and return the one that has the matched ID with the prev_node_address
        return getByAddress(prev_node_address)

class XORLinkedList(object):
    def __init__(self):
        # Keep track of the head & last node
        self.head = None
        self.last = None

        self.length = 0


        '''
        ( ~ Description ( how the method looks ) -> return value [ done(x) / undone(empty) ] )

        ######################### GENERAL METHODS #########################

        ~ Get length                                                                        (self.getLength )                                   -> number                       []
        ~ Create __len__(self) method                                                       ( len(self) )                                       -> number                       []

        ~ Node at index                                                                     ( self.atIndex(index) )                             -> node                         []
        ~ Get node data list                                                                ( self.getNodeData() )                              -> list                         []

        ~ Get last node                                                                     ( self.getLastNode() )                              -> node                         []
        ~ Check the XOR Linked List, chjeck .prev & .next                                   ( self.check() )                                    -> True / False                 []

        ######################### GENERAL METHODS #########################

        ######################### INSERTION / DELETION #########################

        ~ Append                                                                            ( self.append(data) )                               -> None                         []
        ~ Prepend                                                                           ( self.prepend(data) )                              -> None                         []
    
        ~ Insert after node                                                                 ( self.insertAfterNode(node, data) )                -> None                         []
        ~ Insert after node data                                                            ( self.insertAfterNodeData(key, data) )             -> None                         []
        ~ Insert at index                                                                   ( self.insertAtIndex(index, data) )                 -> None                         []

        ~ Delete node                                                                       ( self.deleteNode(node) )                           -> None                         []
        ~ Delete at index                                                                   ( self.deleteAtIndex(index) )                       -> None                         []
        ~ Delete node with data                                                             ( self.deleteNodeWithData(data) )                   -> None                         []
            
        ######################### INSERTION / DELETION #########################

        ######################### OTHERS #########################

        ~ Node Swap ( input : nodes to be swaped )                                          ( self.nodeSwap(node1, node2) )              -> None                         []
        ~ Node Swap ( input : indexes of the nodes that need to be swapped )                ( self.nodeSwapAtIndexes(index1, index2) )   -> None                         []

        ~ Reverse                                                                           ( self.reverse() )                                  -> None                         []

        ~ Merge ( both sorted )                                                             ( self.mergeBothSorted(MERGE_XLLIST) )              -> None                         []
        ~ Merge ( both unsorted )                                                           ( self.mergeBothSorted(MERGE_XLLIST) )              -> None                         []

        ~ Remove duplicates                                                                 ( self.removeDuplicates() )                         -> None                         []
        ~ Rotate                                                                            ( self.rotate(rotation_value) )                     -> None                         []
    
        ~ Is Palindrome                                                                     ( self.isPalindrome() )                             -> True / False                 []

        ~ Move tail to head                                                                 ( self.moveTailToHead() )                           -> None                         []
        ~ Sum with another XLLIST                                                           ( self.sumWithXLLIST(SUM_XLLIST) )                  -> None                         []

        ~ Split list in half                                                                ( self.splitInHalf() )                              -> [ XLLIST_1, XLLIST_2 ]       []
        ~ Split list after node                                                             ( self.splitAfterNode(node) )                       -> [ XLLIST_1, XLLIST_2 ]       []
        ~ Split list at index                                                               ( self.splitAtIndex(index) )                        -> [ XLLIST_1, XLLIST_2 ]       []
    
        ~ Pairs with sum                                                                    ( self.pairsWithSum(sum_value) )                    -> [ [], [], ... [] ]           []

        ######################### OTHERS #########################

        '''

    ######################### GENERAL METHODS #########################

    def getLength(self):
        return self.length

    def __len__(self):
        return self.length

    def atIndex(self, index):
        # Check the index
        if not 0 <= index < self.length:
            raise IndexError("The index is either too big for the XOR Linked List or too small ( < 0 ) ")

        # Keep track of the index & the prev & current nodes  
        indexTrack = 0

        # The reason we keep track of the prev node too is because, in order to get the next node of the current node ( to move ), we need the previous node 
        prev = None
        current = self.head

        # Iterate through the list till the index track will reach the border ( index ). At the end, current will be the node at the given index 
        while indexTrack < index:
            temp = current
            current = current.getNextNode(prev)
            prev = temp 

            indexTrack += 1

        # Return the node at the given index
        return current

    def getNodeData(self):
        # Create a list that will have all the .data properties from all the nodes in the XOR Linked List 
        nodeDataList = [self.head.data] 

        # Iterate over the XOR Linked List and add all the .data properties from all nodes.
        prev = None
        current = self.head
        
        # We need the prev node because we need to move forward with the current node. In order to move forward with the current node we need the previous node ( for the address / ID )
        while current.getNextNode(prev):
            temp = current
            current = current.getNextNode(prev)
            prev = temp

            nodeDataList.append(current.data)

        return nodeDataList

    def getLastNode(self):
        return self.last

    ######################### GENERAL METHODS #########################

    ######################### INSERTION / DELETION #########################

    def append(self, data):
        # Create a new node called that will have the given data
        appendNode = Node(data)

        # Check if there is a head node, if there is then iterate to the last node. If there isn't set it to the new node
        if self.head == None:
            # Set the new head node 
            self.head = appendNode

            # Set the near nodes of the head node to be both None ( None < - > HEAD NODE < - > None ) 
            self.head.setNearNodes(None, None)

            # Update the last node 
            self.last = self.head
        else:
            # Keep track of the previous & current node
            prev = None
            current = self.head

            # Iterate over the XOR Linked List till the end ( till the next node of the current node will be None, so the last node )
            while current.getNextNode(prev):
                # Create a new temp variable to store the current, 'current' node
                temp = current

                # The current will be the next node after the current 
                current = current.getNextNode(prev)

                # Update the prev to be the 'previous current', before it 'transformed' in the next node  
                prev = temp
    
            # Reset the near nodes of the last node in the XOR Linked List to be prev and the new append node
            current.setNearNodes(prev, appendNode)

            # Set the new near nodes of the append node to be the last node of the XOR Linked List and None as it's next node which will make the 'appendNode' the new last node of the XOR Linked List 
            appendNode.setNearNodes(current, None)

            # Update the last node
            self.last = appendNode

        # Increment the legth of the linked list
        self.length += 1
   
    def prepend(self, data):
        # Create the prepend node with the given data
        prependNode = Node(data)

        # Check if there is a head node or not 
        if self.head == None:
            # Create the new head node
            self.head = prependNode
            self.head.setNearNodes(None, None)
        else:
            # Set it's near nodes to be None and the head node of the XLLIST
            prependNode.setNearNodes(None, self.head)
            
            # Reset the near nodes of the XLLIST
            self.head.setNearNodes(prependNode, self.head.getNextNode(None))

            # Update the head of the XLLIST
            self.head = prependNode
    
        # Increment the length of the XLLIST
        self.length += 1

    def insertAfterNode(self, node, data):
        # Check the node
        if type(node) != Node:
            raise ValueError("The given 'node' argument must be of 'Node' type.")

        # Create the insert node with the given data 
        insertNode = Node(data)

        # Iterate over the entire XLLIST and search for the given search node
        prev = None
        current = self.head

        while current != node:
            temp = current
            current = current.getNextNode(prev)
            prev = temp
            
            if current == None:
                raise ValueError("The given search node couldn't be found in the XLLIST.")
        
        # Get the next node and reset its near nodes
        nextNode = current.getNextNode(prev)
        if nextNode:
            nextNode.setNearNodes(insertNode, nextNode.getNextNode(current))

        # Reset the near nodes for the insert node & the current node  
        insertNode.setNearNodes(current, nextNode)
        current.setNearNodes(prev, insertNode)

        # Increment the length of the XLLIST
        self.length += 1

    def insertAfterNodeData(self, key, data):
        # Create the insert node with the given data
        insertNode = Node(data)

        # Search for the node with the given 'key' data property
        prev = None
        current = self.head

        while current.data != key:
            temp = current
            current = current.getNextNode(prev)
            prev = temp

            if current == None:
                raise ValueError("The given 'key' data property couldn't be found in the XOR Linked List.")
    
        # Get the next node and reset its near nodes
        nextNode = current.getNextNode(prev)
        if nextNode:
            nextNode.setNearNodes(insertNode, nextNode.getNextNode(current))

        # Reset the near nodes for the insert node & the current node
        insertNode.setNearNodes(current, nextNode)
        current.setNearNodes(prev, insertNode)
    
        # Increment the length of the XLLIST
        self.length += 1

    def insertAtIndex(self, index, data):
        # Check the given index
        if not 0 <= index < self.length:
            raise IndexError("The given index is either too big for the XOR Linked List or too small ( < 0 ).")

        # Create the insert node with the given data
        insertNode = Node(data)

        # Iterate through the list by keeping track of the prev-, current-node & index.
        indexTrack = 0

        prev = None
        current = self.head

        while indexTrack < index - 1:
            temp = current
            current = current.getNextNode(prev)
            prev = temp

            indexTrack += 1

        # Get the next node and reset its near nodes
        nextNode = current.getNextNode(prev)
        if nextNode:
            nextNode.setNearNodes(insertNode, nextNode.getNextNode(current))

        # Reset the near nodes for the insert node & the current node  
        insertNode.setNearNodes(current, nextNode)
        current.setNearNodes(prev, insertNode)
        
        # Increment the length of the XLLIST
        self.length += 1

    def deleteNode(self, node):
        # Check the given node
        if type(node) != Node:
            raise ValueError("The given 'node' argument must be of type 'Node'")

        # Check if the given node is a head node
        if node == self.head:
            # Reset the near nodes for the next node
            nextNode = self.head.getNextNode(None)
            if nextNode:
                nextNode.setNearNodes(None, nextNode.getNextNode(self.head))
            
            # Update the head
            temp = self.head
            self.head = nextNode
            temp = None
        else:
            # Iterate over the XLLIST till we get to the given node
            prev = None
            current = self.head

            while current != node:
                temp = current
                current = current.getNextNode(prev)
                prev = temp 

                if current == None:
                    raise ValueError("The given node couldn't be found in the XLLIST.")

            print("PREV     -- > {0}".format(prev.data))
            print("CURRENT  -- > {0}".format(current.data))

            # Get the next node and reset it's near nodes
            nextNode = current.getNextNode(prev)
            if nextNode:
                nextNode.setNearNodes(prev, nextNode.getNextNode(current))
            
            # Reset the near nodes for the previous node & delete the current node
            prev.setNearNodes(prev.getPrevNode(current), nextNode)
            current = None

        # Decrement the length of the XLLIST
        self.length -= 1

    def deleteAtIndex(self, index):
        # Check the given index 
        if not 0 <= index < self.length:
            raise IndexError("The given index is either too big for the XOR Linked List or too small ( < 0 )")

        # Check if the given index is 0 ( so if the nodes that must be deleted is the head node )
        if index == 0:
            # Get the next node after the head node and reset its near nodes 
            nextNode = self.head.getNextNode(None)
            if nextNode:
                nextNode.setNearNodes(None, nextNode.getNextNode(self.head))

            # Update the head node
            temp = self.head 
            self.head = nextNode
            temp = None
        else:
            # Keep track of the index & previous & next nodes
            indexTrack = 0

            prev = None
            current = self.head

            while indexTrack < index:
                temp = current
                current = current.getNextNode(prev)
                prev = temp
                
                indexTrack += 1

            # Get the next node & reset it's near nodes
            nextNode = current.getNextNode(prev)
            if nextNode:
                nextNode.setNearNodes(prev, nextNode.getNextNode(current))
    
            # Reset the near nodes of the prev node & delete the current node
            prev.setNearNodes(prev.getPrevNode(current), nextNode)
            current = None

        # Decrement the length of the XLLIST
        self.length -= 1

    def deleteNodeWithData(self, data):
        # Check if the node with the data that must be deleted is the head node
        if data == self.head.data:
            # Get the next node and reset it's near nodes
            nextNode = self.head.getNextNode(None)
            if nextNode:
                nextNode.setNearNodes(None, nextNode.getNextNode(self.head))
        
            # Update the head node 
            temp = self.head
            self.head = nextNode
            temp = None
        else:
            # Iterate over the entire XLLIST until we find the node with the given data
            prev = None
            current = self.head

            while current.data != data:
                temp = current
                current = current.getNextNode(prev)
                prev = temp

                if current == None:
                    raise ValueError("The given data couldn't be found in the XLLIST.")

            # Get the next node and reset its near nodes 
            nextNode = current.getNextNode(prev)
            if nextNode:
                nextNode.setNearNodes(prev, nextNode.getNextNode(current))
            
            # Reset the near nodes of the previous node and delete the current node
            prev.setNearNodes(prev.getPrevNode(current), nextNode)
            current = None

        # Decrement the length of the XLLIST
        self.length -= 1

    ######################### INSERTION / DELETION #########################

    ######################### OTHERS #########################

    def  

    ######################### OTHERS #########################

XLL = XORLinkedList()

for charCode in list(range(ord("A"), ord("A") + 5)):
    XLL.append(chr(charCode))

print("START XOR LINKED LIST -- > ")
print(XLL.getNodeData())

print("LENGTH : {0}".format(len(XLL)))

for i in range(3):
    print()



for i in range(3):
    print()

print("END XOR LINKED LIST -- > ")
print(XLL.getNodeData())

print("LENGTH : {0}".format(len(XLL)))
