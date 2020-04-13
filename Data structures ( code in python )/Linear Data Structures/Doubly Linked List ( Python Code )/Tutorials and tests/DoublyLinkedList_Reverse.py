class Node(object):
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return

        current = self.head
        while current.next:
            current = current.next

        appendNode = Node(data)
        current.next = appendNode
        appendNode.prev = current

    def prepend(self, data):
        prependNode = Node(data)
        prependNode.next = self.head

        if self.head:
            self.head.prev = prependNode

        self.head = prependNode

    def getNodeDataList(self):
        nodeDataList = list()
        current = self.head

        while current:
            nodeDataList.append(current.data)
            current = current.next

        return nodeDataList

    def reverse_myCode(self):
        prev = None
        current = self.head

        while current:
            nxt = current.next

            current.next = current.prev
            current.prev = nxt

            prev = current
            current = nxt 

        self.head = prev

    def reverse_tutorial(self):
        tmp = None
        cur = self.head

        while cur:
            tmp = cur.prev

            cur.prev = cur.next
            cur.next = tmp
            
            cur = cur.prev
        
        if tmp:
            self.head = tmp.prev


dll = DoublyLinkedList()

for i in list(range(1, 11)):
    dll.append(i)

dll.reverse_tutorial()

for i in range(3):
    print()

print(" -- > ")
print(dll.getNodeDataList())
