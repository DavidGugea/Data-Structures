class Node(object):
    def __init__(self, data):
        self.data = data

        self.prev = None
        self.next = None

    def get_address(self):
        return id(self)
'''
node1 = Node("A")
node2 = Node("B")

print("ID node1 -- > {0}".format(node1.get_address()))

node1.data = "X"
node1.next = node2
node1.prev = None

print("ID node1 -- > {0}".format(node1.get_address()))
'''
