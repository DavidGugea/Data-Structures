class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, keyDataNode):
        if not self.head:
            self.head = Node(keyDataNode)
            self.head.next = self.head
            return
        else:
            newAppendNode = Node(keyDataNode)
            
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = newAppendNode
            newAppendNode.next = self.head
    def prepend(self, keyDataNode):
        if not self.head:
            self.head = Node(keyDataNode)
            self.head.next = self.head
            return
        else:
            current = self.head
            prependNode = Node(keyDataNode)

            while current.next != self.head:
                current = current.next

            current.next = prependNode
            prependNode.next = self.head

            self.head = prependNode
    def remove(self, keyDataNode):
        if keyDataNode == self.head.data:
            current = self.head

            while current.next != self.head:
                current = current.next

            if current == self.head:
                self.head = None
                return
            else:
                current.next = self.head.next
                self.head = self.head.next
        else:
            prev = None
            current = self.head
            
            while current.data != keyDataNode:
                prev = current
                current = current.next

            prev.next = current.next
            current = None


    def nodeData(self):
        if self.head:
            nodeDataList = [self.head.data]

            current = self.head.next
            while current is not self.head:
                nodeDataList.append(current.data)
                current = current.next

            return nodeDataList
        else:
            return None

cclist = CircularLinkedList()
cclist.prepend("Z")
cclist.append("A")
cclist.append("B")
cclist.append("C")
cclist.append("D")
cclist.prepend("Y")
cclist.prepend("X")

cclist.remove("A")
cclist.remove("B")
cclist.remove("C")
cclist.remove("D")

print(cclist.nodeData())
