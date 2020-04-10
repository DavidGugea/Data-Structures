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

        Methods :
    
            ############## GENERAL METHODS ##############
            
            ~ Get length                   ( self.getLength )      -> number    [x]
            ~ Create __len__(self) method  ( len(self) )           -> number    [x]
            
            ~ Node at index                ( self.atIndex(index) ) -> number    [x]

            ############## GENERAL METHODS ##############

            ############## INSERTION / DELETION ##############
            
            ~ Append ( self.append(data) )                       -> None     []
            ~ Prepend ( self.prepend(data) )                     -> None     []

            ~ Insert after node ( self.insertAfterNode(node) )   -> None     []
            ~ Insert at index   ( self.insertAtIndex(index)  )   -> None     []

            ~ Delete after node ( self.deleteAfterNode(node) )   -> None     []
            ~ Delete at index   ( self.deleteAtIndex(index)  )   -> None     []

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

    ############## GENERAL METHODS ##############

    ############## INSERTION / DELETION ##############
    
    def append(self, data):
        ########################################################################################
        # There are 2 cases :                                                                 ##
        # ~ 1. The cllist doesn't have a head node, so we will have to create one             ##
        # ~ 2. The cllist has a head node, so we will have to iterate to the end of the llist ##
        ########################################################################################

        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            pass

        
        # Increment the length of the cllist
        self.length += 1

    ############## INSERTION / DELETION ##############

