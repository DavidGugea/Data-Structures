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
        else:
            appendNode = Node(data)
            current = self.head

            while current.next:
                current = current.next

            appendNode.prev = current
            current.next = appendNode

    def prepend(self, data):
        prependNode = Node(data)
        prependNode.next = self.head
        if self.head:
            self.head.prev = prependNode
        self.head = prependNode

    def getNodeData(self):
        nodeDataList = list()
        current = self.head

        while current:
            nodeDataList.append(current.data)
            current = current.next

        return nodeDataList

    def removeDuplicates_myCode(self):
        newChainNode = self.head # new chain node for the dll
        current = self.head.next # iterate over the dll with this variable
        usedDataList = [self.head.data] # keeps track of used node data

        firstNodeInChain = newChainNode

        while current:
            if current.data not in usedDataList:
                appendNode = Node(current.data)

                appendNode.prev = newChainNode
                newChainNode.next = appendNode

                usedDataList.append(current.data)

                newChainNode = newChainNode.next

            current = current.next

        self.head = firstNodeInChain
    
    def delete_node(self, deleteNode):
        if self.head == deleteNode:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
        else:
            prev = None
            cur = self.head

            while cur != deleteNode:
                prev = cur
                cur = cur.next

            prev.next = cur.next
            if cur.next:
                cur.next.prev = prev

            cur = None

    def removeDuplicates_tutorial(self):
        cur = self.head
        seen = dict()

        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)

                cur = nxt 


dll = DoublyLinkedList()
for i in [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5]:
    dll.append(i)

dll.removeDuplicates_tutorial()

for i in range(3):
    print() 

print(" -- > ")
print(dll.getNodeData())
