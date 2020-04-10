class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def append(self, keyDataNode):
        if not self.head:
            self.head = Node(keyDataNode)
            self.head.next = self.head
        else:
            newAppendNode = Node(keyDataNode)
            
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = newAppendNode
            newAppendNode.next = self.head

        self.length += 1
    def prepend(self, keyDataNode):
        if not self.head:
            self.head = Node(keyDataNode)
            self.head.next = self.head
        else:
            current = self.head
            prependNode = Node(keyDataNode)

            while current.next != self.head:
                current = current.next

            current.next = prependNode
            prependNode.next = self.head

            self.head = prependNode

        self.length += 1
    def remove(self, keyDataNode):
        if keyDataNode == self.head.data:
            current = self.head

            while current.next != self.head:
                current = current.next

            if current == self.head:
                self.head = None
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

        self.length -= 1

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

    def splitListInHalf_MyCode(self):
        # self.length // 2 => Start of the second cclist
       
        firstHalf = CircularLinkedList()
        secondHalf = CircularLinkedList()
        
        prevNode = None
        currentNode = self.head
        index = 0

        borderNode = None

        while currentNode.next != self.head:
            if index < self.length // 2:
                firstHalf.append(currentNode.data)
            if index >= self.length // 2:
                secondHalf.append(currentNode.data)

            index += 1
            currentNode = currentNode.next

        secondHalf.append(currentNode.data)

        return [firstHalf, secondHalf]


cclist = CircularLinkedList()

for charCode in list(range(ord("A"), ord("N") + 1, 1)):
    cclist.append(chr(charCode))

for circularLinkedList in cclist.splitListInHalf():
    print(circularLinkedList.nodeData())

for i in range(3):
    print()

print(cclist.nodeData())
