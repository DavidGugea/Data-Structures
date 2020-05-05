import random

class Node(object):
    def __init__(self, data):
        self.data = data

        self.next = None
        self.prev = None

        self.down = None 
        self.up = None

class SkipList(object):
    def __init__(self):
        for i in range(5):
            exec("self.head{0}=None\nself.last{0}=None".format(i))

    def present(self):
        LAYERS = SL.getNodeData()[::-1] 
        for i in range(4, -1, -1):
            print("LAYERS {0} -- > {1}".format(i, LAYERS[4 - i]))

    def getNodeData(self):
        LAYERS_DATA = [ list() for i in range(5) ]
        
        for i in range(5):
            exec("current = self.head{0}\nwhile current:\n\tLAYERS_DATA[{0}].append(current.data)\n\tcurrent = current.next".format(i))

        return LAYERS_DATA

    def search(self, data, DIRECT_RETURN = True):
        '''
        If DIRECT_TURN is True, we return the node found the first time, at any layer, we don't dig down to the bottom layer ( LEVEL 0 LAYER / LAYER 0 ) to return the complete bottom ones.
        OTHERWISE, once the node data is found, we dig down from the node we found, to the LAYER 0 LEVEL and return the bottom node
        '''
        # Start up from the top layer head node
        prev = None
        current = self.head4

        while current:
            if current.data == data:
                if DIRECT_RETURN: return current
                else:
                    while current.down:
                        current = current.down

                    return current
            elif current.data < data and not current.next and not prev:
                current = current.down
                prev = None
            elif current.data > data or ( current.data < data and not current.next and prev ):
                if not prev:
                    raise ValueError("The given data couldn't be found in the node")

                current = prev.down
                prev = None
            elif current.data < data and current.next:
                prev = current
                current = current.next
            
        raise ValueError("The given data couldn't be found in the node")


    def append(self, data):
        if not self.head0:
            for i in range(5):
                exec("self.head{0}=Node(data)\nself.last{0}=Node(data)\n".format(i))

            for i in range(5):
                if i == 0:
                    self.head0.up = self.head1
                    self.head0.down = None

                    self.last0.up = self.last1
                    self.last0.down = None 
                elif i == 4:
                    self.head4.up = None
                    self.head4.down = self.head3

                    self.last4.up = None
                    self.last4.down = self.last3
                else:
                    HEAD_UP_EXEC_STRING = "self.head{0}.up = self.head{1}"
                    HEAD_DOWN_EXEC_STRING = "self.head{0}.down = self.head{2}"
                    
                    LAST_UP_EXEC_STRING = "self.last{0}.up = self.last{1}"
                    LAST_DOWN_EXEC_STRING = "self.last{0}.down = self.last{2}"

                    FULL_EXEC_SET_STRING = "{0}\n{1}\n{2}\n{3}".format(HEAD_UP_EXEC_STRING, HEAD_DOWN_EXEC_STRING, LAST_UP_EXEC_STRING, LAST_DOWN_EXEC_STRING)
                    exec(FULL_EXEC_SET_STRING.format(i, i+1, i-1))
        else:
            if not self.head0.next:
                self.last0 = Node(data)

                self.last0.prev = self.head0
                self.head0.next = self.last0
            else:
                NEW_APPEND_NODE = Node(data)

                NEW_APPEND_NODE.prev = self.last0
                self.last0.next = NEW_APPEND_NODE

                self.last0 = self.last0.next

            counter = 1

            current = self.last0
            randomSkip = random.randint(1, 2)
            
            while randomSkip != 2: 
                '''
                EXEC_STRING IS -- >

                if not self.head{0}.next:
                    self.last{0} = Node(data)

                    self.last{0}.prev = self.head{0}
                    self.head{0}.next = self.last{0}

                    self.last{0}.down = current
                    current.up = self.last{0}
                else:
                    newNode = Node(data)

                    self.last{0}.next = newNode
                    newNode.prev = self.last{0}

                    newNode.down = current
                    current.up = newNode

                    self.last{0} = self.last{0}.next
                '''

                EXEC_STRING = "if not self.head{0}.next:\n\tself.last{0} = Node(data)\n\tself.last{0}.prev = self.head{0}\n\tself.head{0}.next = self.last{0}\n\tself.last{0}.down = current\n\tcurrent.up = self.last{0}\nelse:\n\tnewNode = Node(data)\n\tself.last{0}.next = newNode\n\tnewNode.prev = self.last{0}\n\tnewNode.down = current\n\tcurrent.up = newNode\n\tself.last{0} = self.last{0}.next" 
                exec(EXEC_STRING.format(counter))
                
                counter += 1
                if counter == 5:
                    break
                
                randomSkip = random.randint(1, 2)

SL = SkipList()

for i in range(1, 11):
    SL.append(i)

for i in range(3):
    print()

print(SL.search(2))

for i in range(3):
    print()

SL.present()
