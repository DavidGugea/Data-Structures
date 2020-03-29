import pprint

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.length = 1
        self.head = None

    # DISPLAY LLIST #

    def get_NodeList(self, GET_TYPE = 'NODE_DATA'):
        nodeList = list()
        nodeIndexTracker = 0
        
        currentNode = self.head

        while nodeIndexTracker < self.length:
            if GET_TYPE == 'NODE_DATA':
                nodeList.append(currentNode.data)
            elif GET_TYPE == 'NODE_OBJECT':
                nodeList.append(currentNode)

            nodeIndexTracker += 1
            currentNode = currentNode.next

        return nodeList

    # DISPLAY LLIST #

    # APPEND | PREPEND
    
    def appendNode(self, data):
        if self.head == None:
            self.head = Node(data)
            self.length = 1 
            return
        else:
            nodeIndexTracker = 0
            currentNode = self.head
            
            while nodeIndexTracker < self.length - 1:
                currentNode = currentNode.next
                nodeIndexTracker += 1

            currentNode.next = Node(data)
            self.length += 1
    
    def prependNode(self, data):
        if self.head == None:
            self.head = Node(data)
            self.length = 1
            return
        else:
            swapHeadNode = Node(data)
            swapHeadNode.next = self.head
            self.head = swapHeadNode

            self.length += 1
    
    # APPEND | PREPEND

    # INSERT AT #
    
    def insert_atIndex(self, index, data):
        if index > self.length:
            raise IndexError("The index was too big for the linked list.")

        if index == 0:
            self.prependNode(data)
            return
        elif index == self.length - 1:
            self.appendNode(data)
            return

        insertNode = Node(data)
        
        nodeIndexTracker = 0
        currentNode = self.head

        while nodeIndexTracker != index - 1:
            currentNode = currentNode.next
            nodeIndexTracker += 1
        
        nodeAfter_IndexInsert = currentNode.next

        
        currentNode.next = insertNode
        insertNode.next = nodeAfter_IndexInsert
        
        self.length += 1

    def insertNode_AfterNode(self, NodeLike, data):
        if NodeLike.data == self.head.data:
            self.prependNode(data)
            return

        nodeIndexTracker = 0
        currentNode = self.head

        while nodeIndexTracker < self.length:
            currentNode = currentNode.next
            nodeIndexTracker += 1

            if currentNode.data == NodeLike.data:
                break

        if nodeIndexTracker == self.length - 1:
            self.appendNode(data)
            return

        nodeAfterInsert = currentNode.next
        insertNode = Node(data)

        currentNode.next = insertNode
        insertNode.next = nodeAfterInsert

        self.length += 1

    # INSERT AT #

    # DELETE AT #
    
    def deleteNode_AtIndex(self, index):
        if index > self.length:
            raise IndexError("The index was too big for the linked list")

        if index == 0:
            nextHead = self.head.next
            self.head = nextHead
            self.length -= 1
            return

        nodeIndexTracker = 0

        pastNode = None
        currentNode = self.head

        while nodeIndexTracker != index:
            if pastNode == None:
                pastNode = self.head
            else:
                pastNode = pastNode.next

            currentNode = currentNode.next
            nodeIndexTracker += 1

        if nodeIndexTracker == self.length - 1:
            pastNode.next = None
        else:
            inFrontOfCurrent = currentNode.next
            pastNode.next = inFrontOfCurrent

        self.length -= 1
    
    def deleteNode_AtNode(self, NodeLike):
        if NodeLike.data == self.head.data:
            self.deleteNode_AtIndex(0)
            return

        nodeIndexTracker = 0
        nodeFound = False
        pastNode = None
        currentNode = self.head

        while nodeIndexTracker < self.length:
            if pastNode == None:
                pastNode = self.head
            else:
                pastNode = pastNode.next

            currentNode = currentNode.next
            nodeIndexTracker += 1
        
            
            if currentNode.data == NodeLike.data:
                nodeFound = True
                break 

        if nodeIndexTracker == self.length - 1:
            pastNode.next = None
        else:
            AfterNode = currentNode.next
            pastNode.next = AfterNode

        self.length -= 1
    
    # DELETE AT #   

llist = LinkedList()

llist.appendNode(5)
llist.appendNode(10)

llist.prependNode(15)
llist.prependNode(20)

pprint.pprint(llist.get_NodeList(), indent = 20)

llist.deleteNode_AtNode(Node(20))

pprint.pprint(llist.get_NodeList(), indent = 20)
