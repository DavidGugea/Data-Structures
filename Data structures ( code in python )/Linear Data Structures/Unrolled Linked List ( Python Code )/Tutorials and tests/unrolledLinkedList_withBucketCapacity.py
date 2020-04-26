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

        # Create two pointers that will scan the list 
        LP = low        # Swap ( var > pivot ) 
        RP = high - 1   # Swap ( var < pivot )

        # Scan the entire list using the pointers, swap the necessary items that must be swapped and finally find the position for the pointer
        while LP <= RP:
            if arr[LP] > pivot and arr[RP] < pivot:
                # Swap the values at the pointers
                arr[LP], arr[RP] = arr[RP], arr[LP]

                # Increment the left pointer
                LP += 1

                # Decrement the right pointer
                RP -= 1
            else:
                if arr[LP] < pivot: 
                    # Increment the left pointer
                    LP += 1
                if arr[RP] > pivot:
                    # Decrement the right pointer
                    RP -= 1
            
        # Swap the value at the pivot index ( the pivot ) with the left pointer value
        arr[LP], arr[pivotIndex] = arr[pivotIndex], arr[LP]

        # Update the pivot index
        pivotIndex = LP 

        # Return the pivot index ( found location of the pivot )
        return pivotIndex
    def quickSort(self, arr, low, high):
        if low <= high:
            # Get the border ( partition ) index
            partitionIndex = self.partition(arr, low, high)

            # Quick sort both halves
            self.quickSort(arr, partitionIndex + 1, high)
            self.quickSort(arr, low, partitionIndex - 1)
    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)

class NodeBucket(object):
    def __init__(self, capacity = None):
        self.capacity = capacity
        self.next = None

        self.nodeBucketItems = list()

    def getItems(self):
        return self.nodeBucketItems

    def getBucketLength(self):
        return len(self.nodeBucketItems)

    def __len__(self):
        return len(self.nodeBucketItems)

    def appendToBucket(self, item):
        if self.capacity is None:
            self.nodeBucketItems.append(item)
        else:
            if len(self) >= capacity:
                raise OverflowError("The node bucket is full of items, you can't add anything else in the bucket")

            self.nodeBucketItems.append(item)

    def extendBucket(self, listItems = list()):
        if self.capacity is None:
            self.nodeBucketItems.extend(listItems)
        else:
            if len(self) + listItems > self.capacity:
                raise OverflowError("The node bucket is full of items, you can't add anything else in the bucket")

            self.nodeBucketItems.extend(listItems)

    def sortBucket(self):
        # Sort using quick sort 
        quicksort_alg = QuickSort()
        quicksort_alg.sort(self.nodeBucketItems)

class unrolledLinkedList(object):
    def __init__(self, bucketCapacity = None):
        self.bucketCapacity = bucketCapacity
        self.headNodeBucket = None

        self.bucketCounter = 0
    def appendBucket(self):
        if self.bucketCounter == 0:
            self.headNodeBucket = NodeBucket(self.bucketCapacity)
        else:
            counter = 0
            appendBucket = NodeBucket()
            current = self.headNodeBucket
            
            while counter < self.bucketCounter - 1:
                counter += 1
                current = current.next
                
            current.next = appendBucket

        self.bucketCounter += 1
    def deleteBucket(self, indexToDeleteAt):
        if self.bucketCounter == 0:
            raise ValueError("There is no head node bucket. Hence there is nothing to delete, the unrolled linked list is completly empty")

        if not 0 <= indexToDeleteAt < self.bucketCounter:
            raise IndexError("The given index is either too big for the unrolled linked list or too small ( < 0 )")

        if indexToDeleteAt == 0:
            self.headNodeBucket = self.headNodeBucket.next
        else:
            indexTracker = 0
            
            currentBucket = self.headNodeBucket
            prevBucket = None

            while indexTracker != indexToDeleteAt:
                prevBucket = currentBucket
                currentBucket = currentBucket.next

                indexTracker += 1

            prevBucket.next = currentBucket.next
            currentBucket = None

        self.bucketCounter -= 1

    def appendItemToBucket(self, bucketIndex, itemToAppend):
        if self.bucketCounter == 0:
            raise Exception("There is no head bucket")

        if not 0 <= bucketIndex < self.bucketCounter:
            raise IndexError("The bucket index is either too big for the linked list or too small ( < 0 )")

        currentBucket = self.headNodeBucket
        indexTrack = 0        

        while indexTrack != bucketIndex:
            currentBucket = currentBucket.next
            indexTrack += 1

        currentBucket.appendToBucket(itemToAppend)

    def extendItemWithList(self, bucketIndex, extendList):
        if self.bucketCounter == 0:
            raise Exception("There is no head bucket")

        if not 0 <= bucketIndex < self.bucketCounter:
            raise IndexError("The bucket index is either too big for the linked list or too small ( < 0 )")

        currentBucket = self.headNodeBucket
        indexTrack = 0

        while indexTrack != bucketIndex:
            currentBucket = currentBucket.next
            indexTrack += 1

        currentBucket.extendBucket(extendList)

    def sortBucket(self, bucketIndex):
        if self.bucketCounter == 0:
            raise Exception("There is no head bucket")

        if not 0 <= bucketIndex < self.bucketCounter:
            raise IndexError("The bucket index is either too big for the linked list or too small ( < 0 )")

        currentBucket = self.headNodeBucket
        indexTrack = 0

        while indexTrack != bucketIndex:
            currentBucket = currentBucket.next
            indexTrack += 1

        currentBucket.sortBucket()

    def sortAllBuckets(self):
        currentBucket = self.headNodeBucket

        while currentBucket:
            currentBucket.sortBucket()
            currentBucket = currentBucket.next

    def getBucketValues(self):
        if self.bucketCounter == 0:
            raise Exception("There is no head node bucket. Hence there are no bucket values.") 

        bucketValues = list()
        counter = 0
        current = self.headNodeBucket
        
        while counter < self.bucketCounter:
            print("COUNTER : {0} | BUCKET COUNTER : {1}".format(counter, self.bucketCounter))
            
            bucketValues.append(current.getItems())
            current = current.next
            
            counter += 1

        return bucketValues