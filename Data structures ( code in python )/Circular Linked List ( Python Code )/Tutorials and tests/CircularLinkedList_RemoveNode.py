class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            return
        else:
            current = self.head

            while current.next != self.head:
                current = current.next

            newAppendNode = Node(data)
            current.next = newAppendNode

            newAppendNode.next = self.head

    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            return
        else:
            newPrependNode = Node(data)
            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = newPrependNode
            newPrependNode.next = self.head
            self.head = newPrependNode
    def nodesData(self):
        nodeDataList = [self.head.data]

        current = self.head.next 

        while current is not self.head:
            nodeDataList.append(current.data)
            current = current.next

        return nodeDataList
    
    def nodesData2(self):
        nodeDataList = list()
        current = self.head

        while current.next != self.head:
            nodeDataList.append(current.data)
            current = current.next

        nodeDataList.append(current.data)
        return nodeDataList

    def remove_myCode(self, data):
        if data == self.head.data:
            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            current = self.head

            while current.data != data:
                prev = current
                current = current.next

            prev.next = current.next
            current = None
    def remove_tutorialCode(self, key):        
        # Key => data value for the node that will have to be deleted

        if self.head.data == key:
            cur = self.head

            while cur.next != self.head:
                cur = cur.next

            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None

            while cur.next != self.head:
                prev = cur
                cur = cur.next

                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next



cclist = CircularLinkedList()
cclist.append("C")
cclist.append("D")
cclist.prepend("B")
cclist.prepend("A")

cclist.remove_myCode("D")
cclist.remove_myCode("C")
cclist.remove_myCode("B")
cclist.remove_myCode("A")

for i in range(3):
    print()

print(" -- > ")
print(cclist.nodesData())
