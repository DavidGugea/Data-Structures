import random
import itertools

class QuickSort(object):
    def partition(self, arr, low, high):
        # Get the pivot index & pivot value
        pivotIndex = random.randint(low, high)
        pivot = arr[pivotIndex]

        # Swap the pivot with the last element from the list to get it from our way
        arr[high], arr[pivotIndex] = arr[pivotIndex], arr[high]

        # Update the pivot index
        pivotIndex = high

        # Create two pointers that will scan the entire list and find a positon for the pivot while swapping elements that are not in the right order
        LP = low      # Left pointer  ( swaps > pivot vars. )
        RP = high - 1 # Right pointer ( swaps < pivot vars. )

        # Scan the array & swap the values to find a place for the pivot
        while LP <= RP:
            if arr[LP] > pivot and arr[RP] < pivot:
                # Swap
                arr[LP], arr[RP] = arr[RP], arr[LP]

                # Increment left scan value
                LP += 1

                # Decrement right scan value
                RP -= 1
            
            if arr[LP] < pivot:
                # Increment left scan value
                LP += 1

            if arr[RP] > pivot:
                # Decrement right scan value
                RP -= 1

        # Swap the pivot with the left scan value 
        arr[LP], arr[pivotIndex] = arr[pivotIndex], arr[LP]

        # Update the pivot index
        pivotIndex = LP

        # Return the pivot index
        return pivotIndex
    def quickSort(self, arr, low, high):
        if low < high:
            # Get the index where we have to split the list in half 
            partitionIndexSplit = self.partition(arr, low, high)

            # Quick sort both halves
            self.quickSort(arr, low, partitionIndexSplit - 1)
            self.quickSort(arr, partitionIndexSplit + 1, high)
    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)

