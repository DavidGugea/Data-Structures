import random
import pprint
import itertools

class QuickSort(object):
    def medianOfThree(self, arr, low, high):
        if len(arr) >= 3:
            # Get the first, middle & last element
            start_middle_end = [ arr[ low ], arr[ ( low + high ) // 2 ], arr[ high ] ]

            # Sort the values
            start_middle_end.sort()

            # Return the index of the middle element
            return arr.index(start_middle_end[1])
        else:
            return random.randint(low, high)
    def partition(self, arr, low, high):
        # Get the partition index using the median of three strategy 
        pivotIndex = self.medianOfThree(arr, low, high) 
        pivot = arr[pivotIndex]

        # Get the pivot to the end of the array to get it from our way
        arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]

        # Update the pivot index
        pivotIndex = high

        # Create two pointers that will iterate over the list and scan it
        LP = low        # Scans and swaps values that are > pivot
        RP = high - 1   # Scans and swaps values that are < pivot

        # Iterate using the pointers
        while LP <= RP:
            if arr[LP] > pivot and arr[RP] < pivot:
                # Swap the data at the pointers
                arr[LP], arr[RP] = arr[RP], arr[LP]
                
                # Increment the value of the left pointer
                LP += 1

                # Decrement the value of the right pointer
                RP -= 1
            else:
                if arr[LP] < pivot:
                    # Increment the value of the left pointer
                    LP += 1

                if arr[RP] > pivot:
                    # Decrement the value of the right pointer
                    RP -= 1

        # Swap the pivot with its place
        arr[pivotIndex], arr[LP] = arr[LP], arr[pivotIndex]

        # Update the pivot index
        pivotIndex = LP

        # Return the border split value
        return pivotIndex
    def quickSort(self, arr, low, high):
        if low <= high:
            # Get the partiton border split index & quick sort both halves of the remaining array 
            partitionBorderIndex = self.partition(arr, low, high)

            # Quick sort both halves
            self.quickSort(arr, low, partitionBorderIndex - 1)
            self.quickSort(arr, partitionBorderIndex + 1, high)
    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)

