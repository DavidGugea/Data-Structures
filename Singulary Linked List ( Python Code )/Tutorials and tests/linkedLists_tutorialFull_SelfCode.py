import random
import pprint
import sys

sys.setrecursionlimit(pow(10, 5))

class QuickSort(object):
    def __init__(self, target):
        # The "target" is an unsorted list
        self.target = target
    def getMedianIndex(self, arr, low, high):
        if len(arr) >= 3:
            medianList = [ arr[low], arr[ (low + high) // 2 ], arr[high] ]
            medianList.sort()

            return arr.index(medianList[1])
        else:
            return random.randint(low, high)
    def partition(self, low, high):
        # Get pivot index and pivot value
        pivotIndex = self.getMedianIndex(self.target, low, high) 
        pivot = self.target[pivotIndex]

        # Swap pivot with last element
        self.target[high], self.target[pivotIndex] = self.target[pivotIndex], self.target[high] 
        
        # Update pivot index
        pivotIndex = high
        
        # Scan ( j ) and memory value ( i )
        i = low - 1
        j = low

        while j < high:
            if self.target[j] < pivot:
                # Increment and swap
                i += 1

                self.target[j], self.target[i] = self.target[i], self.target[j] 

            j += 1

        # Swap i+1 with pivot 
        self.target[i+1], self.target[pivotIndex] = self.target[pivotIndex], self.target[i+1]

        # Return i + 1 as partition border splitter
        return i + 1
    def quickSort(self, low, high):
        # BASE CASE < - > RECURSIVE CASE
        if low < high:
            borderIndex = self.partition(low, high)

            self.quickSort(low, borderIndex - 1)
            self.quickSort(borderIndex + 1, high)

        # BASE CASE < - > RECURSIVE CASE
'''
x = list(range(1, 10001))[::-1]
pprint.pprint(x, indent = 20)
newQuickSort = QuickSort(x)
newQuickSort.quickSort(0, len(x) - 1)
pprint.pprint(x, indent = 20)
'''

for i in range(10):
    print()

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

        self.length = 0
        self.cur_node = self.head

    def printOutNextNodes(self):
        currentNode = self.head
        
        for i in range(2):
            print()

        while currentNode:
            x = None
            if currentNode.next:
                x = currentNode.next.data
            print("{0} < - > {1}".format(currentNode.data, x))

            currentNode = currentNode.next

        for i in range(2):
            print()

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def calculateLength_iter(self):
        c = 0
        cur_node = self.head
        while cur_node:
            c += 1 
            cur_node = cur_node.next

        return c
    
    def len_iterative(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count
    
    def len_recursive(self, node):
        if node == None:
            return 0
        return 1 + self.len_recursive(node.next) 

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        
        last_node = self.head
        
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        return
    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def insert_after_node(self, prev_node, data):
        '''
        nodeFound = False

        previousNode = None
        currentNode = self.head

        while currentNode != None: 
            if currentNode.data == prev_node.data:
                nodeFound = True
                break

            if previousNode == None:
                previousNode = self.head
            else:
                previousNode = previousNode.next

            currentNode = currentNode.next
        if not nodeFound:
            print("Node not found")
            return
        else:
            if currentNode.next == None:
                self.append(data)
            if previousNode == None:
                newNode = Node(data)
                afterHead = self.head.next

                self.head.next = newNode
                newNode.next = afterHead
            else:
                newNode = Node(data)
                afterNode = currentNode.next
                
                currentNode.next = newNode
                newNode.next = afterNode
        '''
        
        if not prev_node:
            print("Previous node not in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        '''
        if key == self.head:
            self.head = self.head.next
        '''

        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
      
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None
    '''
    def deleteNodeAtIndex(self, index):
        if index == 0:
            self.head = self.head.next
            return
        else:
            previousNode = None
            currentNode = self.head
            nodeIndexTracker = 0

            while nodeIndexTracker != index:
                previousNode = currentNode
                currentNode = currentNode.next
                nodeIndexTracker += 1
            
            if currentNode.next == None:
                previousNode.next = None
            else:
                previousNode.next = currentNode.next
                currentNode = None
    '''
    def delete_node_at_pos(self, pos):
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next

            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def SwapNodes_MyCode(self, node1, node2):
        if node1 and node2:
            temp = node2.data
            node2.data = node1.data
            node1.data = temp
        else:
            raise Exception("Wrong nodes")
    def swap_nodes(self, key_1, key_2):
        print("Head : {0}".format(self.head.data))
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head

        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
    
        if not curr_1 or not curr_2:
            return
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next
    def swap_nodes_2(self, nodeKey1, nodeKey2):
        if nodeKey1 == nodeKey2:
            return
    
        prevNode_1 = None
        prevNode_2 = None
        currentNode_1 = self.head
        currentNode_2 = self.head 


        if currentNode_1.data == nodeKey1:
            currentNode_1 = self.head 
            node_1_Found = True
        if currentNode_2.data == nodeKey2:
            currentNode_2 = self.head
            node_2_Found = True
   
        while currentNode_1.data != nodeKey1 and currentNode_1:
            prevNode_1 = currentNode_1
            currentNode_1 = currentNode_1.next

            node_1_Found = True
        while currentNode_2.data != nodeKey2 and currentNode_2:
            prevNode_2 = currentNode_2
            currentNode_2 = currentNode_2.next

            node_2_Found = True

        if currentNode_1 and currentNode_2:
            if prevNode_1:
                prevNode_1.next = currentNode_2
            else:
                self.head = currentNode_2

            if prevNode_2:
                prevNode_2.next = currentNode_1
            else:
                self.head = currentNode_1 
            
            currentNode_1.next, currentNode_2.next = currentNode_2.next, currentNode_1.next
        else:
            raise Exception("Key nodes not found. Try again !")

    def printSwapNodes(self, nodeBeforeTarget1, targetNode1, nodeAfterTarget1, nodeBeforeTarget2, targetNode2, nodeAfterTarget2):
            for i in range(3):
                print()

            print("<nodes>")

            if nodeBeforeTarget1:
                print("nodeBeforeTarget1 : {0}".format(nodeBeforeTarget1.data))
            if targetNode1:
                print("*targetNode1*     : {0}".format(targetNode1.data))
            if nodeAfterTarget1:
                print("nodeAfterTarget1  : {0}".format(nodeAfterTarget1.data))
            
            print()

            if nodeBeforeTarget2:
                print("nodeBeforeTarget2 : {0}".format(nodeBeforeTarget2.data))
            if targetNode2:
                print("*targetNode2*     : {0}".format(targetNode2.data))
            if nodeAfterTarget2:
                print("nodeAfterTarget2  : {0}".format(nodeAfterTarget2.data)) 

            print("</nodes>")
            for i in range(3):
                print()
    def _MyCode(self):
        newLList = LinkedList()

        currentNode = self.head
        while currentNode:
            newLList.prepend(currentNode.data)
            currentNode = currentNode.next

        currentNode = self.head
        swapCurrentNode = newLList.head
        while currentNode and swapCurrentNode:
            currentNode.data = swapCurrentNode.data
            currentNode = currentNode.next 
            swapCurrentNode = swapCurrentNode.next
        
    # A -> B -> C -> D -> 0
    # D -> C -> B -> A -> 0
    # A <- B <- C <- D <- 0

    def _iterative(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
        
        self.head = prev 
    def _recursive(self):
        def __recursive(cur, prev):
            if not cur:
                return prev
                
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

            return __recursive(cur, prev)

        self.head = __recursive(cur = self.head, prev = None)
    def _2(self):
        prev = None
        current = self.head

        while current:
            temp = current.next
            prevTemp = current

            current.next = prev

            current = temp
            prev = prevTemp

        self.head = prev
    def _Recursive_2(self):
        def Recursive(prev, current):
            # BASE CASE

            if not current:
                return prev

            # BASE CASE

            # RECURSIVE CASE 
            
            tempCurrent = current
            tempCurrentNext = current.next

            current.next = prev

            prev = tempCurrent
            current = tempCurrentNext

            return Recursive(prev, current)

            # RECURSIVE CASE 
        
        self.head = Recursive(prev = None, current = self.head) 
    def mergeWith_WithQuickSort_MyCode(self, newLList):
        nodesData = list()

        current = self.head
        while current:
            nodesData.append(current.data)
            current = current.next

        current = newLList.head
        while current:
            nodesData.append(current.data)
            current = current.next
        
        newQuickSort = QuickSort(nodesData)
        newQuickSort.quickSort(0, len(nodesData) - 1)

        self.head = Node(nodesData[0])
        current = self.head 
        for element in nodesData[1:]:
            current.next = Node(element)
            current = current.next
    def mergeWith_Iterative_MyCode(self, newLList):
        currentNode = self.head
        currentNode_merge = newLList.head

        while currentNode and currentNode_merge:
            temp = currentNode.next
            temp2 = currentNode_merge.next

            currentNode.next = currentNode_merge
            currentNode.next.next = temp

            currentNode = currentNode.next
            currentNode_merge = temp2
    def mergeCode_TutorialTry(self, newLList):
        P = self.head
        Q = newLList.head

        S = self 

        current = self.head

        nextP = self.head
        nextQ = newLList.head

        while current:
            for i in range(5):
                print()

            print("NEW SECTION --> ")
            inUse = False
            if nextP:
                nextP = nextP.next
                if nextP and P:
                    print("nextP : {0} // P : {0}".format(nextP.data, P.data))
            if nextQ:
                nextQ = nextQ.next
                if nextQ and Q:
                    print("nextQ : {0} // Q : {0}".format(nextQ.data, Q.data)) 
            '''
            if nextP:
                print("nextP : {0}".format(nextP.data))
            else:
                print("nextP : {0}".format(nextP))

            if nextQ:
                print("nextQ : {0}".format(nextQ.data))
            else:
                print("nextQ : {0}".format(nextQ))
            '''

            '''
            if P:
                print("P : {0}".format(P.data))
            else:
                print("Q : {0}".format(P)) 

            if Q:
                print("Q : {0}".format(Q.data))
            else:
                print("Q : {0}".format(Q))
            '''

            if P and Q and P.next: 
                for i in range(2):
                    print()
                
                print("FIRST BLOCK -- > ")
                print("P.data < Q.data and Q.data < P.next.data") 

                if P:
                    print("P : {0}".format(P.data))
                else:
                    print("Q : {0}".format(P)) 

                if Q:
                    print("Q : {0}".format(Q.data))
                else:
                    print("Q : {0}".format(Q))

                if P.next:
                    print("P.next : {0}".format(P.next.data))
                else:
                    print("P.next : {0}".format(P.next))


                if P.data < Q.data and Q.data < P.next.data:
                    current.next = Q
                    
                    if Q:
                        print("current.next = Q ( {0} )".format(Q.data))
                    else:
                        print("current.next = Q ( {0} )".format(Q))
                    
                    P = nextP

                    inUse = True
                    S = newLList
                    print("True")
                else:
                    print("False")

                if S == self:
                    print("S == > self")
                elif S == newLList:
                    print("S == > newLList")

                print("FIRST BLOCK -- < ")

                for i in range(2):
                    print()                

            if P and Q and Q.next and not inUse:
                for i in range(2):
                    print()
                
                print("SECOND BLOCK -- > ")
                print("Q.data < P.data and P.data < Q.next.data")

                if P:
                    print("P : {0}".format(P.data))
                else:
                    print("Q : {0}".format(P)) 

                if Q:
                    print("Q : {0}".format(Q.data))
                else:
                    print("Q : {0}".format(Q))

                if Q.next:
                    print("Q.next : {0}".format(Q.next.data))
                else:
                    print("Q.next : {0}".format(Q.next))

               
                if Q.data < P.data and P.data < Q.next.data:
                    current.next = P

                    if P:
                        print("current.next = P ( {0} )".format(P.data))
                    else:
                        print("current.next = P ( {0} )".format(P))

                    Q = nextQ

                    inUse = True
                    S = self
                    print("True")
                else:
                    print("False")

                if S == self:
                    print("S == > self")
                elif S == newLList:
                    print("S == > newLList")
                
                print("SECOND BLOCK -- < ")

                for i in range(2):
                    print()

            if not inUse:
                print("NOT IN USE.") 
                
                if S == self:
                    print("S == > self")
                elif S == newLList:
                    print("S == > newLList")
               

                if S == newLList:
                    current.next = Q
                    Q = nextQ

                    if Q:
                        print("current.next = Q ( {0} )".format(Q.data))
                    else:
                        print("current.next = Q ( {0} )".format(Q))
                elif S == self:
                    current.next = P
                    P = nextP
                    
                    if P:
                        print("current.next = P ( {0} )".format(P.data))
                    else:
                        print("current.next = P ( {0} )".format(P))
                    
            current = current.next
        
            for i in range(2):
                print()

            print("NEW SECTION -- < ")

            for i in range(5):
                print()
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p 
    def merge_again(self, llist):
        dummyNode = None

        # P == > main pointer to ( self )
        # Q == > pointer to merge list  ( llist )

        P = self.head
        Q = llist.head

        if P.data < Q.data:
            dummyNode = self.head
            P = P.next
        else:
            dummyNode = llist.head
            Q = Q.next

        while P and Q:
            if dummyNode.data < Q.data and Q.data < P.data:
                # dummyNode point to Q
                dummyNode.next = Q
                
                # Update q
                Q = Q.next
            elif dummyNode.data < P.data and P.data < Q.data:
                # dummyNode point to P
                dummyNode.next = P

                # Update p
                P = P.next

            # Update dummyNode
            dummyNode = dummyNode.next

        if not P:
            dummyNode.next = Q
        if not Q:
            dummyNode.next = P
    def remove_duplicates_MyCode(self):
        duplicates = list()
        current = self.head
        while current:
            if current.data not in duplicates:
                duplicates.append(current.data)

            current = current.next

        current = self.head 
        for element in duplicates[1:]:
            current.next = Node(element)
            current = current.next

        current.next = None
    def remove_duplicates_AgainTry_MyCode(self):
        currentNode = self.head
        nodesData = [currentNode.data]
        notDuplicateNodes = [currentNode] 

        while currentNode:
            if currentNode.data not in nodesData:
                nodesData.append(currentNode.data)
                notDuplicateNodes.append(currentNode)

            currentNode = currentNode.next

        current = self.head
        nodeChain = notDuplicateNodes[0] 
        for node in notDuplicateNodes[1:]:
            nodeChain.next = Node(node.data) 
            nodeChain = nodeChain.next
    def removeDuplicates_Try3_MyCode(self):
        trackNode = self.head
        nodeDataMemory = [trackNode.data]
        current = self.head.next

        while current:
            temp = current.next
            if current.data not in nodeDataMemory:
                nodeDataMemory.append(current.data)
                trackNode.next = Node(current.data)
                trackNode = trackNode.next
            else:
                current = None

            current = temp 
    def removeDuplicate_TutorialCode(self):
        cur = self.head
        prev = None

        dup_values = dict()

        while cur:
            # If it's in dict.
            if cur.data in dup_values.keys():
                # Remove
                prev.next = cur.next
                cur = None
            else:
                # Add to dict
                dup_values.setdefault(cur.data, 1)
                prev = cur

            cur = prev.next 
    def indexOf(self, key):
        indexTrack = 0 
        current = self.head

        while current:
            if current.data == key:
                return indexTrack

            indexTrack += 1
            current = current.next

        return None
    def nth(self, i):
        n = 0
        current = self.head

        while current:
            if n == i:
                return current
            n += 1
            current = current.next
        return None
    def print_nth_from_last(self, n):
        '''
        # Method 1:
        total_len = self.len_iterative()
        cur = self.head

        while cur:
            if total_len == n:
                print(cur.data)
                return cur
            total_len -= 1
            cur = cur.next
        
        if cur is None:
            return
        
        '''

        # Method 2:
        p = self.head
        q = self.head
        
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        
        if not q:
            print("{0} is greater than the number of nodes in list".format(n))
            return
        
        while p and q:
            p = p.next
            q = q.next

        return p.data
    def count_Element_iterative_MyCode(self, key):
        counter = 0
        current = self.head

        while current:
            if current.data == key:
                counter += 1

            current = current.next

        return counter
    def count_Element_recursive_MyCode(self, key):
        def recursiveALG(node, counter):
            if node:
                if node.data == key:
                    counter += 1
                return recursiveALG(node.next, counter)
            else: 
                return counter
    
        return recursiveALG(self.head, 0)
    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next

        return count
    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return 0 + self.count_occurences_recursive(node.next, data)
    def rotate_MyCode(self, rotationValue):
        lastNodeBeforeRotation = None
        firstNodeAfterRotationValue = None
        lastNode = None

        prev = None
        current = self.head
        counter = 1
        
        while current:
            if counter == rotationValue:
                lastNodeBeforeRotation = current
                firstNodeAfterRotationValue = lastNodeBeforeRotation.next
                
            prev = current
            current = current.next
            counter += 1

        lastNode = prev 

        lastNode.next = self.head
        lastNodeBeforeRotation.next = None
        self.head = firstNodeAfterRotationValue
    def rotate(self, k):
        p = self.head
        q = self.head

        prev = None
        count = 0

        while p and count < k:
            prev = p

            p = p.next
            q = q.next

            count += 1

        p = prev

        while q:
            prev = q
            q = q.next

        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None
    def isPalindrome_MyCode(self):
        nodeString = str()
        current = self.head

        while current:
            nodeString += str(current.data)
            current = current.next

        return nodeString == nodeString[::-1]
    def is_palindrome(self):
        '''
        # Method 1:
        s = ""
        p = self.head

        while p:
            s += str(p.data)
            p = p.next
        
        return s == s[::-1]
        '''

        '''
        # Method 2:
        p = self.head
        s = []

        while p:
            s.append(p.data)
            p = p.next
   
        p = self.head

        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True
        '''

        # Method 3:
        p = self.head
        q = self.head
        prev = []

        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1

        q = prev[i-1]
        
        count = 1
        while count <= i // 2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1

        return True
    def tailToHead_MyCode(self):
        lastNode = None
        nodeBeforeLastNode = None

        prevPrev = None
        prev = None
        current = self.head

        while current:
            prevPrev = prev
            prev = current
            current = current.next

        lastNode = prev
        nodeBeforeLastNode = prevPrev

        lastNode.next = self.head
        nodeBeforeLastNode.next = None
        self.head = lastNode
    def tailToHead_tutorial(self):
        last = self.head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next

        second_to_last.next = None
        last.next = self.head
        self.head = last
    def sum_llist_myCode(self, llist):
        self.sum = str()
        llist_sum = str()

        current = self.head
        while current:
            self.sum += str(current.data)
            current = current.next

        current = llist.head
        while current:
            llist_sum += str(current.data)
            current = current.next

        for i in range(2):
            print()

        return eval(self.sum[::-1]) + eval(llist_sum[::-1])
    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head

        sum_llist = LinkedList()
        carry = 0

        while p or q:
            if not p:
                i = 0
            else:
                i = p.data

            if not q:
                j = 0
            else:
                j = q.data


            s = i + j + carry

            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            
            if p:
                p = p.next
            if q:
                q = q.next


        
'''
llist_1= LinkedList()
llist_elements = [1, 5, 7, 9, 10]

for element in llist_elements:
    llist_1.append(element)

llist_2 = LinkedList()
newLList_elements = [2, 3, 4, 6, 8]
for element in newLList_elements:
    llist_2.append(element)
'''
    
llist_1 = LinkedList()
llist_1_elements = [5, 6, 3] 

llist_2 = LinkedList()
llist_2_elements = [8, 4, 2]

for element in llist_1_elements:
    llist_1.append(element)

for element in llist_2_elements:
    llist_2.append(element)

# MERGED == > [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(5):
    print()
print("START LINKED LIST : ")

print(llist_1.sum_llist_myCode(llist_2))

for i in range(5):
    print()

# llist.mergeWith_Iterative_MyCode(newLList)
# llist.mergeCode_TutorialTry(newLList)
# llist_1.merge_again(llist_2)
# llist_1.removeDuplicates_Try3_MyCode()
# print(llist_1.count_occurences_recursive(llist_1.head, 1))
# llist_1.rotate(4)
# print(llist_1.is_palindrome())
# print(llist_1.tailToHead_tutorial())

print(llist_1.sum_two_lists(llist_2))

for i in range(5):
    print()

print("END LINKED LIST : ")

llist_1.print_list()
