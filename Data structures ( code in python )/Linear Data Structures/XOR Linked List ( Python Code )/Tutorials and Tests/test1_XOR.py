def get_by_address(address, global_vars):
    if address == 0:
        return None

    return [x for x in global_vars.values() if id(x) == address][0]

class Node(object):
    def __init__(self, data):
        # Set up the data & address_store
        self.data = data
        self.address_store = None

    def get_address(self):
        # Return the id of node
        return id(self)

    def set_neighbours(self, prev_node = None, next_node = None):
        # Get the local_address ( id of self )
        local_address = self.get_address()

        if prev_node == None:
            # Set the previous address of the previous node to 0 
            prev_address = 0
        else:
            # Set up the prev_address of the previous node by getting its ID 
            prev_address = prev_node.get_address()

        # Do the same for the next node
        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.get_address()

        # Set up the address store for * SELF NODE * 
        self.address_store = prev_address ^ next_address

    def get_next(self, prev_node, global_vars):
        if self.address_store == None:
            raise Exception("set_neighbours not called yet, no next node !")

        if prev_node == None:
            prev_address = 0
        else:
            prev_address = prev_node.get_address()
        
        next_address = self.address_store ^ prev_address

        return get_by_address(address = next_address, global_vars = global_vars)

    def get_prev(self, next_node, global_vars):
        if self.address_store == None:
            raise Exception("set_neighbours not called yet, no next node !")
        
        if next_node == None:
            next_address = 0
        else:
            next_address = next_node.get_address()

        prev_address = self.address_store ^ next_address

        return get_by_address(prev_address, global_vars = global_vars)

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")

node1.set_neighbours(None, node2)
print("NEXT -- > {0}".format(node1.get_next(None, globals()).data))
print("PREV -- > {0}".format(node1.get_prev(node2, globals())))
