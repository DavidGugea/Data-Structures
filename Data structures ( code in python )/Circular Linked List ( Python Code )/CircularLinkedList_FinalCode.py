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
            
            ~ Node swap ( input : nodes to be swaped   )   ( self.swapNodes(node1, node2) )             -> None                    []
            ~ Node swap ( input : indexes of the nodes )   ( self.swapNodesAtIndexes(index1, index2) )  -> None                    []

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

cllist = CircularLinkedList()

for charCode in list(range(ord("A"), ord("D") + 1, 1)):
    cllist.append(chr(charCode))

cllist.deleteAtIndex(1)

for i in range(3):
    print()

print(" -- > ")
print(cllist.getNodeData())
