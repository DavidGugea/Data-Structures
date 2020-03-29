import random
import pprint
import sys # ~ sys.setrecursionlimit() to avoid RecursionError for quick sort ~ #

class quickSort(object):
    def medianOfThree(self, arr, low, high):
        if len(arr) >= 3:
            # Create a list with the beginning, the middle and the end element from the list
            start_middle_end = [ arr[ low ], arr[ ( low + high ) // 2 ], arr[ high ] ]
            
            # Sort the list
            start_middle_end.sort()

            # Return the index of the middle sorted element ( median of three )
            return arr.index(start_middle_end[1])
        else:
            return random.randint(low, high)
    def partition(self, arr, low, high):
        # Get the pivot and pivot index
        pivotIndex = self.medianOfThree(arr, low, high) 
        pivot = arr[pivotIndex]
        
        # Swap the pivot with the last element from the array to get it from our way
        arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]
        
        # Update the pivot index
        pivotIndex = high

        # Create two pointers
        LP = low # LP ( left pointer ) < = > Swaps all elements that are bigger than the pivot so that we can have all elements smaller than the pivot on the left side
        RP = high - 1 # RP ( right pointer ) < = > Swaps all the elements that are smaller than the pivot so that we can have all elements bigger than the pivot in the right side

        while LP <= RP:
            if arr[LP] > pivot and arr[RP] < pivot:
                # Swap [ LP ] with [ RP ]
                arr[LP], arr[RP] = arr[RP], arr[LP]

                # Increment left pointer | Decrement right pointer 
                LP += 1
                RP -= 1
            else:
                if arr[LP] < pivot:
                    # Increment left pointer because LP searches for elements that are bigger than the pivot
                    LP += 1
                if arr[RP] > pivot:
                    # Decrement right pointer because RP searches for elements that are smaller than the pivot
                    RP -= 1
            
        # Swap [ LP ] with [ pivotIndex ]
        arr[LP], arr[pivotIndex] = arr[pivotIndex], arr[LP]

        # Return border split index
        return LP
    def quickSort(self, arr, low, high):
        if low <= high:
            # Split the list into two lists and find a place for a pivot
            partitionBorderSplitIndex = self.partition(arr, low, high)

            # Sort both halves
            self.quickSort(arr, partitionBorderSplitIndex + 1, high)
            self.quickSort(arr, low, partitionBorderSplitIndex - 1)
    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList(object):
    def __init__(self):
        # Length of the llist
        self.length = 0

        # Head of the llist 
        self.head = None

    ''' GENERAL METHODS '''

    def getLength(self):
        ''' Return the length of the linked list '''

        return self.length

    def getNodeDataList(self):
        '''
            Return a list with all the data of each node in the llist
        '''

        nodeDataList = list()
        current = self.head

        while current:
            nodeDataList.append(current.data)
            current = current.next

        return nodeDataList

    def indexOf(self, node):
        ''' 
            Return the index of the given node by keeping track of the index of each node
        '''
        
        if not node:
            raise ValueError("The passed in node must be valid and in the linked list.")

        index = 0
        current = self.head

        while current:
            if current == node:
                return index
            
            current = current.next
            index += 1

        if not current:
            raise ValueError("The passed in node wasn't found in the linked list.")
    def indexOf_FirstData(self, data):
        '''
            Return the index of the first node that has the passed in data by keeping track of the index and data of each node
        '''

        index = 0
        current = self.head

        while current:
            if current.data == data:
                return index
            
            current = current.next
            index += 1

        if not current:
            raise ValueError("The passed in data couldn't be found in any node in the linked list.")
    def nodeAtIndex(self, index):
        ''' Return the node at the given index '''

        if index >= self.length:
            raise IndexError("The index passed is is bigger or equal than the length of the linked list. | Index : {0} / Length : {1} |".format(index, self.length))

        indexTrack = 0
        current = self.head 
        while indexTrack <= index - 1:
            current = current.next
            indexTrack += 1

        return current

    ''' GENERAL METHODS '''

    ''' APPEND & EXTEND '''

    def append(self, data):
        ''' Get the last node of the llist and set it's next element to a new node with the data provided '''

        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next 

            current.next = Node(data)

        # Increment length
        self.length += 1

    def extend(self, llist):
        ''' Append each node from the passed in llist '''

        current = llist.head
        while current:
            self.append(current.data)
            current = current.next

        # Increment the length of the main llist ( self ) with the length of the llist
        self.length += llist.length

    ''' APPEND & EXTEND ''' 

    ''' INSERT AT NODE & / INDEX '''

    def insertAtNode(self, node, data):
        ''' Insert a new node at the index of the given node '''

        if not node:
            raise ValueError("The node provided must be valid.")

        # Keep track of the current and previous node till we reach the given node 
        current = self.head
        while current:
            if current == node:
                break

            prev = current
            current = current.next

        if not current:
            raise ValueError("The given node couldn't be found in the linked list.")

        # Create a new node
        insertNode = Node(data)

        prev.next = insertNode
        insertNode.next = current

        # Increment length
        self.length += 1

    def insertAtIndex(self, index, data):
        ''' Insert a new node with the passed in data at the passed in index '''

        if index > self.length:
            raise IndexError("The index provided is bigger than the length of the linked list. | Index : {0} /\ Length : {1} |".format(index, self.length))
        elif index == self.length:
            self.append(data)
        else:
            # Get the node at the specific index
            prev = None
            current = self.head
            indexTrack = 0

            while indexTrack < index:
                prev = current
                current = current.next
                indexTrack += 1

            insertNode = Node(data)
            prev.next = insertNode
            insertNode.next = current

        # Increment length
        self.length += 1

    ''' INSERT AT NODE & / INDEX '''

    ''' DELETE AT NODE & / INDEX '''

    def deleteNode(self, node):
        ''' Delete the given node '''

        if not node:
            raise ValueError("The node provided must be valid")
        if node == self.head:
            self.head = self.head.next
        else:
            # Keep track of the previous and current node in the llist
            prev = None
            current = self.head

            while current != node:
                prev = current
                current = current.next
        
            if not current:
                raise ValueError("The given node must be in the linked list.")

            temp = current.next
            prev.next = temp
            current = None

        # Decrement length
        self.length -= 1

    def deleteAtIndex(self, index):
        ''' Delete the node at the given index '''

        if index >= self.length:
            raise IndexError("The index provided was equal or bigger than the length of the array. | Index : {0} < - > Length : {1} |".format(index, self.length))
        if index == 0:
            self.head = self.head.next
        else:
            # Keep track of the previous, index and current node in the llist
            prev = None
            current = self.head
            indexTrack = 0

            while indexTrack < index:
                prev = current
                current = current.next
    
                indexTrack += 1

            temp = current.next
            prev.next = temp
            current = None
                
        # Decrement length
        self.length -= 1

    ''' DELETE AT NODE & / INDEX '''

    ''' SWAP NODES '''
    
    def swapNodes(self, node0, node1):
        ''' Swap nodes node0 and node1 '''

        if not node0 or not node1:
            raise ValueError("The nodes provided must be valid")
        if node0 == node1 or node0.data == node1.data:
            return

        # Get the previous nodes for each node
        prevNode0 = None
        prevNode1 = None

        prev = None
        current = self.head

        while current:
            if current == node0:
                prevNode0 = prev
            if current == node1:
                prevNode1 = prev

            prev = current
            current = current.next

        if node0 == self.head:
            prevNode1.next = self.head
            self.head = node1
        elif node1 == self.head:
            prevNode0.next = self.head
            self.head = node0
        if node0 != self.head and node1 != self.head:
            prevNode0.next, prevNode1.next = prevNode1.next, prevNode0.next
        
        node0.next, node1.next = node1.next, node0.next 

    def swapNodes_AtIndex(self, index0, index1):
        ''' Swap the nodes at the given indexes '''

        if index0 >= self.length or index1 >= self.length:
            raise IndexError("The indexes given are bigger or equal to the length of the linked list. | First index : {0} / Second index : {1} / Length of the linked list : {2}".format(
                    index0, index1,
                    self.length
            ))

        # Get the nodes and their previous nodes and the given indexes
        prevNode0 = None
        node0 = None

        prevNode1 = None
        node1 = None

        prev = None
        current = self.head
        indexTrack = 0

        while indexTrack <= max([index0, index1]):
            if indexTrack == index0:
                prevNode0 = prev
                node0 = current
            elif indexTrack == index1:
                prevNode1 = prev
                node1 = current

            prev = current
            current = current.next
            indexTrack += 1

        if node0 == self.head:
            prevNode1.next = self.head
            self.head = node1 
        elif node1 == self.head:
            prevNode0.next = self.head
            self.head = node0
        else:
            prevNode0.next, prevNode1.next = prevNode1.next, prevNode0.next
        
        node0.next, node1.next = node1.next, node0.next

    ''' SWAP NODES '''

    ''' REVERSE '''

    def reverse(self):
        ''' Reverse the linked list '''

        # ( None ) A -> B -> C -> D -> E -> None
        # REVERSE (change arrow direction)
        # None <- A <- B <- C <- D <- E ( None )

        # For each node in the llist change the direction of the node to its previous node
        prev = None
        current = self.head

        while current:
            temp = current.next
            current.next = prev

            prev = current
            current = temp

        self.head = prev

    ''' REVERSE '''

    ''' MERGE '''

    def merge_BothSorted(self, llist):
        ''' Merge the main llist ( self ) that is sorted with another linked list ( llist ) that is also sorted 
        
        ##############################################
        # self  => [ 1, 5, 7, 9, 10 ]               ##
        # llist => [ 2, 3, 4, 6,  8 ]               ##
        # AFTER MERGE:                              ##
        # self => [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] ##
        ##############################################

        '''

        # Create three pointers ( P for the main llist, Q for the passed in arg llist and "trail" for the new chain of nodes)
        P = self.head
        Q = llist.head

        trail = None
        if P.data <= Q.data:
            # Change the beginning of the trail to the beginning of the llist
            trail = P
            
            # Update pointer
            P = P.next
        elif Q.data <= P.data:
            # Change the beginning of the trail to the beginning of the arg llist
            trail = Q

            # Update pointer
            Q = Q.next

        while P and Q:
            if P.data <= Q.data:
                # Set a new node to the trail
                trail.next = Node(P.data)
                
                # Update pointer
                P = P.next
            elif Q.data <= P.data:
                # Set a new node to the trail
                trail.next = Node(Q.data)

                # Update pointer
                Q = Q.next
    
            # Update trail
            trail = trail.next

        # Add leftovers
        while P:
            # Set a new node to the trail
            trail.next = Node(P.data)

            # Update trail and pointer
            trail = trail.next
            P = P.next
        while Q:
            # Set a new node to the trail 
            trail.next = Node(Q.data)

            # Update trail and pointer
            trail = trail.next
            Q = Q.next

    def merge(self, llist):
        ''' Merge the main llist ( self ) that is an unsorted llist with the passed in arg llist ( llist ) that is also an unsorted array

        #############################################################################################
        # ~ 1 : Take all the node data from both llist in a list                                 ~ ##
        # ~ 2 : Sort the node data list using quick sort ( the median of three strategy )        ~ ##
        # ~ 3 : Reset the main llist using all the sorted node data in the sorted node data list ~ ##
        #############################################################################################
        
        ##############################################
        # self  => [  5, 4, 3, 2, 1 ]               ##
        # llist => [ 10, 9, 8, 7, 6 ]               ##
        # AFTER MERGE :                             ##
        # self  => [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ##
        ##############################################  

        '''

        # ~ 1 : ~ #
        nodeDataList = list()

        current = self.head
        while current:
            nodeDataList.append(current.data)
            current = current.next 

        current = llist.head
        while current:
            nodeDataList.append(current.data)
            current = current.next

        # ~ 2 : ~ #
        quickSort_alg = quickSort()
        quickSort_alg.sort(nodeDataList)

        # ~ 3 : ~ #
        self.head = Node(nodeDataList[0])
        current = self.head 
        for nodeData in nodeDataList[1:]:
            current.next = Node(nodeData)
            current = current.next
 
    ''' MERGE '''

    ''' REMOVE DUPLICATES '''

    def removeDuplicates(self):
        ''' Remove all the duplicates from the llist by keeping track of all the node data in a list '''

        nodeDataList = [ self.head.data ]

        # Create a new "chain of nodes" for the main list ( self ) | In the nodeDataList the data of the head node is already in the list because we start with the head 
        chain = self.head
        current = self.head.next

        while current:
            if current.data not in nodeDataList:
                # Append the new node data in the list 
                nodeDataList.append(current.data)
                    
                # Create a new next node for the chain node
                chain.next = Node(current.data)
            
                # Update the current node
                current = current.next

                # Update the chain node
                chain = chain.next
            else:
                # Update the current node
                current = current.next

    ''' REMOVE DUPLICATES '''

    ''' COUNT OCCURRENCES ''' 

    def countOccurrences(self, data):
        ''' Count how many nodes in the linked list have the passed in data '''

        counter = 0
        current = self.head

        while current:
            if current.data == data:
                counter += 1 
            current = current.next

        return counter

    ''' COUNT OCCURRENCES '''

    ''' ROTATE '''

    def rotate(self, rotationValue):
        ''' Rotate the llist by the rotation value ( Example : https://www.geeksforgeeks.org/rotate-a-linked-list/ ) 

        ################################################
        # self          => [ 10, 20, 30, 40, 50, 60 ] ##
        # rotationValue => 4                          ##
        # AFTER ROTATION :                            ##
        # self          => [ 50, 60, 10, 20, 30, 40 ] ##
        ################################################
    
        '''

        # Get the first node after the rotation value ( index ), the last node and the node before the first node after the rotation value
        lastNode_Before_RotationValue = None
        firstNode_After_RotationValue = None
        lastNode = None

        index = 0
        current = self.head

        while current:
            if index == self.length - 1:
                lastNode = current
            if index == rotationValue - 1:
                lastNode_Before_RotationValue = current
            if index == rotationValue:
                firstNode_After_RotationValue = current

            current = current.next
            index += 1

        # Set the next node of the last node to the head and set the first node after the rotation value ( index ) as the new head of the llist and set the next node of the last node before the rotation value to none
        lastNode.next = self.head
        self.head = firstNode_After_RotationValue
        lastNode_Before_RotationValue.next = None 

    ''' ROTATE '''

    ''' IS PALINDROME '''
    def isPalindrome(self):
        ''' Return true if the node data is a palindrome, otherwise false '''

        # Create a string with all data from all the nodes and see if the string is the same upside down ( palindrome if true, otherwise false )
        nodeData = str()

        current = self.head
        while current:
            nodeData += str(current.data)
            current = current.next

        return nodeData == nodeData[::-1] 

    ''' IS PALINDROME '''

    ''' MOVE TAIL TO HEAD '''

    def moveTailToHead(self):
        ''' Move tail to head, so the last node of the llist will be the new head 

        ######################################
        # self => A -> B -> C -> D -> None  ##
        # Move tail to head                 ##
        # self => D -> A -> B -> C -> None  ##
        ######################################
        
        '''

        # Get the last and the node before the last node of the llist
        prevNode = None
        lastNode = self.head 

        while lastNode.next:
            prevNode = lastNode 
            lastNode = lastNode.next

        # Set the next node of the last node to the head of the llist and set the next node of the node before the last node to None, after that update self.head
        lastNode.next = self.head
        prevNode.next = None

        self.head = lastNode

    ''' MOVE TAIL TO HEAD '''

    ''' SUM WITH LLIST '''

    def sumWith(self, llist):
        ''' Sum all the elements from the main list ( self ) with all the elements from the passed in llist ( llist ) '''
        nodeSum = 0

        current = self.head
        while current:
            try:
                nodeSum += float(current.data)
            except Exception:
                pass

            current = current.next

        current = llist.head
        while current:
            try:
                nodeSum += float(current.data)
            except Exception:
                pass

            current = current.next

        return nodeSum

    ''' SUM WITH LLIST '''

llist = LinkedList()
for i in [1, 2]: 
    llist.append(i)

llist_2 = LinkedList()
for i in [3]: 
    llist_2.append(i)

print("LINKED LIST BEFORE : ")
pprint.pprint(llist.getNodeDataList(), indent = 20)

for i in range(5):
    print()

########################################################################

print(llist.sumWith(llist_2))

########################################################################

for i in range(5):
    print()

print("LINKED LIST AFTER : ")
pprint.pprint(llist.getNodeDataList(), indent = 20)
