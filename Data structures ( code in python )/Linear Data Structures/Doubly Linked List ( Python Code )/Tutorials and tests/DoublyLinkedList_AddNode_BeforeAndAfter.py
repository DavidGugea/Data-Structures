
class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def append_myCode(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            prev = None
            current = self.head

            while current.next:
                prev = current 
                current = current.next

            AppendNode = Node(data)
            AppendNode.prev = current
            current.next = AppendNode

    def prepend_myCode(self, data):
        prependNode = Node(data)
        prependNode.next = self.head
        self.head = prependNode

    def append_tutorial(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head

            while cur.next:
                cur = cur.next

            new_node.prev = cur 
            cur.next = new_node

    def prepend_tutorial(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def getNodeData(self):
        nodeDataList = list()
        current = self.head

        while current:
            nodeDataList.append(current.data)
            current = current.next

        return nodeDataList

    def addAfter_myCode(self, node, data):
        current = self.head
        insertNode = Node(data) 
        
        while current != node:
            current = current.next

        insertNode.prev = current
        insertNode.next = current.next
        current.next = insertNode
        current.next.next.prev = insertNode
    def addBefore_myCode(self, node, data):
        current = self.head
        insertNode = Node(data)

        while current.next != node:
            current = current.next

        insertNode.prev = current
        insertNode.next = current.next
        current.next = insertNode
        current.next.next.prev = insertNode

    def addAfter_tutorialCode(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append_tutorial(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            
            cur = cur.next
    def addBefore_tutorialCode(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend_tutorial(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev

            cur = cur.next

dll = DoublyLinkedList()

for i in list(range(1, 11)):
    dll.append_myCode(i)

dll.addBefore_tutorialCode(1, "A")

for i in range(3):
    print()

print(" -- > ")
print(dll.getNodeData())
