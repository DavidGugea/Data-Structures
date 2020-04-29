def get_by_address(SA):
    # SA = > search_address
    ids = list()

    for gv in tuple(globals().values()):
        if id(gv) == SA:
            ids.append(gv)

    if not ids:
        return None 
    else:
        return ids[0]

class Node(object):
    def __init__(self, data):
        self.data = data
        self.address_store = None
    
    def get_address(self):
        return id(self)

    def setNearNodes(self, prev_node = None, next_node = None):
        # Get the addresses of both 'neighbouring' nodes ( prev & next ) 
        if prev_node:
            prev_address = prev_node.get_address()
        else:
            prev_address = 0 

        if next_node:
            next_address = next_node.get_address()
        else:
            next_address = 0 

        # Set up the address store of * SELF *
        self.address_store = prev_address ^ next_address

    def getNextNode(self, prev_node):
        if self.address_store == None:
            raise Exception("The node doesn't have a store address. Set the near nodes first.")

        if prev_node:
            prev_address = prev_node.get_address()
        else:
            prev_address = 0 

        next_address = self.address_store ^ prev_address
        return get_by_address(next_address)

    def getPrevNode(self, next_node):
        if self.address_store == None:
            raise Exception("The node doesn't have a store address. Set the near nodes first.")

        if next_node:
            next_address = next_node.get_address()
        else:
            next_address = 0 

        prev_address = self.address_store ^ next_address
        return get_by_address(prev_address)

class XORLinkedList(object):
    def __init__(self):
        self.head = None
           
    def getItems(self):
        items = list()

        prev = None
        current = self.head

        while current:
            items.append(current.data)

            if not current.address_store:
                break

            temp = current
            current = current.getNextNode(prev)
            prev = temp

        return items

XLL = XORLinkedList()

print("START -- > ") 
print(XLL.getItems())
print("< -- START ")

for i in range(5):
    print()

################################################

# XLL.append("A")
# XLL.append("B")

# print("HEAD NODE -- > {0}".format(XLL.head))
# print("HEAD.NEXT NODE -- > {0}".format(XLL.head.getNextNode(None)))

node1 = Node("A")
node2 = Node("B")

node1.setNearNodes(None, node2)
print(node1.getNextNode(None).data)
print(node1.getPrevNode(node2))

print()

node2.setNearNodes(node1, None)
print(node2.getNextNode(node1))
print(node2.getPrevNode(None).data)


################################################

for i in range(5):
    print()

print("END -- > ")
print(XLL.getItems())
print("< -- END ")
