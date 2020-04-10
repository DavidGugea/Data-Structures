class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None # set as make use of node

class LinkedList(object):
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            # Swap the self.head with the new node
            self.head = new_node
            return
        
        # We are at the start of the list || We start at the beginning of the list
        last_node = self.head
        
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
    
    def prepend(self, data):
        # Create a new node
        new_node = Node(data)

        # Change the head to a new node 
        new_node.next = self.head
        self.head = new_node

    def insertAfterNode(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return 
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next


        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

llist = LinkedList()

# Append nodes in linked list
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

# llist.insertAfterNode(llist.head.next, "E")

llist.delete_node("B")

llist.print_list()
