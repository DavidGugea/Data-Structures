import random
import itertools  

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

def updateID(obj):
    if obj == None: return
    IDS[id(obj)] = obj

class QuickSort(object):
    def __init__(self, listToSort):
        self.quick_sort(listToSort, 0, len(listToSort) - 1)
    def medianOfThree(self, arr, low, high):
        if len(arr[low:high]) >= 3:
            # Create a list that contains the START, MIDDLE & END values of the list
            start_middle_end = [ arr[ low ], arr[ ( low + high ) // 2 ], arr[ high ] ]
            
            # Sort the list
            start_middle_end.sort()
                
            # Return the index of the middle element
            return arr.index(start_middle_end[1]) 
        else:
            return random.randint(low, high) 
    def partition(self, arr, low, high):
        # Get the pivot index using the median of three strategy
        pivotIndex = self.medianOfThree(arr, low, high) 

        # Get the pivot value using the pivot index
        pivot = arr[pivotIndex]

        # Swap the pivot with the last value from the list to 'get it from our way'
        arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]

        # Update the pivot index
        pivotIndex = high
        
        # Create two pointers that will scan the list
        LP = low      # Left pointer, swaps values that are bigger than the pivot ( > pivot )
        RP = high - 1 # Right pointer, swaps values that are smaller than the pivot ( < pivot )
             
        # Iterate over the list and swap the needed values while finding the place for the pivot
        while LP <= RP:
            if arr[LP] > pivot and arr[RP] < pivot:
                # Swap the left & right pointers
                arr[LP], arr[RP] = arr[RP], arr[LP]

                # Increment the left pointer
                LP += 1

                # Decrement the right pointer
                RP -= 1
            else:
                if arr[LP] < pivot:
                    # Increment the left pointer
                    LP += 1
                
                if arr[RP] > pivot:
                    # Decrement the right pointer
                    RP -= 1

        # Swap the pivot with the left pointer index value
        arr[LP], arr[pivotIndex] = arr[pivotIndex], arr[LP]
        
        # Update the pivot index
        pivotIndex = LP

        # Return the pivot index
        return pivotIndex
    def quick_sort(self, arr, low, high):
        if low < high:
            # Get the partition border index
            partitionIndex = self.partition(arr, low, high)

            # Quick sort both halves
            self.quick_sort(arr, low, partitionIndex - 1)
            self.quick_sort(arr, partitionIndex + 1, high)

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

        ~ Get length                                                                        (self.getLength )                                   -> number                       [x]
        ~ Create __len__(self) method                                                       ( len(self) )                                       -> number                       [x]

        ~ Node at index                                                                     ( self.atIndex(index) )                             -> node                         [x]
        ~ Get node data list                                                                ( self.getNodeData() )                              -> list                         [x]

        ~ Get last node                                                                     ( self.getLastNode() )                              -> Node                         [x]

        ######################### GENERAL METHODS #########################

        ######################### INSERTION / DELETION #########################

        ~ Append                                                                            ( self.append(data) )                               -> None                         [x]
        ~ Prepend                                                                           ( self.prepend(data) )                              -> None                         [x]
    
        ~ Insert after node                                                                 ( self.insertAfterNode(node, data) )                -> None                         [x]
        ~ Insert after node data                                                            ( self.insertAfterNodeData(key, data) )             -> None                         [x]
        ~ Insert at index                                                                   ( self.insertAtIndex(index, data) )                 -> None                         [x]

        ~ Delete node                                                                       ( self.deleteNode(node) )                           -> None                         [x]
        ~ Delete at index                                                                   ( self.deleteAtIndex(index) )                       -> None                         [x]
        ~ Delete node with data                                                             ( self.deleteNodeWithData(data) )                   -> None                         [x]
            
        ######################### INSERTION / DELETION #########################

        ######################### OTHERS #########################

        ~ Node Swap ( input : nodes to be swaped )                                          ( self.nodeSwap(node1, node2) )                     -> None                         [x]
        ~ Node Swap ( input : indexes of the nodes that need to be swapped )                ( self.nodeSwapAtIndexes(index1, index2) )          -> None                         [x]

        ~ Reverse                                                                           ( self.reverse() )                                  -> None                         [x]

        ~ Merge ( both sorted )                                                             ( self.mergeBothSorted(MERGE_XLLIST) )              -> None                         [x]
        ~ Merge ( both unsorted )                                                           ( self.mergeBothUnsorted(MERGE_XLLIST) )            -> None                         [x]
        ~ Sort  ( sort the main XLLIST )                                                    ( self.sort() )                                     -> None                         [x] 

        ~ Remove duplicates                                                                 ( self.removeDuplicates() )                         -> None                         [x]
        ~ Rotate                                                                            ( self.rotate(rotation_value) )                     -> None                         [x]
    
        ~ Is Palindrome                                                                     ( self.isPalindrome() )                             -> True / False                 [x]

        ~ Move tail to head                                                                 ( self.moveTailToHead() )                           -> None                         [x]
        ~ Sum with another XLLIST                                                           ( self.sumWithXLLIST(SUM_XLLIST) )                  -> None                         [x]

        ~ Split list in half                                                                ( self.splitInHalf() )                              -> [ XLLIST_1, XLLIST_2 ]       [x]
        ~ Split list after node                                                             ( self.splitAfterNode(node) )                       -> [ XLLIST_1, XLLIST_2 ]       [x]
        ~ Split list at index                                                               ( self.splitAtIndex(index) )                        -> [ XLLIST_1, XLLIST_2 ]       [x]
    
        ~ Pairs with sum                                                                    ( self.pairsWithSum(sum_value) )                    -> [ [], [], ... [] ]           [x]

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
        # If the node that we must insert a node after is the last node, then that means that we want to append. 
        if node == self.last:
            self.append(data)
            return

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
        
        # Update the last node in case current was 'last'
        if current == self.last:
            self.last = insertNode

        # Increment the length of the XLLIST
        self.length += 1

    def insertAtIndex(self, index, data):
        # Check the given index
        if not 0 <= index <= self.length:
            raise IndexError("The given index is either too big for the XOR Linked List or too small ( < 0 ).")

        if index == self.length:
            self.append(data)
            return

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
 
        # Try to update the last node
        if index == self.length - 1:
            self.last = insertNode 

        # Increment the length of the XLLIST
        self.length += 1

    def deleteNode(self, node):
        # Check the given node
        if type(node) != Node:
            raise ValueError("The given 'node' argument must be of type 'Node'")

        # Try to update last
        if node == self.last:
            self.last = self.last.getPrevNode(None)

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

        # Try to update the last node 
        if index == self.length - 1:
            self.last = self.last.getPrevNode(None)

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

            # Try to update the last node
            if self.getNodeData().count(data) == 1 and self.last == data:
                self.last = self.last.getPrevNode(None)

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

    def nodeSwap(self, node1, node2):
        # Swap the data of the nodes ( if the nodes are the same, don't swap anything )
        if ( node1 is node2 ) or ( node1.data is node2.data ) : return
        node1.data, node2.data = node2.data, node1.data

    def nodeSwapAtIndexes(self, index1, index2):
        # Check the given indexes
        if not 0 <= index1 < self.length and not 0 <= index2 < self.length:
            raise IndexError("The given indexes are either too big for the XOR Linked List or too small ( < 0 )")

        # Check if the indexes are both the same, if they are there is nothing to swap
        if index1 == index2:
            return

        # Get the nodes & swap the data
        node1 = None
        node2 = None

        prev = None
        current = self.head

        indexTrack = 0
    
        while indexTrack <= max([index1, index2]):
            if indexTrack == index1:
                node1 = current
            if indexTrack == index2:
                node2 = current 
    
            temp = current
            current = current.getNextNode(prev)
            prev = temp 

            indexTrack += 1

        # Swap the data
        node1.data, node2.data = node2.data, node1.data

    def reverse(self):
        # Reverse the 'pointers'
        prev = None
        current = self.head

        # Update the head node 
        self.last = self.head

        while current:
            temp = current
            nextNode = current.getNextNode(prev)

            if prev:
                prev.setNearNodes(current, prev.getPrevNode(current))
            current.setNearNodes(current.getNextNode(prev), prev)

            prev = temp
            current = nextNode
        
        self.head = prev 

    def mergeBothSorted(self, MERGE_XLLIST):
        # Check the MERGE_XLLIST
        if type(MERGE_XLLIST) != XORLinkedList:
            raise Exception("The MERGE_XLLIST must be of type 'XORLinkedList'")

        '''
        Example:
        self            =>      [1, 5, 7, 9, 10]
        MERGE_XLLIST    =>      [2, 3, 4, 6, 8]

        * AFTER MERGE * :

        self            =>      [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        '''
        
        # Keep track of the PREV_P, PREV_Q & PREV_PATH in order to iterate over the XLLISTS
        PREV_P = None
        PREV_Q = None
        PREV_PATH = None

        # Keep track of all the nodes in both XLLISTS
        P = self.head
        Q = MERGE_XLLIST.head
        
        # Create the new 'path' node. It will start with the lowest node head data from both XLLISTS 
        path = Node(min([self.head.data, MERGE_XLLIST.head.data]))

        # Set thea near nodes of the path do be by default None & None, just like a normal head node starts with no near nodes, no 'neighbours'
        path.setNearNodes(None, None)
        
        # Store the 'head' node in a variable and, after we create the path of nodes, we will set the new head node to be self.head 
        BEGIN_HEAD_NODE = path
        
        # Update one of the head nodes ( P or Q , because the 'path' node already took once place ( self.head or MERGE_XLLIST.head ) 
        if path.data == self.head.data:
            P = P.getNextNode(None)
            PREV_P = self.head
        else:
            Q = Q.getNextNode(None)
            PREV_Q = MERGE_XLLIST.head
        
        # Create the new path of nodes in a sorted way  
        while P and Q:
            # Keep track of the current path node  
            TEMP_PATH = path

            if path.data < P.data and P.data < Q.data:
                # Keep track of the current P node  
                TEMP_P = P

                # Create a new next node that has the data property of the P node and set the near nodes to be previous, path and next None 
                nextNode = Node(P.data)
                nextNode.setNearNodes(path, None)

                # Update the near nodes of the path node  
                path.setNearNodes(PREV_PATH, nextNode)
        
                # Update the P node  
                P = P.getNextNode(PREV_P)
                PREV_P = TEMP_P
            elif path.data < Q.data and Q.data < P.data:
                # Keep track of the current Q node 
                TEMP_Q = Q
                
                # Create a new next node that has teh data proeprty of the Q node and set the near nodes to be previous, path and next None
                nextNode = Node(Q.data)
                nextNode.setNearNodes(path, None)
            
                # Update the near nodes of the path node 
                path.setNearNodes(PREV_PATH, nextNode)

                # Update the q node 
                Q = Q.getNextNode(PREV_Q)
                PREV_Q = TEMP_Q  
            
            # Update the path node
            path = path.getNextNode(PREV_PATH)
            PREV_PATH = TEMP_PATH
   
        # Check for left-overs
        while P:            
            TEMP_P = P
            TEMP_PATH = path

            nextNode = Node(P.data)

            nextNode.setNearNodes(path, None)
            path.setNearNodes(PREV_PATH, nextNode)

            path = path.getNextNode(PREV_PATH)
            P = P.getNextNode(PREV_P)

            PREV_P = TEMP_P
            PREV_PATH = TEMP_PATH
        while Q:
            TEMP_Q = Q
            TEMP_PATH = path

            nextNode = Node(Q.data)

            nextNode.setNearNodes(path, None)
            path.setNearNodes(PREV_PATH, nextNode)

            path = path.getNextNode(PREV_PATH)
            Q = Q.getNextNode(PREV_Q)

            PREV_Q = TEMP_Q
            PREV_PATH = TEMP_PATH

        # Update the head node to be the first path node ( BEGIN_HEAD_NODE ) 
        self.head = BEGIN_HEAD_NODE 

        # Update the last node
        self.last = path

        # Update the length of the XLLIST
        self.length += len(MERGE_XLLIST)

    def mergeBothUnsorted(self, MERGE_XLLIST):
        # Check the MERGE_XLLIST
        if type(MERGE_XLLIST) != XORLinkedList:
            raise Exception("The MERGE_XLLIST must be of type 'XORLinkedList'")            

        # Get all the node data in the a list and sort the list
        allNodesData = self.getNodeData() + MERGE_XLLIST.getNodeData()

        # Sort the nodes data using the quick sort algorithm ( median of three strategy )  
        QS = QuickSort(allNodesData)

        # Create a new path node that will store all the new sorted nodes data
        path = Node(allNodesData[0])
        
        # By default set its' near nodes to be both None & None, as a normal default head node 
        path.setNearNodes(None, None)
    
        # Keep track of the previous path node too, in order to be able to move through the list, defaults to None
        PREV_PATH = None

        # Keep track of start head node. We will swap this node with the current head node ( * self.head * ) that we have now. 
        BEGIN_HEAD_NODE = path 

        for data in allNodesData[1:]:
            # Keep track of the current path, we will swap its value with the PREV_PATH node.
            TEMP_PATH = path
            
            # Create a new next node & set its near nodes
            nextNode = Node(data)
            nextNode.setNearNodes(path, None)

            # Reset the near nodes of the current path node
            path.setNearNodes(PREV_PATH, nextNode)

            # Update the path node
            path = path.getNextNode(PREV_PATH)

            # Update the PREV_PATH node to be the last path node
            PREV_PATH = TEMP_PATH

        # Update the head node
        self.head = BEGIN_HEAD_NODE

        # Update the last node
        self.last = path 

        # Update the length of the XLLIST
        self.length += len(MERGE_XLLIST)

    def sort(self):
        # Get all the node data and sort it using quick sort
        allNodesData = self.getNodeData()
        
        # Sort it using the quick sort algorithm ( median of three strategy )
        QS = QuickSort(allNodesData)

        # Create a new path node that will have it's data the first sorted element of the allNodesData 
        path = Node(allNodesData[0])

        # Set its near nodes to be both None & None as a default head node
        path.setNearNodes(None, None) 

        # Keep track of the previous node of the path in order to be able to go through the XLLIST ( defaults to None )
        PREV_PATH = None
        
        # Keep the default path node as a default future head node set in a variable. We will set the current head node that we have now to be this variable in the future after we build the node path 
        BEGIN_HEAD_NODE = path

        for data in allNodesData[1:]:
            # Store the current path node in a new variable in order to update the PREV_PATH ( prev node of the path node ) after we update the path node 
            TEMP_PATH = path 
        
            # Create the next node
            nextNode = Node(data)

            # Set up it's near nodes to be path & None
            nextNode.setNearNodes(path, None)

            # Reset the near nodes of the path node
            path.setNearNodes(PREV_PATH, nextNode)

            # Update the path node
            path = path.getNextNode(PREV_PATH)

            # Update the PREV_PATH node
            PREV_PATH = TEMP_PATH

        # Update the last node
        self.last = path 

        # Update the head node
        self.head = BEGIN_HEAD_NODE 
   
    def removeDuplicates(self):
        # Get all the node data from the XLLIST that doesn't repeat itself
        nodeData = list(set(self.getNodeData()))

        if len(nodeData) == self.length: return

        # Update the length of the XLLIST
        self.length = len(nodeData)

        # Rebuild the XLLIST with the new node data
        path = Node(nodeData[0])
        path.setNearNodes(None, None)

        PREV_PATH = None
        BEGIN_HEAD_NODE = path

        for data in nodeData[1:]:
            TEMP_PATH = path

            nextNode = Node(data)

            nextNode.setNearNodes(path, None)
            path.setNearNodes(PREV_PATH, nextNode)

            path = path.getNextNode(PREV_PATH)
            PREV_PATH = TEMP_PATH

        # Update the last node
        self.last = path

        # Update the head node
        self.head = BEGIN_HEAD_NODE

    def rotate(self, rotation_value):
        # Check the rotation value
        if not 0 <= rotation_value < self.length:
            raise ValueError("The given rotation value is either too big for the XOR Linked List or too small ( < 0 )") 

        # Get all the node data and rotate it, after that rebuilt the list using the given node data  
        nodeData = self.getNodeData()
        nodeData = nodeData[rotation_value:] + nodeData[:rotation_value]

        # Rebuild the XLLIST
        path = Node(nodeData[0])
        path.setNearNodes(None, None)

        BEGIN_PATH_NODE = path
        PREV_PATH = None

        for data in nodeData[1:]:
            TEMP_PATH = path

            nextNode = Node(data)

            nextNode.setNearNodes(path, None)
            path.setNearNodes(PREV_PATH, nextNode)

            path = path.getNextNode(PREV_PATH)
            PREV_PATH = TEMP_PATH
        
        # Update last node
        self.last = path
        
        # Update the head node
        self.head = BEGIN_PATH_NODE

    def isPalindrome(self):
        # Return True/False if the node-data string is the same upside down
        nodeDataString = "".join(map(str, self.getNodeData()))
        return nodeDataString == nodeDataString[::-1]

    def moveTailToHead(self):
        self.last.data, self.head.data = self.head.data, self.last.data 

    def sumWithXLLIST(self, SUM_XLLIST):
        return sum(self.getNodeData()) + sum(SUM_XLLIST.getNodeData())

    def splitInHalf(self):
        XLLIST_1 = XORLinkedList()
        XLLIST_2 = XORLinkedList()

        indexTrack = 0

        prev = None
        current = self.head

        while indexTrack < self.length:
            if indexTrack < self.length // 2:
                XLLIST_1.append(current.data)
            else:
                XLLIST_2.append(current.data)

            TEMP_CURRENT =  current
            current = current.getNextNode(prev)
            prev = TEMP_CURRENT

            indexTrack += 1

        return [ XLLIST_1, XLLIST_2 ]

    def splitAfterNode(self, node):
        # Check the node
        if type(node) == Node:
            raise Exception("The given node argument must be of type 'Node'")

        XLLIST_1 = XORLinkedList()
        XLLIST_2 = XORLinkedList()

        PTRN = False # PTRN = passed the required node 

        prev = None
        current = self.head
    
        while current:
            if not PTRN:
                XLLIST_1.append(current.data)
            else:
                XLLIST_2.append(current.data)
            
            if current == node:
                PTRN = True 
                
            TEMP_CURRENT = current
            current = current.getNextNode(prev) 
            prev = TEMP_CURRENT

        return [ XLLIST_1, XLLIST_2 ]

    def splitAtIndex(self, index):
        # Check the index
        if not 0 <= index < self.length:
            raise IndexError("The given index is either too big for the XOR Linked List or too small ( < 0 )")

        XLLIST_1 = XORLinkedList()
        XLLIST_2 = XORLinkedList()

        indexTrack = 0

        prev = None
        current = self.head

        while current:
            if indexTrack <= index:
                XLLIST_1.append(current.data)
            else:
                XLLIST_2.append(current.data)

            TEMP_CURRENT = current
            current = current.getNextNode(prev)
            prev = TEMP_CURRENT
        
            indexTrack += 1

        return [ XLLIST_1, XLLIST_2 ]

    def pairsWithSum(self, sum_value):
        pairs = list() 

        for pair in list(itertools.permutations(self.getNodeData(), 2)):
            if sum(pair) == sum_value and tuple(pair) not in pairs and tuple(pair[::-1]) not in pairs:
                pairs.append(tuple(pair))
    
        return pairs

    ######################### OTHERS #########################
