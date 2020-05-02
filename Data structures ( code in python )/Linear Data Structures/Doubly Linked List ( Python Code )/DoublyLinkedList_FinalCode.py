import pprint
import random
import itertools

class Node(object):
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None

class QuickSort(object):
    def medianOfThree(self, arr, low, high):
        if len(arr) >= 3:
            # Get the first, middle & last item
            start_middle_last = [ arr[low], arr[ ( low + high ) // 2 ], arr[high] ]

            # Sort it
            start_middle_last.sort()

            # Return the index of the middle item
            return arr.index(start_middle_last[1])
        else:
            return random.randint(low, high)
    def partition(self, arr, low, high):
        # Get the pivot index
        pivotIndex = self.medianOfThree(arr, low, high)
        pivot = arr[pivotIndex]

        # Swap the pivot index with the last element from the list to 'get it from our way'
        arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]

        # Update the pivot index
        pivotIndex = high

        # Create two pointers that will scan the list from both sides
        LP = low        # left pointer  ( swap when arr[LP] > pivot ) 
        RP = high - 1   # right pointer ( swap when arr[RP] < pivot )

        while LP <= RP:
            if arr[LP] > pivot and arr[RP] < pivot:
                # Swap [LP] & [RP] 
                arr[LP], arr[RP] = arr[RP], arr[LP]
    
                # Increment left pointer value
                LP += 1
                # Decrement right pointer value
                RP -= 1
            elif arr[LP] < pivot:
                # Increment left pointer value
                LP += 1
            elif arr[RP] > pivot:
                # Decrement right pointer value
                RP -= 1


        # Swap the pivot with the [LP] value, because we found the place for the pivot
        arr[LP], arr[pivotIndex] = arr[pivotIndex], arr[LP]

        # Update the pivot index
        pivotIndex = LP

        # Return the 'border' split value
        return pivotIndex
    def quickSort(self, arr, low, high):
        if low <= high:
            partitionBorderIndex = self.partition(arr, low, high)

            self.quickSort(arr, low, partitionBorderIndex - 1)
            self.quickSort(arr, partitionBorderIndex + 1, high)
    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)

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

<<<<<<< HEAD
        ~ Node Swap ( input : nodes to be swaped )                                      ( self.nodeSwap(node1, nod2) )                               -> None                     [x]
        ~ Node Swap ( input : indexes of the node that need to be swaped )              ( self.nodeSwapAtIndexes(index1, index2) )                  -> None                     [x]
=======
        ~ Node Swap ( input : nodes to be swaped )                                      ( self.nodeSwap(node1, nod2) )                                      -> None                     [x]
        ~ Node Swap ( input : indexes of the node that need to be swaped )              ( self.nodeSwapAtIndexes(index1, index2) )                          -> None                     [x]
