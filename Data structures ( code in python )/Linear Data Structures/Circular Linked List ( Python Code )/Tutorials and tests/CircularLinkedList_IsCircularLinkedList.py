class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = Node(data) 

    def getNodeData(self):
        nodeDataList = list()
        current = self.head

        while current:
            nodeDataList.append(current.data)
            current = current.next

        return nodeDataList

class CircularLinkedList(object):
    def __init__(self):
        self.head = None
    def __len__(self):
        if not self.head:
            return 0

        counter = 1
        current = self.head

        while current.next != self.head:
            current = current.next
            counter += 1

        return counter

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

    def removeNode(self, node):
        if node is self.head:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            current = self.head

            while current != node:
                prev = current
                current = current.next

            prev.next = current.next
            current = None
    def getNodeData(self):
        nodeDataList = [self.head.data]
        current = self.head.next

        while current is not self.head:
            nodeDataList.append(current.data)
            current = current.next

        return nodeDataList

    def josephusProblem(self, step):
        current = self.head
        while len(self) >= step:
            stepCounter = 1
            while stepCounter != step:
                current = current.next
                stepCounter += 1
            self.removeNode(current)
            current = current.next

    def is_circular_linked_list_myCode(self, input_list):
        current = input_list.head.next
        while current:
            if current == input_list.head:
                return True
            current = current.next
        return False
    def is_circular_linked_list_tutorialCode(self, input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur == input_list.head:
                return True

        return False


cllist = CircularLinkedList()
sllist = SinglyLinkedList()

for charCode in list(range(ord("A"), ord("D") + 1, 1)):
    cllist.append(chr(charCode))

for charCode in list(range(ord("A"), ord("D") + 1, 1)):
    sllist.append(chr(charCode))

print(cllist.getNodeData())
print(sllist.getNodeData())

print(cllist.is_circular_linked_list_tutorialCode(cllist))
print(cllist.is_circular_linked_list_tutorialCode(sllist))
