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

    def reverseString(self, givenString):
        stringStack = Stack()

        for char in givenString:
            stringStack.push(str(char))

        return "".join(stringStack.get_stack()[::-1]) 

    def convertIntegerToBinary(self, integer):
        trackStack = Stack()

        while integer > 0:
            trackStack.push(str(integer % 2))
            integer //= 2

        return "".join(trackStack.get_stack()[::-1])

    def checkParanthesis(self, paranthesisString):
        mainStack = Stack()
        track = list()

        opened = [ "{", "[", "(" ]
        closed = [ "}", "]", ")" ]

        for char in paranthesisString[::-1]:
            mainStack.push(char)

        while not mainStack.is_empty():
            if mainStack.peek() in opened:
                track.append(mainStack.peek())
                mainStack.pop()
            elif mainStack.peek() in closed and track:
                paranthesis = mainStack.peek()
                if ( track[-1] == "{" and paranthesis != "}" ) or ( track[-1] == "[" and paranthesis != "]" ) or ( track[-1] == "(" and paranthesis != ")" ):
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