>>>>>>> DoublyLinkedList_PythonCode

        ~ Reverse                                                                       ( self.reverse() )                                                  -> None                     [x]

        ~ Merge ( both sorted )                                                         ( self.mergeBothSorted(dllist_merge) )                              -> None                     [x]
        ~ Merge ( both unsorted )                                                       ( self.mergeBothUnsorted(dllist_merge) )                            -> None                     [x]

        ~ Remove duplicates                                                             ( self.removeDuplicates() )                                         -> None                     [x]
        ~ Rotate                                                                        ( self.rotate(rotationValue) )                                      -> None                     [x]

        ~ Is palindrome                                                                 ( self.isPalindrome() )                                             -> True / False             [x]

        ~ Move tail to head                                                             ( self.moveTailToHead() )                                           -> None                     [x]
        ~ Sum with another dllist                                                       ( self.sumWithDLLIST(sum_dllist) )                                  -> number                   [x]

        ~ Split list in half                                                            ( self.splitInHalf() )                                              -> [ dllist1, dllist2 ]     [x]
        ~ Split list after node                                                         ( self.splitAfterNode(node) )                                       -> [ dllist1, dllist2 ]     [x]
        ~ Split list at index                                                           ( self.splitAtIndex(index) )                                        -> [ dllist1, dllist2 ]     [x] 

        ~ Pairs with sum                                                                ( self.pairsWithSum(sum_value) )                                    -> [ (), () .. () ]         [x]

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

        # Create the insert node & modify the .next & .prev values for the current & next node
        insertNode = Node(data)

        nxt = node.next

        insertNode.prev = node
        insertNode.next = nxt

        if nxt:
            nxt.prev = insertNode

        node.next = insertNode

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
           
        if node != self.head and node.next: 
           prev = node.prev
           nxt  = node.next

           prev.next = nxt
           nxt.prev = prev 
        elif node == self.head:
            nxt = node.next

            nxt.prev = None
            self.head = nxt
        elif node != self.head and not node.next:
            prev = node.prev
            prev.next = None

        node = None
        
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

    def nodeSwap(self, node1, node2):
        # Check the nodes
        if not node1 or not node2:
            raise ValueError("The given nodes are not valid.")

        if node1 == node2:
            return

        # Swap only the data
        node1.data, node2.data = node2.data, node1.data

    def nodeSwapAtIndexes(self, index1, index2):
        # Check the indexes
        if not 0 <= index1 < self.length and not 0 <= index2 < self.length:
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

    def reverse(self):
        # Reverse the direction of the arrows ( .next & .prev ) for each node while iterating over all nodes
        prev = None
        current = self.head
        while current:
            nxtNode = current.next
            current.prev, current.next = current.next, current.prev

            prev = current
            current = nxtNode

        self.head = prev

    def mergeBothSorted(self, dllist_merge):
        # Check the dllist_merge argument
        if type(dllist_merge) != DoublyLinkedList:
            raise ValueError("The passed in dllist_merge argument must be a DoublyLinkedList class.")
            
        ###############################################
        # EXAMPLE :                                  ##
        # dllist_1 => [1, 5, 7, 9, 10]               ##
        # dllist_2 => [2, 3, 4, 6, 8 ]               ##
        # After merge:                               ##
        # dllist_1 => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]##
        ###############################################

        # Create the pointers
        mp = None               # main pointer
        up = self.head          # up pointer   ( the pointer that iterates over the main dllist ( self ) )
        dp = dllist_merge.head  # down pointer ( the pointer that iterates over the dllist_merge         ) 

        # Find the place for the main pointer
        if up.data <= dp.data:
            mp = self.head
            up = up.next
        elif up.data > dp.data:
            mp = dllist_merge.head
            dp = dp.next
    
        firstNode = mp

        while up and dp:
            if mp.data < dp.data and dp.data < up.data:
                # Create a new node with the same data as the dp node
                newNode = Node(dp.data)
    
                # update the pointer
                dp = dp.next

                # Change the previous pointer to the node to point to the main node that we are at now
                newNode.prev = mp
                
                # Make the main pointer .next value the new node that we create
                mp.next = newNode
            elif mp.data < up.data and up.data < dp.data:
                # Same as above
                newNode = Node(up.data)

                up = up.next

                newNode.prev = mp 
                mp.next = newNode

            # Change the main pointer location
            mp = mp.next
            
        # Change the head node of the dllist
        self.head = firstNode

        # Add leftovers
        while up:
            newNode = Node(up.data)

            newNode.prev = mp
            mp.next = newNode

            up = up.next
            mp = mp.next

        while dp:
            newNode = Node(dp.data)

            newNode.prev = mp
            mp.next = newNode

            dp = dp.next
            mp = mp.next
    
    def mergeBothUnsorted(self, dllist_merge):
        # Steps:
        # ~ 1. Get the node data from both lists in a bigger list
        # ~ 2. Sort the node data list using quick sort ( median of three strategy )
        # ~ 3. Rebuild dllist

        # ~ 1.
        nodeDataList = self.getNodeData() + dllist_merge.getNodeData() 

        # ~ 2.
        quickSort_alg = QuickSort()
        quickSort_alg.sort(nodeDataList)

        # ~ 3.
        current = Node(nodeDataList[0])
        self.head = current

        for nodeData in nodeDataList[1:]:
            newNode = Node(nodeData)

            newNode.prev = current
            current.next = newNode

            current = current.next
    
    def removeDuplicates(self):
        # Keep track of the used node data
        usedNodeData = [self.head.data]

        # Create two pointers
        mp = self.head       # main pointer ( the one that rebuilds the node structure )
        sp = self.head.next  # scan pointer ( the one that iterates over all the nodes in the list checking for their data )
            
        while sp:
            # Check if the scan pointer data has already been used
            if sp.data not in usedNodeData:
                # Create a new node with the data
                newNode = Node(sp.data)

                # Set the .prev for the new node & the .next for the main pointer 
                newNode.prev = mp
                mp.next = newNode
            
                # Update the main pointer
                mp = mp.next

                # Add the used node data to the list so that we will know next time that this data has already been used
                usedNodeData.append(sp.data)
            
            sp = sp.next
    
    def rotate(self, rotationValue):
        # Check the rotation value
        if rotationValue > self.length:
            raise ValueError("The given rotation value if bigger than the length of the dllist. Try again with a smaller value. ( <= self.length ).")

        beforeRotationValue = None
        mainRotationNode = None
        lastNode = None

        prev = None
        current = self.head
        counter = 0

        while current: 
            if counter == rotationValue:
                mainRotationNode = current
                beforeRotationValue = current.prev 


            counter += 1

            prev = current
            current = current.next
            
    
        lastNode = prev

        beforeRotationValue.next = None
        lastNode.next = self.head
        self.head.prev = lastNode

        mainRotationNode.prev = None
        self.head = mainRotationNode

    def isPalindrome(self):
        # Get all the node data in a string and see if the string upsidedown is the same as the normal node data string
        nodeString = str()
        
        current = self.head
        
        while current:
            nodeString += str(current.data)

            current = current.next

        return nodeString == nodeString[::-1]

    def moveTailToHead(self):
        # Swap the last node with the head node by iterating over the entire dllist till you get the last node and modify the values for the previous, last & head node
        
        current = self.head
        while current.next:
            current = current.next
        
        # Get the previous node of the last node and modify it so, that it will be the last node ( no .next < = > .next = None)  
        prev = current.prev
        prev.next = None

        # Modify the values of the last node so that it will be like the 'head' node ( .prev is None & .next is the current .head that we have now ) 
        current.next = self.head
        self.head.prev = current
        current.prev = None

        # Update the head node to be the last node
        self.head = current
        
    def sumWithDLLIST(self, sum_dllist):
        # Create the sum & set it to 0 by default.
        sum_ = 0

        # Create two pointers for both dllists
        p = self.head       # pointer for our dllist, for the main dllist ( self       )
        q = sum_dllist.head # pointer for the dllist argument, sum_dllist ( sum_dllist )

        # Iterate over both lists and check if the values are numbers, if that is the case, add them to the sum_ value
        while p or q:
            if p:
                if type(p.data) == int or type(p.data) == float:
                    sum_ += eval(str(p.data))
                
                p = p.next
    
            if q:
                if type(q.data) == int or type(q.data) == float:
                    sum_ += eval(str(q.data))

                q = q.next

        return sum_
    
    def splitInHalf(self):
        # Create two new dllists and add all the node data in the first one till it hits the half of our list, after that add all the node that in the second dllist
        dllist_1 = DoublyLinkedList()
        dllist_2 = DoublyLinkedList()

        # Create the border ( represents the half of the dllist ) 
        border = self.length // 2

        # Keep track of the index & of the current node
        indexTrack = 0
        current = self.head

        while current:
            if indexTrack < border:
                dllist_1.append(current.data)
            elif indexTrack >= border:
                dllist_2.append(current.data)

            current = current.next
            indexTrack += 1

        return [ dllist_1, dllist_2 ]
    
    def splitAfterNode(self, node):
        # Check the node
        if type(node) != Node or not node:
            raise ValueError("The given node must have a 'Node' type and it can't be None.")

        # Create two dllists and keep track of the current node, while the current node didn't hit the node given as an argument, add it to the first dllist, otherwise add it to the second dllist
        dllist_1 = DoublyLinkedList()
        dllist_2 = DoublyLinkedList()

        current = self.head
        hitNode = False

        while current:
            if not hitNode:
                dllist_1.append(current.data)
            if hitNode:
                dllist_2.append(current.data)

            if current == node:
                hitNode = True

            current = current.next

        return [ dllist_1, dllist_2 ]
    
    def splitAtIndex(self, index):
        # Check the index
        if index >= self.length or index < 0:
            raise IndexError("The given index is either too big for the dllist or it is too small ( < 0 ).")

        # Create two dllists and keep track of the index & of the current node
        dllist_1 = DoublyLinkedList()
        dllist_2 = DoublyLinkedList()

        current = self.head
        indexTrack = 0

        while current:
            if indexTrack < index:
                dllist_1.append(current.data)
            if indexTrack >= index:
                dllist_2.append(current.data)

            current = current.next
            indexTrack += 1 

        return [ dllist_1, dllist_2 ]

    def pairsWithSum(self, sum_value):
        sums_ = list()
        for permutation in list(itertools.permutations(self.getNodeData(), 2)):
            if sum(list(permutation)) == sum_value and tuple(permutation) not in sums_ and tuple(list(permutation)[::-1]) not in sums_:
                sums_.append(tuple(permutation))

        return sums_

    ############################### OTHERS ###############################
