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


cclist = CircularLinkedList()
cclist.append("C")
cclist.append("D")
cclist.prepend("B")
cclist.prepend("A")

for i in range(3):
    print()

print(" -- > ")
print(cclist.nodesData())
