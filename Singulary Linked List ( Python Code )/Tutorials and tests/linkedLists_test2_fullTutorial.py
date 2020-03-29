import pprint

# Create Node Class
class Node(object):
    def __init__(self, data):
        # Set the data of the node to the given arg
        self.data = data

        # Set the self.next ( next node ) to none | It will change as we add to the linked list
        self.next = None

# Create the linked list class
class LinkedList(object):
    def __init__(self):
        # Create the self.length value to keep track of the length of the linked list
        self.length = 0
        
        # Create the head node
        self.head = Node(None)

    # DISPLAY 
    def return_ListOfNodesData(self):
        nodeDataList = list()
        nodeIndexCounter = 0
        currentNode = self.head

        while nodeIndexCounter < self.length and currentNode != None:
            # Add node data to array
            nodeDataList.append(currentNode.data)
            # Update current node
            currentNode = currentNode.next

        # Return node data list
        return nodeDataList

    # INSERTION
    def appendNode(self, data):
        if self.head.data == None:
            # If the head hasn't been set already to a node, set the data of the head to the data passed in
            self.head.data = data

            # Update self.length
            self.length = 1

            return
        else:
            # Iterate over the linked list and find the last node ( The last node is the node that doesn't have a next node ( next is None )

            # Begin the counter from the head
            currentNode = self.head 
            
            # Iterate
            while currentNode.next != None:
                currentNode = currentNode.next # Move to the next node
    
            # Node found, create a new node with the data passed in by the user and set it to the next node of the last present node
            appendNode = Node(data)

            currentNode.next = appendNode
            
            # Update the length of the linked list ( increment it )
            self.length += 1
    def prependNode(self, data):
        # Create a new node with the data passed in by the user
        newNode = Node(data)

        # Transform the head to a the next node of a new node
        newNode.next = self.head

        # Update self.head to the new node we created 
        self.head = newNode

        # Update the length of the linked list
        self.length += 1

    # INSERTION
    def insertNodeAtIndex(self, insertIndex, data):
        # Check if the index is bigger or equal to the length of the linked list
        if insertIndex > self.length:
            raise IndexError("The index passed in was too big for the linked list")

        if insertIndex == 0:
            self.prependNode(data)
            return
        elif insertIndex == self.length - 1:
            self.appendNode(data)
            return
        
        # Create new node with the data passed in by the user
        newNode = Node(data)

        # Search for the index of the node
        nodeIndexTracker = 0
        currentNode = self.head
        
        while nodeIndexTracker != insertIndex - 1:
            # Increment node index tracker and update the current node
            nodeIndexTracker += 1
            currentNode = currentNode.next
         
        
        afterInsertionNode = currentNode.next 

        currentNode.next = newNode 
        newNode.next = afterInsertionNode
    def insertNodeAtNode(self, NodeToInsertBefore, data): 
        # Check if the passed in node is in the llist and keep track of it too, in case it's found we can the new node directly there
        nodeIndexTracker = 0
        currentNode = self.head

        nodeFound = False

        while nodeIndexTracker < self.length:
            if currentNode.data == NodeToInsertBefore.data:
                nodeFound = True
                break
            else:
                # Increment node index tracker and update the current node
                nodeIndexTracker += 1
                currentNode = currentNode.next
                
        if not nodeFound:
            raise ValueError("Node passed in doesn't exist in the linked list")
        
        if nodeIndexTracker == 0:
            self.prependNode(data)
        elif nodeIndexTracker == self.length - 1:
            self.appendNode(data)
        else:
            # Create a new node with the data passed in by the user
            newNode = Node(data)

            afterInsertionNode = currentNode.next
            
            currentNode.next = newNode
            newNode.next = afterInsertionNode 
    
    # DELETION
    def deleteNodeAtIndex(self, index):
        # Check if the index is bigger than the length of the llist
        if index > self.length:
            raise IndexError("Index was too big for the llist")

        if index == self.length - 1:
            # Delete the last node of the llist
            nodeIndexTracker = 0
            pastNode = self.head

            while nodeIndexTracker < self.length - 2:
                # Increment index tracker and update past node
                nodeIndexTracker += 1
                pastNode = pastNode.next

            # Set past node next node to none
            pastNode.next = None

            return 
        elif index == 0:
            # Delete the first node
            self.head = self.head.next

            return

        # Find the index of the node that the user wants to delete
        pastNode = self.head
        nodeIndexTracker = 0

        while nodeIndexTracker < index-1:
            # Update index tracker and past node
            nodeIndexTracker += 1
            pastNode = pastNode.next

        afterDeleteNode = pastNode.next.next
        pastNode.next = afterDeleteNode
    def deleteNodeAtNode(self, deleteNode):
        # Check if the delete node is in the llist and keep track of its last node
        nodeIndexTracker = 0
        nodeFound = False

        pastNode = None
        currentNode = self.head

        while nodeIndexTracker < self.length:
            if currentNode.data != deleteNode.data:
                if pastNode == None:
                    pastNode = self.head
                else:
                    pastNode = pastNode.next

                currentNode = currentNode.next 
                
                nodeIndexTracker += 1
            else:
                nodeFound = True
                break

        if nodeIndexTracker == self.length - 1:
            self.deleteNodeAtIndex(self.length - 1)
            return
        else:
            self.deleteNodeAtIndex(0)
            return
    
        afterCurrentNode = currentNode.next
        pastNode.next = afterCurrentNode

# Create linked list
llist = LinkedList()

# Append new nodes to the linked list
llist.appendNode(5)
llist.appendNode(10)

llist.prependNode(15)
llist.prependNode(20)

pprint.pprint(llist.return_ListOfNodesData(), indent = 50)

#llist.insertNodeAtIndex(0, 30)
#llist.insertNodeAtNode(Node(20), 30)

llist.deleteNodeAtNode(Node(15))

pprint.pprint(llist.return_ListOfNodesData(), indent = 50)
