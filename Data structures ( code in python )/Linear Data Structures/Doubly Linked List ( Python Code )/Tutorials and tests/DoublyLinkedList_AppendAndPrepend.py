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

dll = DoublyLinkedList()

for i in list(range(1, 11)):
    dll.prepend_tutorial(i)



for i in range(3):
    print()

print(" -- > ")
print(dll.getNodeData())
