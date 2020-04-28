class Node(object):
    def __init__(self, data):
        self.data = data
        self.address_store = None

    def get_by_address(self, SA):
        # SA = search_address 
        ids = list()

        for gv in tuple(globals().values()):
            if id(gv) == SA:
                ids.append(gv)

        if len(ids) == 0:
            return None
        else:
            return ids[0]

    def get_address(self):
        return id(self)

    def setNearNodes(self, prev_node = None, next_node = None):
        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.get_address()

        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.get_address()

        self.address_store = prev_address ^ next_address

    def get_next(self, prev_node):
        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.get_address()

        next_node_address = self.address_store ^ prev_address

        return self.get_by_address(next_node_address)

    def get_prev(self, next_node):
        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.get_address()

        prev_node_address = self.address_store ^ next_address

        return self.get_by_address(prev_node_address)

node1 = Node("A")
node2 = Node("B")

node1.setNearNodes(prev_node = None, next_node = node2)
print("NEXT NODE -- > {0}".format(node1.get_next(None).data))
print("PREV NODE -- > {0}".format(node1.get_prev(node2)))
