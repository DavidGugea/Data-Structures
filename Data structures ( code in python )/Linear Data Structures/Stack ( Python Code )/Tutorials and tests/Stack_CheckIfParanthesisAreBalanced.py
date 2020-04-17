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

def checkParanthesis_myCode(paranthesisString):
    mainStack = Stack()
    track = list() 

    opened = [ "{", "[", "(" ]
    closed = [ "}", "]" ,")" ] 

    for char in paranthesisString[::-1]:
        mainStack.push(char)

    pprint.pprint(mainStack.get_stack(), indent = 20)
    
    while not mainStack.is_empty():
        if mainStack.peek() in opened:
            track.append(mainStack.peek())
            mainStack.pop()
        elif mainStack.peek() in closed and track:
            paranthesis = mainStack.peek()
            if ( track[-1] == "{" and paranthesis != "}" )  or ( track[-1] == "[" and paranthesis != "]" ) or ( track[-1] == "(" and paranthesis != ")" ):
                return False
            else:
                mainStack.pop()
                del track[-1]
        else:
            return False
    
    if not track:
        return True
    else:
        return False

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "[" and p2 == "]":
        return True
    if p1 == "{" and p2 == "}":
        return True

    return False

def checkParanthesis_tutorial(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "{[(":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False