class Queue(object):
    def __init__(self):
        self.items = list()

        self.rear = None
        self.front = None

        '''
        ~ Description ( how the method looks ) -> return value [ done (x) / undone ( empty ) ]
        
        ##################################### GENERAL METHODS #############################################

        ~ Get length                                ( self.getLength() )                -> Number            [x]
        ~ Create __len__(self) method               ( len(self) )                       -> Number            [x] 

        ~ Value at index                            ( self.atIndex(index) )             -> Item              [x]     
        ~ Get all queue items                       ( self.get_queue() )                -> list              [x]
        
        ~ Get item in the middle                    ( self.getMiddle() )                -> Item              [x]

        ##################################### GENERAL METHODS #############################################

        ##################################### Basic Stack methods #########################################
      
        ~ Add something to the queue                ( self.enqueue(item) )              -> None              [x]
        ~ Dequeue from queue( delete first item )   ( self.dequeue()  )                 -> None              [x]
        ~ Check if the queue is empty               ( self.is_empty() )                 -> True/False        [x]

        ~ Get the first item of the queue           ( self.getFront() )                 -> item              [x]
        ~ Get the last item of the queue            ( self.getRear()  )                 -> item              [x]
        
        ###################################### Basic Stack methods #########################################

        ######################################### OTHERS ###################################################

        ~ Insert after item                         ( self.insertAfterItem(data, item, startIndex = 0)      )   -> None              [x]
        ~ Insert at index                           ( self.insertAtIndex(index, item, startIndex = 0)       )   -> None              [x]
        
        ~ Delete at index                           ( self.deleteAtIndex(index)                             )   -> None              [x]
        ~ Delete item with data                     ( self.deleteItemWithData(data, startIndex = 0)         )   -> None              [x]

        ~ Swap                                      ( self.swap(index1, index2)                             )   -> None              [x]
        
        ~ Reverse                                   ( self.reverse()                                        )   -> None              [x]
        
        ~ Merge two queues                          ( self.basicMerge(merge_queue)                          )   -> None              [x]
        ~ Merge two queues in sorted order          ( self.sortedMerge(merge_queue)                         )   -> None              [x]

        ~ Remove duplicates                         ( self.removeDuplicates()                               )   -> None              [x]
        ~ Rotate                                    ( self.rotate(rotation_value)                           )   -> None              [x]

        ~ Is palindrome                             ( self.isPalindrome()                                   )   -> True/False        [x]

        ~ Move tail to head                         ( self.moveTailToHead()                                 )   -> None              [x]
        ~ Sum with another stack DS                 ( self.sumWith(sum_queue)                               )   -> None              [x]

        ~ Split stack in half                       ( self.splitInHalf()                                    )   -> [queue1, queue2]  [x]
        ~ Split at index                            ( self.splitAtIndex(index)                              )   -> [queue1, queue2]  [x]

        ~ Pairs with sum                            ( self.pairsWithSum(sum_value)                          )   -> [ (), (), .. () ] [x]

        ######################################### OTHERS ###################################################
        '''
    ##################################### GENERAL METHODS #############################################

    def getLength(self):
        return len(self.items)
    
    def __len__(self):
        return len(self.items)

    def atIndex(self, index):
        # Check the index
        if index < 0 or index >= len(self.items):
            raise IndexError("The index given is either too big for the queue or too small ( < 0 )")

        return self.items[index]
    
    def get_queue(self):
        return self.items

    def getMiddle(self):
        # Check if the queue is empty or not
        if not self.items:
            raise ValueError("The given queue is empty. There can't be no item 'in the middle'")

        return self.items[len(self.items) // 2]

    ##################################### GENERAL METHODS #############################################

    ###################################### Basic Stack methods #########################################

    def enqueue(self, item):
        # Add the item at the beginning of the list and change the rear property
        self.items.insert(0, item)
    
        self.front = self.items[-1]
        self.rear = item

    def dequeue(self):
        # Check if the queue is not empty. If it is empty, raise an error, otherwise, delete the last element added in the queue & change the front property 
        if not self.items:
            raise ValueError("The queue is empty, can't delete anything.")

        self.front = self.items[-2]
        del self.items[-1]

    def is_empty(self):
        return not self.items
    
    def getFront(self):
        return self.front

    def getRear(self):
        return self.rear

    ###################################### Basic Stack methods #########################################
    ######################################### OTHERS ###################################################

    def insertAfterItem(self, data, item, startIndex = 0):
        # Check the start index and if the data is or not in the items of the queue 
        if startIndex < 0 or startIndex >= len(self.items):
            raise IndexError("The start index is either too big for the queue or too small ( < 0 ).")
        if data not in self.items:
            raise ValueError("The data that you want to insert the item after in the queue is not in the items of the queue.")

        self.items.insert(self.items.index(data, startIndex) + 1, item)

        # Update rear & front depending on the queue, it might be the case to update them in case that the user inserted an item at the end or front of the list
        self.rear = self.items[0]
        self.front = self.items[-1]
  
    
    def insertAtIndex(self, index, item):
        # Check the index
        if index < 0 or index > len(self.items):
            raise IndexError("The index is either too big for the queue or too small ( < 0 ).")

        self.items.insert(index, item)

        # Update rear & front depending on the queue, it might be the case to update them in case that the user inserted an item at the end or front of the list
        self.rear = self.items[0]
        self.front = self.items[-1]

    def deleteAtIndex(self, index):
        # Check the index
        if index < 0 or index >= len(self.items):
            raise IndexError("The index is either too big for the qeueu or too small ( < 0 ).")

        del self.items[index]

        # Update rear & front depending on the queue, it might be the case to update them in case that the user inserted an item at the end or front of the list
        self.rear = self.items[0]
        self.front = self.items[-1]

    def deleteItemWithData(self, data, startIndex = 0):
        # Check the start index
        if startIndex < 0 or startIndex >= len(self.items):
            raise IndexError("The index is either too big for the queue or too small ( < 0 ).")

        del self.items[self.items.index(data, startIndex)]

        # Update rear & front depending on the queue, it might be the case to update them in case that the user inserted an item at the end or front of the list
        self.rear = self.items[0]
        self.front = self.items[-1]

    def swap(self, index1, index2):
        # Check both indexes
        if index1 < 0 or index2 < 0 or index1 >= len(self.items) or index2 >= len(self.items):
            raise IndexError("The given indexes are either too big for the queue or too small ( < 0 ).")

        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

        self.rear = self.items[0]
        self.front = self.items[-1]
    
    def reverse(self):
        self.items = self.items[::-1]

        self.rear, self.front = self.front, self.rear

    def basicMerge(self, merge_queue):
        # Check the merge_queue 
        if type(merge_queue) != Queue:
            raise ValueError("The given merge queue must be of type queue.")

        self.items += merge_queue.get_queue()

        self.rear = self.items[0]
        self.front = self.items[-1]

    def sortedMerge(self, merge_queue):
        # Add all the items from the merge_queue to the self.items
        self.items.extend(merge_queue.get_queue())
        
        # Sort the items using quick sort
        q = QuickSort()
        q.sort(self.items)

        self.rear = self.items[0]
        self.front = self.items[-1]

    def removeDuplicates(self):
        self.items = list(set(self.items))[::-1]
        
        self.rear = self.items[0]
        self.front = self.items[-1]

    def rotate(self, rotation_value):
        # Check the rotation value
        if rotation_value >= len(self.items):
            raise ValueError("The given rotation value is too big for the queue item list")

        # Example:
        # self.items => [10, 20, 30, 40, 50, 60]
        # rotation_value = 4
        # self.items => [50, 60, 10, 20, 30, 40]
        self.items = self.items[rotation_value:] + self.items[:rotation_value]

        self.rear = self.items[0]
        self.front = self.items[-1]

    def isPalindrome(self):
        # Get the items list in an array and see if it's the same when turned upside down
        return "".join(map(str, self.items)) == "".join(map(str, self.items))[::-1]

    def moveTailToHead(self):
        # Example:
        # self.items => [10, 20, 30, 40, 50, 60]
        # After 'moving the tail to head'
        # self.items => [60, 10, 20, 30, 40, 50]

        self.items[0], self.items[-1] = self.items[-1], self.items[0]
        self.rear, self.front = self.front, self.rear

    def sumWith(self, sum_queue):
        # Example:
        # self.items => [10, 20]
        # sum_queue  => [5]
        # sumWith returns == > 10 + 20 + 5

        return sum(self.items) + sum(sum_queue.get_queue())

    def splitInHalf(self):
        # Example:
        # self.items => [10, 20, 30, 40]
        # splitInHalf returns => [[10, 20], [30, 40]]

        return [ self.items[:len(self.items) // 2], self.items[len(self.items) // 2:] ]

    def splitAtIndex(self, index):
        # Check the index
        if index < 0 or index >= len(self.items):
            raise IndexError("The given index is either too big for the queue or too small ( < 0 ).")

        return [ self.items[:index], self.items[index:] ]

    def pairsWithSum(self, sum_value):
        pairs = list()
        for permutation in itertools.permutations(self.items, 2):
            if sum(list(permutation)) == sum_value and tuple(permutation) not in pairs and tuple(permutation[::-1]) not in pairs:
                pairs.append(tuple(permutation))

        return pairs

    ######################################### OTHERS ###################################################
