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
        # There are 2 cases:
        # 1. There is no head node, so we will have to create one
        # 2. There already is a head node so we will have to set the next node of the previous node of the node that we want to delete to the node in front of the node that we want to delete
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
        # Try to have the nodes data using another alg.
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
