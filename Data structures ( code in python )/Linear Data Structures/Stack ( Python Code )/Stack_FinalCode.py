import random
import pprint

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
            
x = list(range(1, 11))[::-1]
pprint.pprint(x, indent = 20)
q = QuickSort()
q.quickSort(x, 0, len(x) - 1)
pprint.pprint(x, indent = 20)

class Stack(object):
    def __init__(self):
        self.items = list()

        '''
        ~ Description ( how the method looks ) -> return value [ done (x) / undone ( empty ) ]
        
        ##################################### GENERAL METHODS #############################################

        ~ Get length                                ( self.getLength() )                -> Number            []
        ~ Create __len__(self) method               ( len(self) )                       -> Number            [] 

        ~ Value at index                            ( self.atIndex(index) )             -> Item              []     
        ~ Get all stack items                       ( self.get_stack() )                -> list              []
        
        ~ Get item in the middle                    ( self.getMiddle() )                -> Item              []

        ##################################### GENERAL METHODS #############################################

        ##################################### Basic Stack methods #########################################
      
        ~ Add something to the stack                ( self.push(item) )                 -> None              []
        ~ Delete the item at the top of the stack   ( self.pop()      )                 -> None              []
            
        ~ Check if the stack is empty               ( self.is_empty() )                 -> True/False        []
        ~ Get the last item at the top of the stack ( self.peek()     )                 -> Item              []
        
        ###################################### Basic Stack methods #########################################

        ######################################### OTHERS ###################################################

        ~ Insert after item                         ( self.insertAfterItem(item)            )   -> None              []
        ~ Insert at index                           ( self.insertAtIndex(index, item)       )   -> None              []
        
        ~ Delete at index                           ( self.deleteAtIndex(index)             )   -> None              []
        ~ Delete item with data                     ( self.deleteItemWithData(data)         )   -> None              []

        ~ Swap                                      ( self.swap(index1, index2)             )   -> None              []
        
        ~ Reverse                                   ( self.reverse()                        )   -> None              []
        
        ~ Merge two stacks                          ( self.basicMerge(merge_stack)          )   -> None              []
        ~ Merge two stacks in sorted order          ( self.sortedMerge(merge_stack)         )   -> None              []

        ~ Remove duplicates                         ( self.removeDuplicates()               )   -> None              []
        ~ Rotate                                    ( self.rotate(rotation_value)           )   -> None              []

        ~ Is palindrome                             ( self.isPalindrome()                   )   -> True/False        []

        ~ Move tail to head                         ( self.moveTailToHead()                 )   -> None              []
        ~ Sum with another stack DS                 ( self.sumWith(sum_stack)               )   -> None              []

        ~ Split stack in half                       ( self.splitInHalf()                    )   -> [stack1, stack2]  []
        ~ Split at index                            ( self.splitAtIndex(index)              )   -> [stack1, stack2]  []

        ~ Pairs with sum                            ( self.pairsWithSum(sum_value)          )   -> [ (), (), .. () ] []

        ~ Reverse a string using the stack          ( self.reverseString(givenString)       )   -> string            []
        ~ Convert integer to binary using the stack ( self.convertIntegerToBinary(integer)  )   -> string            [] 
        ~ Check paranthesis string using the stack  ( self.checkParanthesis(givenString)    )   -> string            []

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

        def insertAfterItem(self, item):
            self.items.insert(self.items.index(item)+1, item)

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

        def swap(index1, index2):
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
                    
        ######################################### OTHERS ###################################################
