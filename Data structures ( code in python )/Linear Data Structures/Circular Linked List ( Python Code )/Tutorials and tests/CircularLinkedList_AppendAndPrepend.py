class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def prepend_myCode(self, data):
        # 2 cases : 
        # ~ 1. There is no head
        # ~ 2. There is already a head that needs to be "pushed forward"
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            return
    
        lastNode = self.head
        while lastNode.next != self.head:
            lastNode = lastNode.next   

        newNode = Node(data)

        lastNode.next = newNode
        newNode.next = self.head
        self.head = newNode 

    def prepend_tutorialCode(self, data):
        new_node = Node(data)
        cur = self.head

        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next

            cur.next = new_node 


        self.head = new_node

    def append_myCode(self, data):
        # Appending something in the list : there are 2 cases:
        # ~ case 1 : the head doesn't exist yet, so we will have to replace the head value, which is currently none to a new node data
        # ~ case 2 : the head exists already, go to the last node while keeping track of the previous node and then set the next node of the previous node to a new node with the given data as an input and set the next node of the current node which will be None to the head because it is a circular linked list so the last pointer of the list of the last node doesn't point to None like in a normal Singly Linked List, it will point to the head 

        # DO ~ case 1 : 
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            return

        # DO ~ case 2 :
        appendNode = Node(data)
        
        lastNode = self.head
        while lastNode.next != self.head:
            lastNode = lastNode.next

        lastNode.next = appendNode
        appendNode.next = self.head

    def append_tutorialCode(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            return
        else:
            new_node = Node(data)
            cur = self.head

            while cur.next != self.head:
                cur = cur.next

            cur.next = new_node
            new_node.next = self.head


    def print_list_myCode(self):
        nodeDataList = [self.head.data]
        current = self.head.next

        while current:
            nodeDataList.append(current.data)
            current = current.next

            if current is self.head:
                break

        return nodeDataList
    
    def print_list_tutorialCode(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next

            if cur == self.head:
                break



cllist = CircularLinkedList()
cllist.append_tutorialCode("C")
cllist.append_tutorialCode("D")
cllist.prepend_tutorialCode("B")
cllist.prepend_tutorialCode("A")
cllist.print_list_tutorialCode()

for i in range(3):
    print()

print(" -- > ")
print(cllist.head.data)
print(cllist.head.next.data)
print(cllist.head.next.next.data)
