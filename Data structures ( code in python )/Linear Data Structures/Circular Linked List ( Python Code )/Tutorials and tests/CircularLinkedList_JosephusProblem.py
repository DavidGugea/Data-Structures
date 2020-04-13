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
    def removeAtIndex_MyCode(self, deleteIndex):
        if deleteIndex == 0:
            current = self.head
            
            while current.next != self.head:
                current = current.next

            current.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            current = self.head
            index = 0

            while index < deleteIndex:
                prev = current
                current = current.next

                index += 1

            
            prev.next = current.next
            current = None

        self.length -= 1
    def josephusProblem_myCode(self, step):
        stepTrack = 0
        current = self.head

        while self.length >= step:
            if ( stepTrack + 1 ) % step == 0:
                self.removeAtIndex_MyCode(stepTrack)

            stepTrack += 1
            current = current.next
            if current.next == self.head:
                stepTrack = 0

    def __len__(self):
        counter = 1
        current = self.head

        while current.next != self.head:
            counter += 1
            current = current.next 

        return counter

    def remove_node(self, node):
        if self.head == node:
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
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def josephusProblem_tutorialCode(self, step):
        cur = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1

            self.remove_node(cur)
            cur = cur.next

cllist = CircularLinkedList()

'''
for charCode in list(range(ord("A"), ord("H") + 1, 1)):
    cllist.append(chr(charCode))
'''

for i in list(range(1, 5)):
    cllist.append(i)

cllist.josephusProblem_myCode(2)

# cllist.remove_node(cllist.head)

for i in range(3):
    print()

print(" -- > ")
#print(cllist.head.data)
#print(cllist.head.next.data)
print(cllist.getNodeData())
