import random
import pprint
import sys # ~ sys.setrecursionlimit() to avoid RecursionError for quick sort ~ #

class quickSort(object):
    def partition(self, arr, low, high):
        # Get the pivot and pivot index
        pivotIndex = random.randint(low, high)
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
                ar[LP], arr[RP] = arr[RP], arr[LP]

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

    def deleteAtNode(self, node):
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

        # self  => [ 1, 5, 7, 9, 10 ] 
        # llist => [ 2, 3, 4, 6,  8 ]
        # AFTER MERGE: 
        # self => [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

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

        ############################################################################################
        # ~ 1 : Take all the node data from both llist in a list                                 ~ #
        # ~ 2 : Sort the node data list using quick sort ( the median of three strategy )        ~ #
        # ~ 3 : Reset the main llist using all the sorted node data in the sorted node data list ~ #
        ############################################################################################

        # self  => [  5, 4, 3, 2, 1 ]
        # llist => [ 10, 9, 8, 7, 6 ]
        # AFTER MERGE :
        # self  => [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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
        pass

    ''' MERGE '''

llist = LinkedList()
for i in [1, 5, 7, 9, 10]:
    llist.append(i)

llist_2 = LinkedList()
for i in [2, 3, 4, 6, 8]:
    llist_2.append(i)

print("LINKED LIST BEFORE : ")
pprint.pprint(llist.getNodeDataList(), indent = 20)

for i in range(5):
    print()

########################################################################

llist.merge_BothSorted(llist_2)

########################################################################

for i in range(5):
    print()

print("LINKED LIST AFTER : ")
pprint.pprint(llist.getNodeDataList(), indent = 20)
