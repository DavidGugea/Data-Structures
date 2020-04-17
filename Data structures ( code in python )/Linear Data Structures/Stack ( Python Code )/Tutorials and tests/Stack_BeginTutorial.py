class Stack():
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item) 

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == list() 

    def peek(self):
        if self.items:
            return self.items[len(self.items) - 1] 
        else:
            return None

    def get_stack(self):
        return self.items

s = Stack()

print(s.peek())

for charCode in list(range(ord("A"), ord("D")+1, 1)):
    s.push(chr(charCode))

print(s.get_stack())
print(s.peek())
