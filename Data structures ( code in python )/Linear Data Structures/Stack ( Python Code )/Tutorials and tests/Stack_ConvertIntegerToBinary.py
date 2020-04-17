import pprint

class Stack(object):
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return not self.items 

    def peek(self):
        if self.items:
            return self.items[ len(self.items) - 1 ]
        else:
            return None
    
    def get_stack(self):
        return self.items

def convertToBinary_myCode(integer):
    s = Stack()

    while integer != 0:
        s.push(str(integer % 2))
        integer //= 2

    return "".join(s.get_stack()[::-1])

def convertToBinary_tutorial(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)

        dec_num //= 2

    bin_num = str()

    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(convertToBinary_tutorial(125))
