class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            current = self.head
            appendNode = Node(data)

            while current.next != self.head:
                current = current.next

            current.next = appendNode
            appendNode.next = self.head

        self.length += 1
    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            current = self.head
            prependNode = Node(data)

            while current.next != self.head:
                current = current.next

            current.next = prependNode
            prependNode.next = self.head
            self.head = prependNode

        self.length += 1

    def getNodeData(self):
        nodeDataList = [self.head.data] 
        current = self.head.next 

        while current is not self.head:
            nodeDataList.append(current.data)
            current = current.next

        return nodeDataList

    def splitListInHalf(self):
        # Split the circular linked list and return two circular linked lists with both halves
        firstHalf_CLLIST = CircularLinkedList()
        secondHalf_CLLIST = CircularLinkedList()

        current = self.head
        index = 0

        while current.next != self.head:
            if index < self.length // 2:
                firstHalf_CLLIST.append(current.data)
            else:
                secondHalf_CLLIST.append(current.data)

            current = current.next
            index += 1

        # Add left over
        secondHalf_CLLIST.append(current.data)

        return [ firstHalf_CLLIST, secondHalf_CLLIST ]

    def splitListAtNodeData(self, data):
        firstHalf_CLLIST = CircularLinkedList()
        secondHalf_CLLIST = CircularLinkedList()

        current = self.head
        afterTargetValue = False

        while current.next != self.head:
            if not afterTargetValue:
                firstHalf_CLLIST.append(current.data)
            else:
                secondHalf_CLLIST.append(current.data)

            if current.data == data:
                afterTargetValue = True

            current = current.next

        secondHalf_CLLIST.append(current.data)

        return [ firstHalf_CLLIST, secondHalf_CLLIST ]
    def splitAtIndex(self, index):
        firstHalf_CLLIST = CircularLinkedList()
        secondHalf_CLLIST = CircularLinkedList()

        current = self.head
        indexTrack = 0

        while current.next != self.head:
            if indexTrack <= index:
                firstHalf_CLLIST.append(current.data)
            else:
                secondHalf_CLLIST.append(current.data)

            current = current.next
            indexTrack += 1

        if index == self.length - 1:
            firstHalf_CLLIST.append(current.data)
        else:
            secondHalf_CLLIST.append(current.data)

        return [ firstHalf_CLLIST, secondHalf_CLLIST ]

cllist = CircularLinkedList()

for charCode in list(range(ord("A"), ord("D") + 1, 1)):
    cllist.append(chr(charCode))

for split_cllist in cllist.splitAtIndex(3):
    if split_cllist.head:
        print(split_cllist.getNodeData())
    else:
        print(None)

for i in range(3):
    print()

print(" -- > ")
print(cllist.getNodeData())
