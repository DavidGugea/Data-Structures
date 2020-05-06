import random

class Node(object):
    def __init__(self, data):   
        self.data = data

        self.next = None
        self.prev = None

        self.up = None
        self.down = None

class SkipList(object):
    def __init__(self):
        for i in range(5):
            exec("self.head{0} = None\nself.last{0} = None".format(i))

    def getNodeData(self):
        LAYERS_DATA = [ list() for i in range(5) ]

        for i in range(5):
            exec("current = self.head{0}\nwhile current:\n\tLAYERS_DATA[{0}].append(current.data)\n\tcurrent = current.next".format(i))

        return LAYERS_DATA

    def present(self):
        LAYERS_DATA = self.getNodeData()[::-1]
        for i in range(4, -1, -1):
            print("LAYER {0} -- > {1}".format(i, LAYERS_DATA[4 - i]))

    def search(self, data, DIRECT_RETURN = True):
        # ~ START SEARCHING FROM THE TOP TO THE BOTTOM ~ # ( START WITH THE LAST LAYER HEAD NODE ) ~ #
        prev = None
        current = self.head4
        START_CURRENT = current

        print("SEARCH PRESENTATION -- >")
        for i in range(3):
            print()

        self.present() 
        
        for i in range(3):
            print()
        print("< -- SEARCH PRESENTATION ")

        while True:
            if current.data == data:
                if DIRECT_RETURN:
                    return current
                else:
                    while current.down:
                        current = current.down

                    return current
            elif current.data > data and not prev:
                raise ValueError("ASD")
            elif current.data > data and prev or (current.data < data and not current.next and prev) :
                current = prev.down
                prev = None  
                START_CURRENT = current
            elif current.data < data and not current.next and not prev:
                current = START_CURRENT.down
                prev = None
                START_CURRENT = current
            elif current.data < data and current.next:
                prev = current
                current = current.next

    def append(self, data):
        if not self.head0:
            for i in range(5):
                exec("self.head{0} = Node(data)\nself.last{0} = Node(data)".format(i))

            for i in range(5):
                if i == 0:
                    self.head0.down = None
                    self.head0.up = self.head1

                    self.last0.down = None
                    self.last0.up = self.last1
                elif i == 4:
                    self.head4.down = self.head3
                    self.head4.up = None

                    self.last4.down = self.last3
                    self.last4.up = None
                else:
                    exec("self.head{0}.up = self.head{1}\nself.head{0}.down = self.head{2}\nself.last{0}.up = self.last{1}\nself.last{0}.down = self.last{2}".format(i, i+1, i-1))
        else:
            if not self.head0.next:
                self.last0 = Node(data)

                self.last0.prev = self.head0
                self.head0.next = self.last0
            else:
                LAYER0_APPEND_NODE = Node(data) 

                LAYER0_APPEND_NODE.prev = self.last0 
                self.last0.next = LAYER0_APPEND_NODE
                
                self.last0 = self.last0.next

            current = self.last0
            randomSkip = random.randint(1, 2)
            counter = 1 

            while randomSkip != 2:
                '''
                if not self.head1.next:
                    self.last1 = Node(data)

                    self.last1.down = current
                    self.last1.prev = self.head1

                    self.head1.next = self.last1
                    current.up = self.last1
                else:
                    NEW_APPEND_NODE = Node(data)

                    self.last1.next = NEW_APPEND_NODE
                    NEW_APPEND_NODE.prev = self.last1

                    NEW_APPEND_NODE.down = current
                    current.up = NEW_APPEND_NODE

                    self.last1 = self.last1.next
                '''
        
                exec("if not self.head{0}.next:\n\tself.last{0} = Node(data)\n\tself.last{0}.down = current\n\tself.last{0}.prev = self.head{0}\n\tself.head{0}.next = self.last{0}\n\tcurrent.up = self.last{0}\nelse:\n\tNEW_APPEND_NODE = Node(data)\n\tself.last{0}.next = NEW_APPEND_NODE\n\tNEW_APPEND_NODE.prev = self.last{0}\n\tNEW_APPEND_NODE.down = current\n\tcurrent.up = NEW_APPEND_NODE\n\tself.last{0} = self.last{0}.next".format(counter))
            
                counter += 1
                if counter == 5:
                    break
                randomSkip = random.randint(1, 2)


SL = SkipList()

for i in range(1, 11):
    SL.append(i)

for i in range(3):
    print()

'''
for i in range(5):
    print(" -- > ")
    print("SL.head{0} == > {1}".format(i, eval("SL.head{0}.data".format(i))))
    print("SL.last{0} == > {1}".format(i, eval("SL.last{0}.data".format(i))))
    print("< -- ")

    for i in range(2):
        print()
'''

x = SL.search(2)

for i in range(3):
    print()

if not x:
    print("x -- > {0}".format(x))
else:
    print("x -- > {0}".format(x.data))

for i in range(3):
    print()

SL.present()
