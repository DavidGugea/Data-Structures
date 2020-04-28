import pprint
import itertools
import random

class QuickSort(object):
    def partition(self, arr, low, high):
        # Get the pivot index
        pivotIndex = random.randint(low, high)

        # Get the pivot value
        pivot = arr[pivotIndex]

        # Swap the pivot with the last element from the list to get it from our way
        arr[pivotIndex], arr[high] = arr[high], arr[pivotIndex]

        # Update the pivot index
        pivotIndex = high

        # Create two pointers that will scan the list & swap the necessary items
        LP = low        # Left pointer  ( swaps -> var > pivot )
        RP = high - 1   # Right pointer ( swaps -> var < pivot ) 

        # Iterate and swap
        while LP <= RP:
            if arr[LP] > pivot and arr[RP] < pivot:
                # Swap pointer values
                arr[LP], arr[RP] = arr[RP], arr[LP]

                # Increment left pointer
                LP += 1

                # Decrement right pointer
                RP -= 1
            else:
                if arr[LP] < pivot:
                    # Increment the left pointer
                    LP += 1

                if arr[RP] > pivot:
                    # Decrement the right pointer
                    RP -= 1

        # Swap the left pointer with the pivot
        arr[LP], arr[pivotIndex] = arr[pivotIndex], arr[LP]

        # Update the pivot index
        pivotIndex = LP

        # Return the border index value ( pivotIndex )
        return pivotIndex
    def quickSort(self, arr, low, high):
        if low <= high:
            # Get the border index
            borderIndex = self.partition(arr, low, high)

            # Quick sort both halves
            self.quickSort(arr, low, borderIndex - 1)
            self.quickSort(arr, borderIndex + 1, high)
    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)

class NodeBucket(object):
    def __init__(self, capacity = None):
        # Get the capacity of the node bucket, defaults to None
        if type(capacity) != int and capacity != None:
            raise ValueError("The capacity must be None or an integer")
   
        self.capacity = capacity

        # Define bucket items
        self.bucketItems = list()

        # Create the quick sort object to sort the bucket
        self.qs = QuickSort()

        # Create pointer to next bucket
        self.next = None
    
    def getSize(self):
        return len(self.bucketItems)

    def getItems(self):
        return self.bucketItems

    def appendToBucket(self, item):
        # Check if there is a capacity ( if there is, check if the node bucket is full if not, just append the item to the bucket items list )
        if self.capacity:
            if len(self.bucketItems) >= self.capacity:
                raise OverflowError("The node bucket is full. You can't add any items to it anymore.")

        self.bucketItems.append(item)

    def extendBucket(self, extend_list):
        # Check the extend_list 
        if type(extend_list) != list:
            raise ValueError("The extend list must be of type list.")
        
        if self.capacity:
            if len(self.bucketItems) + len(extend_list) > self.capacity:
                raise OverflowError("The node bucket is full.")

        self.bucketItems.extend(extend_list)
    
    def insertInBucket(self, index, item):
        # Check the index
        if not 0 <= index < len(self.bucketItems):
            raise IndexError("The given index is either too big for the node bucket or too small ( < 0 )")

        # Check if the bucket is full or not
        if self.capacity:
            if len(self.bucketItems) >= self.capacity:
                raise OverflowError("The node bucket is full.")

        self.bucketItems.insert(index, item)

    def sortBucket(self):
        self.qs.sort(self.bucketItems)

    def removeDuplicates(self):
        self.bucketItems = list(set(self.bucketItems))

    def rotate(self, rotation_value):
        # Example : 
        # self.bucketItems = [10, 20, 30, 40, 50, 60]
        # rotation_value   = 4
        # After rotation :
        # self.bucketItems = [50, 60, 10, 20, 30, 40]
        self.bucketItems = self.bucketItems[rotation_value:] + self.bucketItems[:rotation_value]

    def isPalindrome(self):
        # Put all the items in a string and return True if it's the same upside down, otherwise False
        return "".join(map(str, self.bucketItems)) == "".join(map(str, self.bucketItems[::-1]))
    
    def pairsWithSum(self, sum_value):
        pairs = list()

        for permutation in itertools.permutations(self.bucketItems, 2):
            if tuple(permutation) not in pairs and tuple(permutation[::-1]) not in pairs and sum(permutation) == sum_value:
                pairs.append(tuple(permutation))

        return pairs

class UnrolledLinkedList(object):
    def __init__(self, defaultCapacity = None, ULL_CAPACITY = None):
        '''
        The defaultCapacity represents the default capacity of each node bucket that will be added to the ULL
        The ULL_CAPACITY represents the maximum number of buckets
        '''
        
        if type(defaultCapacity) != int and defaultCapacity != None:
            raise ValueError("The defaultCapacity must be None or an integer")
        self.defaultCapacity = defaultCapacity

        if type(ULL_CAPACITY) != int and ULL_CAPACITY != None:
            raise ValueError("The ULL_CAPACITY must be None or an integer")
        self.ULL_CAPACITY = ULL_CAPACITY

        # Keep track of the number of buckets in the ULL
        self.bucketCounter = 0

        # Create the head bucket
        self.headBucket = None

    def getBucketCounter(self):
        return self.bucketCounter

    def getItems(self):
        items = list()
        current = self.headBucket

        while current:
            items.append(current.getItems())
            current = current.next

        return items

    def appendBucket(self, individualCapacity = None):
        newBucket = NodeBucket(individualCapacity)

        if not self.headBucket:
            self.headBucket = newBucket
        else:
            current = self.headBucket

            while current.next:
                current = current.next

            current.next = newBucket

        # Increment the number of buckets 
        self.bucketCounter += 1

    def appendItemToBucket(self, bucketIndex, item):
        # Check the bucket index
        if not 0 <= bucketIndex < self.bucketCounter:
            raise IndexError("The bucket index is either too big for the ULL or too small ( < 0 )")

        current = self.headBucket
        indexTrack = 0

        while indexTrack < bucketIndex:
            current = current.next
            indexTrack += 1

        current.appendToBucket(item)

    def deleteBucketAtIndex(self, bucketIndex):
        # Check the bucket index
        if not 0 <= bucketIndex < self.bucketCounter:
            raise IndexError("The bucket index is either too big for the ULL or too small ( < 0 )")

        if bucketIndex == 0:
            temp = self.headBucket
            self.headBucket = temp.next
            temp = None
        else:
            prev = None
            current = self.headBucket
            indexTrack = 0

            while indexTrack < bucketIndex:
                prev = current
                current = current.next

                indexTrack += 1

            prev.next = current.next
            current = None

        # Decrement bucket counter
        self.bucketCounter -= 1