class Stack(object):
    def __init__(self):
        self.items = list()

        '''
        ~ Description ( how the method looks ) -> return value [ done (x) / undone ( empty ) ]
        
        ##################################### GENERAL METHODS #############################################

        ~ Get length                                ( self.getLength() )                -> Number            [x]
        ~ Create __len__(self) method               ( len(self) )                       -> Number            [x] 

        ~ Value at index                            ( self.atIndex(index) )             -> Item              [x]     
        ~ Get all stack items                       ( self.get_stack() )                -> list              [x]
        
        ~ Get item in the middle                    ( self.getMiddle() )                -> Item              [x]

        ##################################### GENERAL METHODS #############################################

        ##################################### Basic Stack methods #########################################
      
        ~ Add something to the stack                ( self.push(item) )                 -> None              [x]
        ~ Delete the item at the top of the stack   ( self.pop()      )                 -> None              [x]
            
        ~ Check if the stack is empty               ( self.is_empty() )                 -> True/False        [x]
        ~ Get the last item at the top of the stack ( self.peek()     )                 -> Item              [x]
        
        ###################################### Basic Stack methods #########################################

        ######################################### OTHERS ###################################################

        ~ Insert after item                         ( self.insertAfterItem(data, item)      )   -> None              [x]
        ~ Insert at index                           ( self.insertAtIndex(index, item)       )   -> None              [x]
        
        ~ Delete at index                           ( self.deleteAtIndex(index)             )   -> None              [x]
        ~ Delete item with data                     ( self.deleteItemWithData(data)         )   -> None              [x]

        ~ Swap                                      ( self.swap(index1, index2)             )   -> None              [x]
        
        ~ Reverse                                   ( self.reverse()                        )   -> None              [x]
        
        ~ Merge two stacks                          ( self.basicMerge(merge_stack)          )   -> None              [x]
        ~ Merge two stacks in sorted order          ( self.sortedMerge(merge_stack)         )   -> None              [x]

        ~ Remove duplicates                         ( self.removeDuplicates()               )   -> None              [x]
        ~ Rotate                                    ( self.rotate(rotation_value)           )   -> None              [x]

        ~ Is palindrome                             ( self.isPalindrome()                   )   -> True/False        [x]

        ~ Move tail to head                         ( self.moveTailToHead()                 )   -> None              [x]
        ~ Sum with another stack DS                 ( self.sumWith(sum_stack)               )   -> None              [x]

        ~ Split stack in half                       ( self.splitInHalf()                    )   -> [stack1, stack2]  [x]
        ~ Split at index                            ( self.splitAtIndex(index)              )   -> [stack1, stack2]  [x]

        ~ Pairs with sum                            ( self.pairsWithSum(sum_value)          )   -> [ (), (), .. () ] [x]

        ~ Reverse a string using the stack          ( self.reverseString(givenString)       )   -> string            [x]
        ~ Convert integer to binary using the stack ( self.convertIntegerToBinary(integer)  )   -> string            [x] 
        ~ Check paranthesis string using the stack  ( self.checkParanthesis(givenString)    )   -> string            [x]

        ######################################### OTHERS ###################################################
       
        '''

    ##################################### GENERAL METHODS ##############################################
    
    def getLength(self):
        return len(self.items)

    def __len__(self):
        return len(self.items)

    def atIndex(self, index):
        return self.items[index]

    def get_stack(self):
        return self.items

    def getMiddle():
        return self.items[ len(self.items) // 2 ]

    ##################################### GENERAL METHODS ##############################################

    ###################################### Basic Stack methods #########################################

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    ###################################### Basic Stack methods #########################################

    ######################################### OTHERS ###################################################

    def insertAfterItem(self, data, item):
        self.items.insert(self.items.index(item)+1, data)

    def insertAtIndex(self, index, item):
        # Check the index
        if index >= len(self.items) or index < 0:
            raise IndexError("The given index is either too big for the stack or to small. ( < 0 )") 

        self.items.insert(index, item)

    def deleteAtIndex(self, index):
        # Check the index
        if index >= len(self.items) or index < 0:
            raise IndexError("The given index is either too big for the stack or to small. ( < 0 )") 

        del self.items[index]

    def deleteItemWithData(self, data):
        del self.items[ self.items.index(data) ]

    def swap(self, index1, index2):
        # Check the indexes
        if index1 >= len(self.items) or index2 >= len(self.items) or index1 < 0 or index2 < 0:
            raise IndexError("The given indexes are either too big for the stack or to small ( < 0 )")

        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def reverse(self):
        self.items = self.items[::-1]

    def basicMerge(self, merge_stack):
        self.items.extend(merge_stack.get_stack())

    def sortedMerge(self, merge_stack):
        # Merge the current items with the new merge_stack items and after that sort them using quick sort
        self.items.extend(merge_stack.get_stack())
        
        # Sort the items using quick sort
        q = QuickSort()
        q.sort(self.items)

    def removeDuplicates(self):
        self.items = list(set(self.items))
        
    def rotate(self, rotation_value):
        # Example :
        # stack = > [10, 20, 30, 40, 50, 60]
        # rotation_value = 4
        # stack after rotation => [50, 60, 10, 20, 30, 40]
        
        insertItems = self.items[rotation_value:]
        del self.items[rotation_value:]
        
        for item in insertItems[::-1]:
            self.items.insert(0, item)
            
    def isPalindrome(self):
        # Get all items into a string and see if it's the same upside down
        itemData = "".join(self.items)
        return itemData == itemData[::-1]
    
    def moveTailToHead(self):
        # Example:
        # stack => ["A", "B", "C", "D", "E", "F"]
        # After 'moving the tail to the head'
        # stack => ["F", "A", "B", "C", "D", "E"]
        
        self.items.insert(0, self.items.pop())
    
    def sumWith(self, sum_value):
        # Create a 'pairs' list where you put all the pairs that match the value
        pairs = list()
        
        # For all the pairs that match the sum and that are not in the 'pairs' variable even if we change their order ([::-1]), add them in the 'pairs' list
        for permutation in itertools.permutations(self.items, 2):
            if tuple(permutation) not in pairs and tuple(permutation[::-1]) not in pairs and sum(list(permutation)) == sum_value:
                pairs.append(tuple(permutation))
                
        # Return the pairs that summed have the given value
        return pairs

    def splitInHalf(self):
        return [ self.items[:len(self.items) // 2], self.items[len(self.items) // 2:] ]

    def splitAtIndex(self, index):
        return [ self.items[:index], self.items[index:] ]

    def pairsWithSum(self, sum_value):
        pairs = list()
        for permutation in itertools.permutations(self.items, 2):
            if sum(list(permutation)) == sum_value and tuple(permutation) not in pairs and tuple(permutation[::-1]) not in pairs:
                pairs.append(tuple(permutation))

        return pairs

    def reverseString(self, givenString):
        # Create a special stack for the given string
        stringStack = Stack()
        
        for char in givenString:
            stringStack.push(char)
            
        reversedString = str()
        
        while not stringStack.is_empty():
            reversedString += stringStack.pop()
        
        return reversedString
    
    def convertIntegerToBinary(self, integer):
        binaryStack = Stack()
        
        while integer > 0:
            binaryStack.push(str(integer % 2))
            integer //= 2
            
        return "".join(binaryStack.get_stack()[::-1])
    
    def checkParanthesis(self, givenString):
        # Create a stack that will have all the chars that the upside given string has and then the track list, that keep track of opened paranthesis
        mainTrack = Stack()
        track = list()
        
        # Add all the chars of the upside given string in the main stack
        for char in givenString[::-1]:
            mainTrack.push(char)
            
        # Create two lists that define what "opened" & "closed" paranthesis mean
        opened = [ "{", "[", "(" ]
        closed = [ "}", "]", ")" ]
    
        # Iterate over the entire stack
        while not mainTrack.is_empty():
            if mainTrack.peek() in opened:
                # If we have an opened paranthesis we must add it to the track, and delete it after that from the mainTrack
                track.append(mainTrack.peek())
                mainTrack.pop()
            elif mainTrack.peek() in closed and track:
                # Check if the paranthesis is closed and the track list exists, because there is also the case where the string can start like this : ']...', which, if it does, it can't be a valid paranthesis string anymore because it started with a closed paranthesis, so also because of that our 'track' list is empty, so this part of the code won't execute, and on the next one, on 'else' we will just return False.
                # Because this is a closed paranthesis, and we know that we already have some opened paranthesis because 'track' is not empty, we will have to check if the paranthesis that we have know, matches the last opened paranthesis that we had back in the string
                paranthesis = mainTrack.peek()
                
                if ( track[-1] == "{" and paranthesis != "}" ) or ( track[-1] == "[" and paranthesis != "]" ) or ( track[-1] == "(" and paranthesis != ")" ):
                    return False # the paranthesis don't match, so return False
                else:
                    mainTrack.pop()
                    del track[-1]
            else:
                return False

        if not track:
            return True # Return true, because we are sure that there are no opened paranthesis opened & also sure that there are no closed paranthesis opened ( from the loop )
        else:
            return False
                
    ######################################### OTHERS ###################################################
