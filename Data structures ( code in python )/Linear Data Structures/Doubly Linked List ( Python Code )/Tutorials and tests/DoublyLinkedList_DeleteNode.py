class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def append_myCode(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            prev = None
            current = self.head

            while current.next:
                prev = current 
                current = current.next

            AppendNode = Node(data)
            AppendNode.prev = current
            current.next = AppendNode

    def prepend_myCode(self, data):
        prependNode = Node(data)
        prependNode.next = self.head
        self.head = prependNode

    def append_tutorial(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head

            while cur.next:
                cur = cur.next

            new_node.prev = cur 
            cur.next = new_node

    def prepend_tutorial(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def getNodeData(self):
        nodeDataList = list()
        current = self.head

        while current:
            nodeDataList.append(current.data)
            current = current.next

        return nodeDataList

    def deleteNode_myCode(self, nodeData):
        if self.head.data == nodeData:
            if not self.head.next:
                self.head = None
            else:
                nxt = self.head.next
                nxt.prev = None
                self.head = nxt
                return        
        else:
            current = self.head

            while current:
                if current.data == nodeData:
                    break
                prev = current
                current = current.next

            if not current:
                raise ValueError("The given data couldn't be found in the list.")

            prev = current.prev
            prev.next = current.next
            if current.next:
                current.next.prev = prev
            current = None

    def deleteNode_tutorial(self, key):
        cur = self.head
        while cur:
            # Case 1:
            if cur.data == key and cur == self.head:
                if not cur.next: 
                    cur = None
                    self.head = None
                    return
                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                # Case 3:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    
                    prev.next = nxt
                    nxt.prev = prev

                    cur = None
                    return
                # Case 4:
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return

            cur = cur.next

dll = DoublyLinkedList()

for i in list(range(1, 11)):
    dll.append_myCode(i)

dll.deleteNode_tutorial(1)

for i in range(3):
    print()

print(" -- > ")
print(dll.getNodeData())
