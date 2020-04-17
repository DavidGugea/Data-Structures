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

def reverseString_myCode(givenString):
    newStack = Stack() 
    for char in givenString:
        newStack.push(char)
    
    reversedString = str()
        
    while not newStack.is_empty():
        reversedString += newStack.pop()

    return reversedString

myString = "Hello World"
print("Start string   -- > {0}".format(myString))
myString = reverseString_myCode(myString)
print("After rotation -- > {0}".format(myString))

for i in range(10):
    print()

def reverseString_tutorial(stack, input_str):
    # Loop through the string and push contents character by character onto stack.
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = str()

    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

stack = Stack()
input_str = "Hello"

print(reverseString_tutorial(stack, input_str))
