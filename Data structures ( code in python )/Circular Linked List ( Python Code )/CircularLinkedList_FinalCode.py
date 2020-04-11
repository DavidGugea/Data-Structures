# Create the node object, it will have a pointer to the next node (self.next) & a data value (self.data)
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        # Create the head node of the list when you make a new instance of the circular linked list class & set it to none
        self.head = None
        
        # Besides the head node, keep track of the length of the circular linked list too. Set it by default to 0
        self.length = 0

        '''
        ( ~ Description ( how the method looks ) -> return value [done ( x ) / undone ( empty ) ] )

        Methods :
    
            ############## GENERAL METHODS ##############
            
            ~ Get length                   ( self.getLength )      -> number    [x]
            ~ Create __len__(self) method  ( len(self) )           -> number    [x]
            
            ~ Node at index                ( self.atIndex(index) ) -> number    [x]
            ~ Get node data list           ( self.getNodeData()  ) -> list      [x]

            ~ Get last node                ( self.getLastNode()  ) -> Node      [x]
    
            ############## GENERAL METHODS ##############

            ############## INSERTION / DELETION ##############
            
            ~ Append ( self.append(data) )                             -> None     [x]
            ~ Prepend ( self.prepend(data) )                           -> None     [x]

            ~ Insert after node ( self.insertAfterNode(node, data) )   -> None     [x]
            ~ Insert at index   ( self.insertAtIndex(index, data)  )   -> None     [x]

            ~ Delete node       ( self.deleteNode(node) )              -> None     [x]
            ~ Delete at index   ( self.deleteAtIndex(index)  )         -> None     [x]

            ############## INSERTION / DELETION ##############

            ############## OTHERS ##############
            
            ~ Node swap ( input : nodes to be swaped   )   ( self.swapNodes(node1, node2) )             -> None                    [x]
            ~ Node swap ( input : indexes of the nodes )   ( self.swapNodesAtIndexes(index1, index2) )  -> None                    [x]

            ~ Reverse                                      ( self.reverse() )                           -> None                    []

            ~ Merge ( both sorted )                        ( self.mergeBothSorted(cllist) )             -> None                    []
            ~ Merge ( both unsorted )                      ( self.mergeBothUnsorted(cllist) )           -> None                    []

            ~ Remove duplicates                            ( self.removeDuplicates() )                  -> None                    []

            ~ Rotate                                       ( self.rotate() )                            -> None                    []

            ~ Is palindrome                                ( self.isPalindrome() )                      -> True / False            []
            ~ Move tail to head                            ( self.moveTailToHead() )                    -> None                    []

            ~ Sum with another circular linked list        ( self.sumWithCLLIST(cllist) )               -> number                  []

            ~ Split list in half                           ( self.splitInHalf() )                       -> [ cllist1, cllist2 ]    []
            ~ Split list after node                        ( self.splitAfterNode(node) )                -> [ cllist1, cllist2 ]    []
            ~ Split list at index                          ( self.splitAtIndex(index) )                 -> [ cllist1, cllist2 ]    []

            ~ Josephus problem                             ( self.josephusProblem(step) )               -> None                    []
            ~ Is Circular Linked List                      ( self.isCircularLinkedList() )              -> True / False            []

            ############## OTHERS ##############
         
        '''
    
    ############## GENERAL METHODS ##############

    def getLength(self):
        return self.length
    def __len__(self):
        return self.length

    def atIndex(self, index):
        # Check if the index is bigger or equal than the circular linked list, if that is the case, raise an IndexError
        if index >= self.length:
            raise IndexError("The given index is too big for the cllist.")

        # If index is 0 , return the head
        if index == 0:
            return self.head

        # Otherwise, iterate till you hit the index by keeping track of the index & the current node
        indexTrack = 0
        current = self.head

        while indexTrack <= index:
            current = current.next
            indexTrack += 1

        return current

    def getNodeData(self):
        nodeDataList = [self.head.data]
        current = self.head.next

        while current is not self.head:
            nodeDataList.append(current.data)
            current = current.next

        return nodeDataList
    
    def getLastNode(self):
            current = self.head
            
            while current.next != self.head:
                current = current.next

            return current

    ############## GENERAL METHODS ##############

    ############## INSERTION / DELETION ##############
    
    def append(self, data):
        ########################################################################################
        # There are 2 cases :                                                                 ##
        # ~ 1. The cllist doesn't have a head node, so we will have to create one             ##
        # ~ 2. The cllist has a head node, so we will have to iterate to the end of the llist ##
        ########################################################################################

        if not self.head:
            # Create the head
            self.head = Node(data)
            self.head.next = self.head
        else:
            # Iterate to the end of the cllist and add it
            current = self.head
            appendNode = Node(data)

            # Iterate to the end to get the last node
            while current.next != self.head:
                current = current.next

            # Change the pointer of the last node to point at a new node, not at the head of the cllist
            current.next = appendNode

            # Change the pointer of the last node to pointer at the head of the cllist, since it is a 'circular" linked list
            appendNode.next = self.head 
        
        # Increment the length of the cllist
        self.length += 1
    
    def prepend(self, data):
        #########################################################################################################################################################################################
        # There are 2 cases:                                                                                                                                                                   ##
        # ~ 1. The cllist doesn't have a head node, so we will have to create one                                                                                                              ##
        # ~ 2. The cllist has a head node so we will have to iterate to the end of the cllist and replace the next node of the last node with a new one and then change the head of the cllist ##
        #########################################################################################################################################################################################

        if not self.head:
            # Create the head
            self.head = Node(data)
            self.head.next = self.head
        else:
            # Iterate to the end of the cllist and change the pointer
            current = self.head
            prependNode = Node(data)

            # Iterate to the end to get the last node
            while current.next != self.head:
                current = current.next
    
            # Change the pointer of the last node
            current.next = prependNode

            # Change the pointer of the prepend node, to point to the head of the cllist
            prependNode.next = self.head

            # Change the head of the llist to a new node
            self.head = prependNode

        # Increment the length of the cllist
        self.length += 1

    def insertAfterNode(self, node, data):
        # Check the node
        if not node:
            raise ValueError("The given node is not valid.")

        # Keep track of the current and of the "after"-node in the cllist, to insert a new node after the current node, that will bind with the "after"-node
        current = self.head
        after = self.head.next
        insertNode = Node(data)

        # Find the node to insert after
        while current != node:
            current = after 
            after = after.next

        # Change pointers
        current.next = insertNode
        insertNode.next = after

        # Increment the length of the cllist
        self.length += 1
    def insertAtIndex(self, index, data):
        # Check the given index
        if index > self.length or index < 0:
            raise IndexError("The given index is too big for the list or too small")
        
        if index == 0:
            # Prepend the node

            # Iterate over the entire cllist to get the last node
            current = self.head
            prependNode = Node(data)

            # Iterate over the cllist 
            while current.next != self.head:
                current = current.next

            # Change the pointers of the nodes
            current.next = prependNode
            prependNode.next = self.head
            self.head = prependNode
        elif index == self.length:
            # Append the node

            # Itearte over the eniter cllist to get the last node
            current = self.head
            appendNode = Node(data)

            # Itearte over the cllist
            while current.next != self.head:
                current = current.next

            # Change the pointers of the nodes
            current.next = appendNode
            appendNode.next = self.head
        else:
            # Keep track of the previous & current - node, while counting the index
            prev = None
            current = self.head
            indexTrack = 0
            insertNode = Node(data)

            # Find the node at the given index
            while indexTrack < index:
                prev = current
                current = current.next

                indexTrack += 1

            prev.next = insertNode
            insertNode.next = current

        self.length += 1
    
    def deleteNode(self, node):
        # Check node
        if not node:
            raise ValueError("The given node is not valid.")

        if node == self.head:
            # Change the pointer of the last node to the next node after the head node and then update the head node
            current = self.head
            
            # Iterate over the cllist to find the last node
            while current.next != self.head:
                current = current.next

            # Change the pointers
            current.next = self.head.next
            self.head = self.head.next
        else:
            # Look for the node that needs to be deleted while keeping track of the previous node. When you find the nodes, set the pointer of the previous node to the node in front of the node that needs to be deleted
            
            prev = None
            current = self.head

            # Iterate over the cllist to find the node that needs to be deleted
            while current.next != self.head and current != node:
                prev = current
                current = current.next

            # Change the pointers
            prev.next = current.next
            current = None
        
        # Decrement the length of the cllist
        self.length -= 1
    def deleteAtIndex(self, index):
        # Check index
        if index >= self.length or index < 0:
            raise IndexError("The given index is not valid. It is either too big for the cllist or too small ( < 0 ).")
        
        if index == 0:
            # Change the pointer of the last node to the next node after the head node and then update the head node
            current = self.head

            # Iterate over cllist to find the last node
            while current.next != self.head:
                current = current.next
               
            # Change the pointers
            current.next = self.head.next
            self.head = self.head.next
        else:
            # Look for the node that needs to be deleted at the given index while keeping track of the previous node. After that change the pointers in the proper order in order to delete the node at the given index
            prev = None
            current = self.head
            indexTrack = 0
            
            # Iterate over the list till the given index  
            while indexTrack < index:
                prev = current
                current = current.next

                indexTrack += 1

            # Change the pointers in the proper order
            prev.next = current.next
            current = None
        
        # Decrement the length of the cllist
        self.length -= 1

    ############## INSERTION / DELETION ##############

    ############## OTHERS ##############
    
    def swapNodes(self, node1, node2):
        # Check the given nodes
        if not node1 or not node2:
            raise ValueError("The given nodes are not valid.")
        if node1 == node2:
            return

        # Get the previous nodes for each swap node
        pv1 = None # - > previous node of the first node that needs to be swaped 
        pv2 = None # - > previous node of the second node that needs to be swaped

        # Check if one of the nodes is a head node, if that is the case the previous node would be the last node
        if node1 == self.head:
            pv1 = self.getLastNode()
        if node2 == self.head:
            pv2 = self.getLastNode()
            
        # Now iterate to get all the previous needed nodes
        prev = None
        current = self.head

        # Iterate and find pv1 & pv2 
        while not pv1 or not pv2: 
            if current == node1 and not pv1:
                pv1 = prev
            if current == node2 and not pv2:
                pv2 = prev

            prev = current
            current = current.next

        # Swap the nodes
        pv1.next, pv2.next = pv2.next, pv1.next
        node1.next, node2.next = node2.next, node1.next

        # Check for head node and change it in case one of the given swap nodes was a head node ( change the head to the opposite node )
        if node1 == self.head:
            self.head = node2
        elif node2 == self.head:
            self.head = node1
    
    def swapNodesAtIndexes(self, index1, index2):
        # Check the indexes
        if index1 < 0 or index2 < 0 or index1 >= self.length or index2 >= self.length:
            raise IndexError("The provided indexes aren't valid. One or both were too big for the length of the llist ( >= ) or they were too small ( < 0 )")
        if index1 == index2:
            return

        # Get the previous & nodes at the given indexes
        pv1 = None # ~ previous node of the first node 
        n1  = None # ~ first node

        pv2 = None # ~ previous node of the second node
        n2  = None # ~ second node

        # Check if one of the nodes is a head node
        if index1 == 0:
            # Set the previous node of the first node to the last element of the cllist
            pv1 = self.getLastNode()

            # Set the node to the head node of the cllist 
            n1 = self.head
        if index2 == 0:
            # Set the previous node of the second node to the last element of the cllist
            pv2 = self.getLastNode()
            
            # Set the node to the head node of the cllist
            n2 = self.head

        prev = None
        current = self.head
        indexTrack = 0

        # While not all values are found : 
        while not pv1 or not n1 or not pv2 or not n2:
            if indexTrack == index1 and not pv1 and not n1:
                pv1 = prev
                n1 = current
            if indexTrack == index2 and not pv2 and not n2:
                pv2 = prev
                n2 = current

            prev = current
            current = current.next

            indexTrack += 1

        # Swap the nodes
        pv1.next, pv2.next = pv2.next, pv1.next
        n1.next, n2.next = n2.next, n1.next

        # Check for head nodes
        if n1 == self.head:
            self.head = n2
        elif n2 == self.head:
            self.head = n1

    def reverse(self):
        # To reverse the circular linked list we will change the pointers ( .next ) of each node to the node before it
        prev = None
        current = self.head

        while current.next != self.head:
            nodeAfter = current.next

            current.next = prev

            prev = current
            current = nodeAfter

        current.next = prev 
        self.head.next = current
        self.head = current

    def mergeBothSorted(self, merge_cllist):
        ''' 
        We will merge a sorted cllist where both lists are sorted :
        Example :

            cllist1 -- > [1, 5, 7, 9, 10]
            cllist2 -- > [2, 3, 4, 6, 8 ]

            after merge method :
            cllist1 -- > [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        '''
        
        # Create pointers
        P = self.head
        Q = merge_cllist.head
        S = None

        # Create the main node at the lowest node between P & Q 
        if P.data < Q.data:
            S = Node(self.head.data)
            P = P.next
        elif Q.data < P.data:
            S = Node(merge_cllist.head.data)
            Q = Q.next

        newHeadNode = S

        # Iterate over the nodes in both cllists 
        while ( P is not self.head ) or ( Q is not merge_cllist.head ):
            for i in range(2):
                print()

            print("P -- > {0}".format(P.data))
            print("Q -- > {0}".format(Q.data))
            print("S -- > {0}".format(S.data))

            for i in range(2):
                print()

            if S.data < Q.data and Q.data < P.data:
                S.next = Node(Q.data)
                Q = Q.next
            elif S.data < P.data and P.data < Q.data:
                S.next = Node(P.data)
                P = P.next

            S = S.next
        
        self.head = S
        S.next = newHeadNode

    ############## OTHERS ##############


cllist = CircularLinkedList()
cllist_2 = CircularLinkedList()

for i in [1, 5, 7, 9, 10]:
    cllist.append(i)
for i in [2, 3, 4, 6, 8]:
    cllist_2.append(i)

for i in range(3):
    print()

cllist.mergeBothSorted(cllist_2)

print(" -- > ")
print(cllist.getNodeData())
