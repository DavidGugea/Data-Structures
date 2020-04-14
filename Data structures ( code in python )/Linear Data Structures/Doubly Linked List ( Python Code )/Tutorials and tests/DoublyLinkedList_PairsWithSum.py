import itertools

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
        if not self.head:
            self.head = Node(data)
        else:
            prependNode = Node(data)

            self.head.prev = prependNode
            prependNode.next = self.head

            self.head = prependNode

    def getNodeDataList(self):
        nodeDataList = list()
        current = self.head

        while current:
            nodeDataList.append(current.data)
            current = current.next

        return nodeDataList
    
    def pairsWithSum_myCode(self, sumValue):
        pairs = list()
        for permutation in list(itertools.permutations(self.getNodeDataList(), 2)):
            if sum(permutation) == sumValue and tuple(permutation) not in pairs and tuple(permutation[::-1]) not in pairs:
                pairs.append(tuple(permutation))

        return pairs

    def pairsWithSum_tutorial(self, sum_val):
        pairs = list()
        
        p = self.head
        q = None

        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val and "( {0} , {1} )".format(p.data, q.data) not in pairs:
                   pairs.append("( {0} , {1} )".format(p.data, q.data))

                q = q.next

            p = p.next

        return pairs



dll = DoublyLinkedList()

for i in list(range(1, 6)):
    dll.prepend(i)

dll.append(5)
dll.prepend(-5)

print(dll.pairsWithSum_tutorial(0))

for i in range(3):
    print() 

print(" -- > ")
print(dll.getNodeDataList())
